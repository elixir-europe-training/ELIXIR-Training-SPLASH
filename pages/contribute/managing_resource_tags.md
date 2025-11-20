---
title: Managing Resource Tags
---

This guide explains how to use and manage the tag system for categorizing resources on the ELIXIR Training SPLASH website.

## Overview

The tag system allows you to categorize resources with colored badges that appear on resource cards. Tags are centrally managed in `_data/resource_tags.yml` to ensure consistency across the site.

## Tag Categories

Tags are organized into categories defined in `_data/tag_categories.yml`. Common categories include:
- **Organization** - Resources affiliated with specific organizations
- **Node** - Resources specific to ELIXIR national nodes
- **Lifecycle** - Training development phases (Plan, Design, Develop, Deliver, Evaluate)
- **Topic** - Subject areas and themes

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
  category: topic           # organization, lifecycle, topic, country, etc.
  color: primary            # Bootstrap color: primary, secondary, success, danger, warning, info, light, dark
  description: Tooltip text # Optional: shown on hover
```

### Available Bootstrap Colors

- <span class="badge bg-primary">primary</span> - Aubergine/purple (default theme color)
- <span class="badge bg-secondary">secondary</span> - Gray
- <span class="badge bg-success">success</span> - Green
- <span class="badge bg-danger">danger</span> - Red
- <span class="badge bg-warning">warning</span> - Orange/Yellow
- <span class="badge bg-info">info</span> - Light blue
- <span class="badge bg-light text-dark">light</span> - Light gray
- <span class="badge bg-dark">dark</span> - Dark gray/black

**Note:** For consistency, use the same color for all tags within a category.

## Adding a New Category

To create an entirely new category, you only need to update one file:

### Add the category to `_data/tag_categories.yml`

```yaml
- id: yourcategory          # Use kebab-case, matches the category field in tags
  label: Your Category      # Display name (will be shown in uppercase)
  description: Explanation of what this category represents
```

**That's it!** The category will automatically appear on the resources page in the order defined in `tag_categories.yml`. No changes needed to `resources.md`.

### Example: Adding a "Format" Category

1. Add to `_data/tag_categories.yml`:
```yaml
- id: format
  label: Format
  description: The format or delivery method of the training resource
```

2. Add tags with this category in `_data/resource_tags.yml`:
```yaml
- id: online
  label: Online
  category: format
  color: warning
  description: Online/virtual training

- id: in-person
  label: In-Person
  category: format
  color: warning
  description: Face-to-face training
```

The "Format" category will automatically appear in the filter sidebar with an info icon showing the description.

## Adding Category Descriptions

Category descriptions appear as tooltips when users hover over the info icon (ℹ️) next to category labels.

To add or update a category description:

1. Open `_data/tag_categories.yml`
2. Add or modify the `description` field:

```yaml
- id: organization
  label: Organization
  description: Resources affiliated with specific organizations or collaborative networks
```

The description should briefly explain what the category represents and help users understand which tags to use for filtering.

## Best Practices

1. **Limit tags per resource**: Use 3-7 tags for clarity
2. **Use consistent categories**: Include at least one organization or lifecycle tag
3. **Color coding**: Use consistent colors per category (see `_data/resource_tags.yml` for current conventions)
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

## Examples

### Example 1: Training Platform
```yaml
tags: [elixir, catalogue, plan, design]
```

### Example 2: Training Course
```yaml
tags: [elixir, train-the-trainer, design, deliver, evaluate]
```

### Example 3: Node-Specific Resource
```yaml
tags: [elixir, ch, develop, elearning]
```

## Display

Tags appear as small colored badges below the resource title on resource cards. They help visitors quickly identify:
- Which organization provides or endorses the resource
- Which ELIXIR node(s) support the resource (if applicable)
- What phase(s) of the training lifecycle it supports
- What topic or domain it covers

Each tag has a tooltip that appears on hover, providing additional context about its meaning.

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
