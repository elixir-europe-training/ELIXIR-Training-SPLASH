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
  category: topic           # organization, lifecycle, or topic
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

## Adding a New Category

If you want to create an entirely new category (beyond organization, lifecycle, topic):

### Step 1: Add tags with the new category in `_data/resource_tags.yml`

```yaml
# Your New Category Tags
- id: your-tag-id
  label: Display Name
  category: yourcategory    # Your new category name
  color: primary
  description: Tooltip description
```

### Step 2: Update `pages/resources/resources.md`

Find the line with category definitions (around line 27):
```liquid
{% assign categories = "organization,country,lifecycle,topic" | split: "," %}
```

Add your new category name to the comma-separated list:
```liquid
{% assign categories = "organization,country,lifecycle,topic,yourcategory" | split: "," %}
```

The new category will automatically appear as a separate filter section on the resources page, with all its tags grouped together.

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
