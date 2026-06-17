#!/usr/bin/env python3
"""Update the contributors field in .zenodo.json from _data/CONTRIBUTORS.yml.

Usage:
    python3 scripts/update_zenodo_contributors.py [--check-only]

Options:
    --check-only    Run consistency checks without writing .zenodo.json.

Run from the repository root. Reads _data/CONTRIBUTORS.yml and .zenodo.json,
runs consistency checks, replaces the contributors list, and writes the result
back to .zenodo.json.

Consistency checks (fail with non-zero exit if violated):
  1. Every person listed as creator or contributor in .zenodo.json must be
     present in CONTRIBUTORS.yml.
  2. GitHub contributors for the repository must be present in CONTRIBUTORS.yml.
     Set the GITHUB_REPOSITORY env var (e.g. "org/repo") to enable this check;
     it is skipped when the variable is absent (e.g. local runs without auth).
      Matching uses CONTRIBUTORS.yml fields `git` and optional `github_aliases`.
"""

import json
import os
import ssl
import sys
import urllib.request
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).parent.parent
CONTRIBUTORS_YML = REPO_ROOT / "_data" / "CONTRIBUTORS.yml"
ZENODO_JSON = REPO_ROOT / ".zenodo.json"

GITHUB_API = "https://api.github.com"


def build_ssl_context() -> ssl.SSLContext:
    """Build an SSL context, preferring certifi when available."""
    # Respect explicit user/system override first.
    ssl_cert_file = os.environ.get("SSL_CERT_FILE")
    if ssl_cert_file:
        return ssl.create_default_context(cafile=ssl_cert_file)

    # Fallback to certifi bundle when installed (helpful on some local setups).
    try:
        import certifi  # type: ignore

        return ssl.create_default_context(cafile=certifi.where())
    except Exception:
        return ssl.create_default_context()


def http_get_json(url: str, headers: dict) -> dict | list:
    """GET JSON over HTTPS with robust SSL handling and actionable errors."""
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, context=build_ssl_context()) as resp:
            return json.loads(resp.read())
    except ssl.SSLError as exc:
        raise RuntimeError(
            "TLS certificate verification failed while calling GitHub API. "
            "Try one of: 1) install certifi: 'pip install certifi', "
            "2) set SSL_CERT_FILE to your CA bundle path, "
            "3) on macOS Python.org build, run Install Certificates.command. "
            f"Original error: {exc}"
        ) from exc


def zenodo_name_to_given_family(name: str) -> str:
    """Convert 'Family, Given' → 'Given Family', leave other forms unchanged."""
    if "," in name:
        family, given = name.split(",", 1)
        return f"{given.strip()} {family.strip()}"
    return name.strip()


def fetch_github_contributors(repo: str) -> list[str]:
    """Return list of login strings for all human contributors of *repo*."""
    logins = []
    page = 1
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    while True:
        url = f"{GITHUB_API}/repos/{repo}/contributors?per_page=100&page={page}"
        data = http_get_json(url, headers)
        if not data:
            break
        for c in data:
            if c.get("type") == "User":
                logins.append(c["login"])
        page += 1

    return logins


def fetch_github_profile_name(login: str) -> str | None:
    """Return the display name for a GitHub login, or None if unavailable."""
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    url = f"{GITHUB_API}/users/{login}"
    try:
        data = http_get_json(url, headers)
        return data.get("name") or None
    except Exception:
        return None


def check_zenodo_in_contributors(zenodo: dict, yml_names: set) -> list[str]:
    """Return error messages for .zenodo.json people missing from CONTRIBUTORS.yml."""
    errors = []
    all_people = zenodo.get("creators", []) + zenodo.get("contributors", [])
    for person in all_people:
        given_family = zenodo_name_to_given_family(person["name"])
        if given_family not in yml_names:
            errors.append(
                f"  '{given_family}' is in .zenodo.json but not in CONTRIBUTORS.yml"
            )
    return errors


def build_known_logins(contributors_data: dict) -> set[str]:
    """Collect all known GitHub logins from `git` and `github_aliases` fields."""
    known_logins = set()
    for value in contributors_data.values():
        if not value:
            continue

        git_login = str(value.get("git") or "").strip().lower()
        if git_login:
            known_logins.add(git_login)

        aliases = value.get("github_aliases")
        if isinstance(aliases, str):
            alias = aliases.strip().lower()
            if alias:
                known_logins.add(alias)
        elif isinstance(aliases, list):
            for alias in aliases:
                alias_text = str(alias).strip().lower()
                if alias_text:
                    known_logins.add(alias_text)

    return known_logins


def check_github_in_contributors(repo: str, yml_names: set) -> list[str]:
    """Return error messages for GitHub contributors missing from CONTRIBUTORS.yml."""
    errors = []
    try:
        logins = fetch_github_contributors(repo)
    except Exception as exc:
        print(f"WARNING: Could not fetch GitHub contributors ({exc}), skipping check.")
        return []

    for login in logins:
        display_name = fetch_github_profile_name(login)
        if display_name and display_name in yml_names:
            continue
        # Fall back: check if any yml entry has this git login
        errors.append(
            f"  GitHub contributor '{login}'"
            + (f" ({display_name})" if display_name else "")
            + " is not in CONTRIBUTORS.yml"
        )
    return errors


def main():
    check_only = "--check-only" in sys.argv

    with open(CONTRIBUTORS_YML) as f:
        contributors_data = yaml.safe_load(f)

    with open(ZENODO_JSON) as f:
        zenodo = json.load(f)

    yml_names = set(contributors_data.keys())

    # ── Consistency check 1: .zenodo.json → CONTRIBUTORS.yml ────────────────
    errors = check_zenodo_in_contributors(zenodo, yml_names)
    if errors:
        print("ERROR: The following people are in .zenodo.json but missing from CONTRIBUTORS.yml:")
        print("\n".join(errors))
        print(
            "\nAdd them to _data/CONTRIBUTORS.yml before running this script."
        )
        sys.exit(1)

    # ── Consistency check 2: GitHub contributors → CONTRIBUTORS.yml ─────────
    repo = os.environ.get("GITHUB_REPOSITORY")
    if repo:
        # Build a set of all git logins known in CONTRIBUTORS.yml for fast lookup.
        known_logins = build_known_logins(contributors_data)
        yml_names_lower = {n.lower() for n in yml_names}

        try:
            logins = fetch_github_contributors(repo)
        except Exception as exc:
            print("ERROR: Could not fetch GitHub contributors; cannot verify consistency.")
            print(f"Reason: {exc}")
            sys.exit(2)

        github_errors = []
        for login in logins:
            if login.lower() in known_logins:
                continue
            display_name = fetch_github_profile_name(login)
            if display_name and display_name.lower() in yml_names_lower:
                continue
            github_errors.append(
                f"  GitHub login '{login}'"
                + (f" (display name: '{display_name}')" if display_name else "")
            )

        if github_errors:
            print("ERROR: The following GitHub contributors are not in CONTRIBUTORS.yml")
            print("(match by 'git:', 'github_aliases', or display name):")
            print("\n".join(github_errors))
            print(
                "\nAdd them to _data/CONTRIBUTORS.yml "
                "(include 'git: <login>' and/or 'github_aliases') "
                "before running this script."
            )
            sys.exit(1)
    else:
        print("INFO: GITHUB_REPOSITORY not set — skipping GitHub contributor check.")

    if check_only:
        print("All consistency checks passed.")
        return

    # ── Build contributors list from CONTRIBUTORS.yml ────────────────────────
    creator_given_family = set()
    for c in zenodo.get("creators", []):
        creator_given_family.add(zenodo_name_to_given_family(c["name"]))

    contributors = []
    for full_name, data in contributors_data.items():
        if full_name in creator_given_family:
            continue

        if data is None:
            data = {}

        # Convert "Given Family" → "Family, Given" by splitting on last space
        parts = full_name.rsplit(" ", 1)
        zenodo_name = f"{parts[1]}, {parts[0]}" if len(parts) == 2 else full_name

        entry = {
            "name": zenodo_name,
            "type": "ProjectMember",
        }

        orcid = str(data.get("orcid") or "").strip()
        if orcid:
            entry["orcid"] = orcid

        affiliation = str(data.get("affiliation") or "").strip()
        if affiliation:
            entry["affiliation"] = affiliation

        contributors.append(entry)

    zenodo["contributors"] = contributors

    with open(ZENODO_JSON, "w") as f:
        json.dump(zenodo, f, indent=4, ensure_ascii=False)
        f.write("\n")

    print(f"Wrote {len(contributors)} contributors to {ZENODO_JSON}")


if __name__ == "__main__":
    main()
