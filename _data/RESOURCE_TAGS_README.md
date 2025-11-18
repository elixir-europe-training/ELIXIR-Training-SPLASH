# Resource Tags System

This document explains how to use the tag system for categorizing resources on the ELIXIR Training SPLASH website.

## Overview

The tag system allows you to categorize resources with colored badges that appear on resource cards. Tags are centrally managed in `_data/resource_tags.yml` to ensure consistency across the site.

## Tag Categories

Tags are organized into three categories:

### 1. **Organization Tags** (Primary Blue / Info colors)
- `elixir` - ELIXIR Europe resource
- `goblet` - GOBLET collaboration

### 2. **Lifecycle Tags** (Success Green)
Tags corresponding to the training lifecycle phases:
- `plan` - Training planning phase
- `design` - Training design phase
- `develop` - Training development phase
- `deliver` - Training delivery phase
- `evaluate` - Training evaluation phase

### 3. **Topic Tags** (Various colors)
- `fair-training` - FAIR principles for training (Warning/Orange)
- `train-the-trainer` - Training for instructors (Danger/Red)
- `quality-metrics` - Training quality and impact assessment (Secondary/Gray)
- `materials-discovery` - Finding and curating training materials (Info/Blue)
- `elearning` - Online learning resources (Warning/Orange)
- `certification` - Training certification programs (Danger/Red)
- `community` - Community resources and groups (Info/Blue)

## How to Add Tags to a Resource

In the frontmatter of any resource page (e.g., `pages/resources/your-resource.md`), add a `tags` field with an array of tag IDs:

```yaml
---
id: your-resource
title: Your Resource Name
# ... other fields ...

#OPTIONAL FIELDS
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

- `primary` - ELIXIR blue (default theme color)
- `secondary` - Gray
- `success` - Green
- `danger` - Red
- `warning` - Orange/Yellow
- `info` - Light blue
- `light` - Light gray
- `dark` - Dark gray/black

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

1. **Limit tags per resource**: Use 3-5 tags maximum for clarity
2. **Use consistent categories**: Include at least one organization or lifecycle tag
3. **Color coding**: Use the same color for related concepts
   - Organization tags: `primary` or `info`
   - Lifecycle tags: `success` (green)
   - Topic tags: vary by theme
4. **Descriptive labels**: Keep labels short (1-3 words) but clear
5. **Meaningful descriptions**: Add helpful tooltip text for less obvious tags

## Examples

### Example 1: Training Platform
```yaml
tags: [elixir, materials-discovery, plan]
```
Displays: ELIXIR (blue), Materials Discovery (blue), Plan (green)

### Example 2: Training Course
```yaml
tags: [train-the-trainer, design, deliver]
```
Displays: Train-the-Trainer (red), Design (green), Deliver (green)

### Example 3: Community Resource
```yaml
tags: [elixir, community, fair-training]
```
Displays: ELIXIR (blue), Community (blue), FAIR Training (orange)

## Display

Tags appear as small colored badges below the resource title and above the funding information on resource cards. They help visitors quickly identify:
- Which organization provides the resource
- What phase of the training lifecycle it supports
- What topic or domain it covers

Each tag has a tooltip that appears on hover, providing additional context about its meaning.
