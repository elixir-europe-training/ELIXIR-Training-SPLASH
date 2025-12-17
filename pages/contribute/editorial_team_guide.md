---
title: Editorial team guide
summary: Guidelines for editors managing contributions and pull requests.
---

## Working with the repository

### General workflow

* Work on feature branches, not directly on `main`
* Open pull requests for review before merging to `main`
* Small fixes (typos) can be committed directly to `main`

### File structure

* Content pages are in [`pages/`](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH/tree/main/pages) directory
* Sidebar navigation is in [`_data/sidebars/`](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH/tree/main/_data/sidebars)
* Contributors metadata is in [`_data/CONTRIBUTORS.yml`](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH/blob/master/_data/CONTRIBUTORS.yml)

### Markdown file naming

* Use lowercase with underscores instead of spaces
* Ensure unique filenames across the entire site
* File `example.md` renders at `https://elixir-europe-training.github.io/ELIXIR-Training-SPLASH/example`

### GitHub checks

Pull requests trigger automated checks:
* Website build validation
* Tool/resource table validation

PRs cannot be merged if checks fail. Click the failed check for details.

## Managing issues and pull requests

### Issues

* Monitor [open issues](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH/issues) regularly
* Apply relevant labels
* Assign at least one editor to each issue
* Discuss with contributors via issue comments
* Link PRs to related issues

### Pull requests

* Editors responsible for changed files are automatically assigned
* All PRs must be assigned to at least one editor
* Review using GitHub's [review features](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests)
* Verify tags for pages, tools and resources
* The final approving editor should merge the PR
* Link PRs to issues using `closes #issue_number`, `fixes #issue_number`, or `resolves #issue_number`

Learn more: [Linking pull requests to issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue)

## Creating new pages

### Via GitHub web interface

1. Navigate to the appropriate `TEMPLATE_` file in [`pages/`](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH/tree/main/pages)
2. Click "Raw" to view the source
3. Copy all content
4. Go to the target directory → "Add file" → "Create new file"
5. Paste template content
6. Name the file (lowercase, underscores, unique)
7. Update frontmatter (see [page metadata guide](https://elixir-belgium.github.io/elixir-toolkit-theme/page_mechanics)):
   * Remove `search_exclude: true`
   * Add contributor names
   * Update title if needed
8. Commit to a new branch
9. Create pull request for review

### Via Git

Follow the [Git workflow](contributing_via_github#git-workflow) for local development.

## Adding pages to navigation

By default, new pages exist as orphans at their URL. Add them to navigation or link from existing pages.

### Sidebar navigation

Edit the relevant `.yml` file in [`_data/sidebars/`](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH/tree/main/_data/sidebars):

```yaml
- title: Level_1_title
  url: /page_name
  subitems:
    - title: Level_2_title
      url: /subpage_name
```

**Attributes:**
* `title`: Display text in sidebar
* `url`: Internal page path (e.g., `/example`)  
* `external_url`: Use for external links instead of `url`
* `subitems`: Create hierarchy levels

## Managing contributors

Add contributor details to [`_data/CONTRIBUTORS.yml`](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH/blob/master/_data/CONTRIBUTORS.yml):

```yaml
Name Surname:
  git: github_username
  email: email@example.com
  orcid: 0000-0000-0000-0000
  role: editor
  affiliation: Institution Name
```

Names in this file must match exactly those used in page metadata.

## Managing affiliations

Institutions, projects, funders and infrastructures are in [`_data/affiliations.yml`](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH/blob/master/_data/affiliations.yml):

```yaml
- name: Institution Name
  image_url: /images/institutions/logo.svg
  pid: https://ror.org/unique_id
  expose: true
  type: institution
  url: https://www.institution.org
```

**Attributes:**
* `name`: Institution name (must match usage in pages)
* `image_url`: Relative path to logo
* `pid`: ROR identifier URL
* `expose`: Set `true` to display in About section
* `type`: `institution`, `funder`, `infrastructure`, or `project`
* `url`: Homepage URL

**Logo directories:**
* `/assets/img/logos/institutions/`
* `/assets/img/logos/projects/`
* `/assets/img/logos/infrastructures/`
* `/assets/img/logos/funders/`

{% include callout.html type="tip" content="Use vector images (SVG) for better quality and smaller file sizes." %}
  url: https://www.vib.be/
```

- `name`: name
- `image_url`: relative url towards the image
- `pid`: url including the unique identifier towards the page of the association on [ROR](https://ror.org)
- `expose`: true or false, when true this association will be shown in the about section
- `type`: can be any of these values: *institution*, *funder*, *infrastructure* or *project*
- `url`: url towards the homepage of this association


The logos can be added to the [/images/institutions](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH/blob/main/images/institutions/), [/images/projects](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH/blob/main/images/projects/), [/images/infrastructures](https://github.com/eelixir-europe-training/ELIXIR-Training-SPLASH/blob/main/images/infrastructures/) and [/images/funders](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH/blob/main/images/funders/) directory.

{% include callout.html type="important" content="Upload vector images (.svg filetype) of the institute logo for better quality, scaleability and file size, if possible." %}


{% glossary TODO %}:


```yml
related_pages: 
   your_tasks: [page_id1, page_id2]
   your_domain: [page_id1, page_id2]
   tool_assembly: [page_id1, page_id2]
  ``` 


### Page ID

To find out what the `page_id` of an Training SPLASH page is, please check its metadata attribute `page_id` at the top of the markdown file or the [list of page IDs](website_overview).

