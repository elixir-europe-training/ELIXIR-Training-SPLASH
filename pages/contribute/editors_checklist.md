---
title: Editors checklist
summary: Pre-merge checklist for pull request reviews.
---

Before approving and merging a pull request, verify:

## Content and presentation

* Page preview renders correctly
* Content follows the [style guide](style_guide)
* No [copyright](copyright) issues
* Contributors acknowledged and gave permission

## Metadata

### For resource pages

Verify required resource metadata fields (see [adding resources guide](adding_resources)):

* Unique `id` (use kebab-case)
* `title` provided
* `resourceUrl` links to the actual resource
* `description` clearly explains the resource
* `objective` describes what the resource aims to achieve
* `contributors` listed and added to [CONTRIBUTORS.yml](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH/blob/master/_data/CONTRIBUTORS.yml)
* `coordinators` listed (must also be in contributors)
* `contacts` provided with valid email addresses
* `tags` use existing tags from [resource_tags.yml](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH/blob/master/_data/resource_tags.yml) (3-7 tags recommended)
* `logo` file added to `assets/img/logos/` if provided
* `screenshots` added to `assets/img/screenshots/` if provided

### For other pages

Verify required fields (see [page metadata guide](https://elixir-belgium.github.io/elixir-toolkit-theme/page_mechanics)):

* Unique `page_id` ([check existing IDs](website_overview))
* `contributors` listed
* `description` provided
* `search_exclude` removed (unless intentionally excluded)
* `related_pages` configured if applicable
* `training` materials added if applicable
* `affiliation` specified if applicable

## Navigation and linking

* Page linked in appropriate [sidebar menu](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH/tree/master/_data/sidebars)
* Contributors added to [CONTRIBUTORS.yml](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH/blob/master/_data/CONTRIBUTORS.yml) with contact info
* Pull request linked to related issues
* No merge conflicts with main branch

## Review process

* Requested changes have been implemented
* Contributors thanked and informed about publication timeline
* All conversations resolved

## Final step

**The editor providing final approval should merge the pull request.**
