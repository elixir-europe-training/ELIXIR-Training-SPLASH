---
title: Adding and Managing Resources
---

This guide explains how to add new resources to the ELIXIR Training SPLASH website and manage the tag system for categorizing them.

## Adding a New Resource

### 1. Create a new resource page

Resources are located in the `pages/resources/` directory. To add a new resource:

1. Navigate to [`pages/resources/`](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH/tree/main/pages/resources)
2. Copy the [`TEMPLATE_resource_page.md`](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH/blob/main/pages/resources/TEMPLATE_resource_page.md) file
3. Rename it using lowercase with hyphens (e.g., `my-new-resource.md`)
4. Fill in the metadata fields (see below)

### 2. Fill in the resource metadata

The frontmatter (metadata) at the top of the file contains all resource information. Here are the key fields:

#### Mandatory fields

```yaml
---
id: unique-resource-id        # Unique identifier, use kebab-case
title: Resource Name           # Display name
resourceUrl: https://example.org/  # Link to the resource
description: |                 # Brief description (can be multiline markdown)
  Short description of the resource
objective: |                   # What the resource aims to achieve
  Main objectives and goals
contributors: [Name One, Name Two]  # List of contributors
coordinators: [Name One]       # Resource coordinators (must also be in contributors)
contacts:                      # Contact information
  - name: Contact Name
    email: contact@example.org
---
```

#### Optional but recommended fields

```yaml
tags: [elixir, plan, design]   # Resource tags (see Tag System below)
mission: |                     # Mission statement (multiline markdown)
  Resource mission
benefit: |                     # Benefits to users (multiline markdown)
  * Benefit 1
  * Benefit 2
logo: resource-logo.svg        # Logo filename (place in assets/img/logos/)
screenshots:                   # Screenshots (place in assets/img/screenshots/)
  - screenshot1.png
  - screenshot2.png
video: https://www.youtube.com/embed/VIDEO_ID  # YouTube embed URL only
publications:                  # Related publications
  - title: Publication title
    url: https://doi.org/...
licenses:                      # License information
  - name: CC BY 4.0
    icon: ccby.png
    url: https://creativecommons.org/licenses/by/4.0/
mailingList: https://...       # Link to mailing list
joinLink: https://...          # Link to join/participate
funding:                       # Funding information
  - name: Funder Name
    logo: funder-logo.png
    url: https://funder.org/
citations: |                   # How to cite the resource
  Citation information
```

### 3. Add resource logo and images

**Logo:**
- Add logo file to [`assets/img/logos/`](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH/tree/main/assets/img/logos)
- Use SVG format when possible
- Reference in frontmatter: `logo: your-logo.svg`

**Screenshots:**
- Add screenshots to [`assets/img/screenshots/`](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH/tree/main/assets/img/screenshots)
- Use descriptive filenames
- List in frontmatter under `screenshots:`

### 4. Add resource content

After the frontmatter, add the main content of the resource page using Markdown. Structure your content with clear headings:

```markdown
---
# frontmatter here
---

## Make your SPLASH! (Highlights)

Main highlights and key features of the resource.

* Feature 1
* Feature 2
* Feature 3

## Additional Information

More detailed information about the resource.
```

### 5. Add contributors to CONTRIBUTORS.yml

Ensure all contributors listed in the resource metadata are also in [`_data/CONTRIBUTORS.yml`](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH/blob/main/_data/CONTRIBUTORS.yml):

```yaml
Name Surname:
  git: github_username
  email: email@example.com
  orcid: 0000-0000-0000-0000
  affiliation: Institution Name
```

## Tag System for Resources

The tag system allows you to categorize resources with colored badges that appear on resource cards. Tags are centrally managed in `_data/resource_tags.yml` to ensure consistency across the site.

## Tag Categories

Tags are organized into categories defined in `_data/tag_categories.yml`. Each category has an associated color that applies to all tags within that category. Common categories include:
- **Organization** (red) - Resources affiliated with specific organizations
- **Node** (gray) - Resources specific to ELIXIR national nodes
- **Lifecycle** (green) - Training development phases (Plan, Design, Develop, Deliver, Evaluate)
- **Topic** (blue) - Subject areas and themes

To see current tags and categories, refer to:
- [`_data/resource_tags.yml`](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH/blob/main/_data/resource_tags.yml) - All available tags
- [`_data/tag_categories.yml`](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH/blob/main/_data/tag_categories.yml) - Category definitions

## How to Add Tags to a Resource

In the frontmatter of any resource page (e.g., `pages/resources/your-resource.md`), add a `tags` field with an array of tag IDs:

```yaml
---
id: your-resource
title: Your Resource Name
# ... other fields ...

# OPTIONAL FIELDS
tags: [elixir, plan, design, fair-training]
# ... rest of frontmatter ...
---
```

## Adding New Tags

To add a new tag to the system:

1. Open `_data/resource_tags.yml`
2. Add a new entry following this format:

```yaml
- id: your-tag-id           # Use kebab-case, no spaces
  label: Display Name       # How it appears on cards
  category: topic           # organization, country, lifecycle, topic, etc.
  description: Tooltip text # Optional: shown on hover
```

**Note:** The tag's color is automatically determined by its category (defined in `_data/tag_categories.yml`). All tags within the same category share the same color.

### Available Bootstrap Colors

Colors are defined at the category level in `_data/tag_categories.yml`. All tags within a category automatically inherit that category's color.

**Available Bootstrap color options:**
- <span class="badge bg-primary">primary</span> - Aubergine/purple (default theme color)
- <span class="badge bg-secondary">secondary</span> - Gray
- <span class="badge bg-success">success</span> - Green
- <span class="badge bg-danger">danger</span> - Red
- <span class="badge bg-warning">warning</span> - Orange/Yellow
- <span class="badge bg-info">info</span> - Light blue
- <span class="badge bg-light text-dark">light</span> - Light gray
- <span class="badge bg-dark">dark</span> - Dark gray/black

## Adding a New Category

To create an entirely new category, you only need to update one file:

### Add the category to `_data/tag_categories.yml`

```yaml
- id: yourcategory          # Use kebab-case, matches the category field in tags
  label: Your Category      # Display name (will be shown in uppercase)
  description: Explanation of what this category represents
  color: primary            # Bootstrap color class - all tags in this category will use this color
```

**That's it!** The category will automatically appear on the resources page in the order defined in `tag_categories.yml`. No changes needed to `resources.md`.

## Best Practices

1. **Limit tags per resource**: Use 3-7 tags for clarity
2. **Use consistent categories**: Include at least one organization or lifecycle tag
3. **Category colors**: Colors are managed at the category level - choose colors that visually distinguish categories
4. **Descriptive labels**: Keep labels short (1-3 words) but clear
5. **Meaningful descriptions**: Add helpful tooltip text for less obvious tags

## Where Tags Are Used

### Resources Page
- **Filter sidebar**: All tags appear as clickable filter buttons organized by category
- **Search functionality**: Tags are searchable via the search box
- **Tag deselection**: Click an active tag again to deselect it and return to "All Resources"
- **Resource cards**: Tags displayed on each card (in order defined in `resource_tags.yml`)

### Home Page Carousel
- Only shows resources tagged with `elixir`
- Displays only **lifecycle tags** on cards (organization, node, and topic tags are hidden)
- Randomized order on each build

### Lifecycle Pages (Plan, Design, Develop, Deliver, Evaluate)
- Automatically displays resources tagged with the corresponding lifecycle tag
- Shows full resource cards with logos, titles, and tags

## Technical Implementation

### Reusable Components

#### `_includes/related-resources.html`
A reusable Liquid component for displaying filtered resource cards:

```liquid
{% raw %}{% include related-resources.html tag="plan" %}{% endraw %}
```

This component:
- Filters resources by the specified tag
- Displays cards with logos, titles, and tag badges
- Used on all lifecycle pages (plan.md, design.md, etc.)

### Tag Ordering

Tags are displayed in the order they appear in `_data/resource_tags.yml`, NOT alphabetically. This allows you to control the visual priority of tags by reordering them in the file.

### Filtering Behavior

On the resources page:
- Clicking a tag filter shows only resources with that tag
- Clicking the same tag again deselects it (returns to "All Resources")
- The "All Resources" button always shows all resources
- Search works in combination with tag filters
