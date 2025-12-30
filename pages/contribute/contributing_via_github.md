---
title: Contributing via GitHub
---

This guide shows you how to contribute to the ELIXIR Training SPLASH website using GitHub. Choose the workflow that suits your experience level.

## Prerequisites

[Create a free GitHub account](https://github.com/join) if you don't have one already.

## Contributing via web browser

Perfect if you're new to Git/GitHub or want to make changes without installing software.

### 1. Discuss your proposal

Before making changes, create or find a relevant issue:

1. Visit the [ELIXIR Training SPLASH repository](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH/issues)
2. Search existing issues to avoid duplicates
3. Create a new issue if needed (use one of our templates)
4. Discuss your idea with editors in the issue comments

Learn more: [GitHub's guide to creating issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue)

### 2. Fork the repository

Create your own copy of the repository:

1. Go to the [ELIXIR Training SPLASH repository](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH)
2. Click the **Fork** button in the top-right corner
3. Select your account as the destination
4. Wait for GitHub to create your fork

Your fork will be at `https://github.com/YOUR-USERNAME/ELIXIR-Training-SPLASH`

Learn more: [Forking a repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)

### 3. Make your changes

**To edit an existing file:**
1. In your fork, navigate to the file you want to edit (e.g., `pages/resources/`)
2. Click the pencil icon (✏️ Edit this file) in the top-right
3. Make your changes using [Markdown](https://elixir-belgium.github.io/elixir-toolkit-theme/markdown_cheat_sheet)
4. Preview your changes using the "Preview" tab

**To create a new resource:**
1. In your fork, go to `pages/resources/`
2. Click **Add file** → **Create new file**
3. Copy content from [`TEMPLATE_resource_page.md`](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH/blob/main/pages/resources/TEMPLATE_resource_page.md)
4. Name your file (e.g., `my-resource.md`)
5. Fill in the template with your resource information

**Formatting guidelines:**
* Follow our [style guide](style_guide)
* Check the [page metadata guide](https://elixir-belgium.github.io/elixir-toolkit-theme/page_mechanics) for frontmatter
* See [adding resources](adding_resources) for resource-specific instructions

### 4. Commit your changes

1. Scroll to the bottom of the edit page to "Commit changes"
2. Select **"Create a new branch for this commit and start a pull request"**
3. Give your branch a descriptive name (e.g., `add-my-resource`)
4. Write a brief commit message describing what you changed
5. Click **Propose changes**

Learn more: [Committing changes](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files#committing-changes)

### 5. Create a pull request

After proposing changes, you'll be taken to the "Open a pull request" page:

1. Write a clear title for your pull request
2. In the description:
   * Explain what you changed and why
   * Link to the related issue by typing `#issue_number` (e.g., `Fixes #123`)
3. Choose the pull request type:
   * **"Create draft pull request"** - if you're still working (can mark "Ready for review" later)
   * **"Create pull request"** - if you're ready for editor review
4. Click the green button to create the pull request

Your pull request will appear at [ELIXIR-Training-SPLASH/pulls](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH/pulls)

Learn more: [Creating a pull request from a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)

### 6. Make additional changes (if needed)

If you need to update your pull request before or after review:

1. Go to your fork: `https://github.com/YOUR-USERNAME/ELIXIR-Training-SPLASH`
2. Switch to your branch using the branch dropdown
3. Navigate to the file and click the pencil icon (✏️)
4. Make your changes
5. Commit directly to your branch (same branch name as before)
6. Changes automatically appear in your pull request

### 7. Respond to review comments

When editors review your pull request:

1. You'll receive notifications about comments
2. Read the feedback and respond to questions
3. Make requested changes following step 6 above
4. Reply to comments to let editors know you've addressed them
5. Editors will mark conversations as "Resolved" when satisfied

Learn more: [Commenting on pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/commenting-on-a-pull-request)

### 8. Merge and celebrate! 🎉

Once editors approve your changes:
* An editor will merge your pull request
* Your contributions will appear on the live website
* You'll be listed as a contributor (if you added yourself to the metadata)

## Git workflow

For contributors familiar with Git who want to work locally and preview changes.

### Fork and clone

```bash
# Fork the repository via GitHub web interface first, then:
git clone https://github.com/YOUR-USERNAME/ELIXIR-Training-SPLASH.git
cd ELIXIR-Training-SPLASH

# Add upstream remote to sync with main repository
git remote add upstream https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH.git
```

### Keep your fork updated

```bash
# Sync your fork with the main repository before starting new work
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

### Create a feature branch

```bash
# Create and switch to a new branch for your changes
git checkout -b descriptive-feature-name
```

### Make changes and commit

```bash
# Make your changes using your preferred editor
# Stage all changes
git add .

# Or stage specific files
git add path/to/file

# Commit with a descriptive message
git commit -m "Brief description of your changes"
```

### Push and create pull request

```bash
# Push your branch to your fork
git push origin descriptive-feature-name
```

Then visit [github.com/elixir-europe-training/ELIXIR-Training-SPLASH](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH) and click "Compare & pull request".

Learn more: [Creating a pull request from a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)

### Preview changes locally

See our [preview changes guide](preview_changes) for instructions on running the website locally using Docker or Jekyll.

## Need help?

* Check [GitHub's documentation](https://docs.github.com)
* Ask questions in your issue or pull request
* Contact the editorial team via [training-splash@elixir-europe.org](mailto:training-splash@elixir-europe.org)
