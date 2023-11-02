---
title: Editors checklist
summary: Checklist for editors before approving and merging a pull request (PR).
---

## Before approving and merging a pull request (PR), the editors must check that
1. The page layout in preview looks correct.
2. The new page is linked in the appropriate [sidebar](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH/tree/master/_data/sidebars) menu, in the same branch of the PR.
3. The contributors' names are listed in the [CONTRIBUTORS file](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH/blob/master/_data/CONTRIBUTORS.yaml), in the same branch of the PR. Advice to have at least one  contributor per page having its contact information in this  [CONTRIBUTORS file](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH/blob/master/_data/CONTRIBUTORS.yaml).
4. All relevant metadata fields in a specific page are correctly filled in (see the [page metadata](page_metadata) and the [Editorial board guide](editorial_board_guide)). Some critical ones are listed below.
   * unique `page_id` ([List of page IDs](website_overview))
   * `contributors`
   * `related_pages` ([Related pages](editorial_board_guide.html#related-pages))
   * `training`
   * `search_exclude` must be deleted
   * `description`
   * `affiliation`
   * `coordinators`(only used in national pages + they must be listed as `contributors` as well)
   * `resources`
5. The content is conform to ELIXIR Training SPLASH scope, [style](style_guide) and templates.
6. There are no [copyright](copyright) issues related to the content of the page.
7. The contributors implemented the requested changes.
8. The contributors are thanked for their effort and informed about the publication of their content.
9. The PR is linked to related issues and can be merged in main branch with no conflicts.
