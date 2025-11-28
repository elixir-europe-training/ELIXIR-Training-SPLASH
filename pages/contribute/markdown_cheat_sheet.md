---
title: Markdown cheat sheet
summary: Quick reference for SPLASH-specific formatting.
contributors: [Bert Droesbeke]
search_exclude: true
---

This page provides quick examples of SPLASH-specific formatting. For comprehensive documentation:

* **Basic Markdown**: [GitHub's Markdown guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
* **Page metadata and attributes**: [ELIXIR Toolkit Theme - Page mechanics](https://elixir-belgium.github.io/elixir-toolkit-theme/page_mechanics)
* **Complete formatting guide**: [ELIXIR Toolkit Theme - Markdown cheat sheet](https://elixir-belgium.github.io/elixir-toolkit-theme/markdown_cheat_sheet)

We use [Kramdown](https://kramdown.gettalong.org/parser/kramdown.html) for advanced Markdown features.

## Message boxes

Use callouts to highlight important information:

{% include callout.html type="note" content="This is a note." %}

{% include callout.html type="tip" content="This is a tip." %}

{% include callout.html type="warning" content="This is a warning." %}

{% include callout.html type="important" content="This is important information." %}

Code:
{% raw %}
```
{% include callout.html type="note" content="Your message here." %}
```
{% endraw %}

Replace `note` with `tip`, `warning`, or `important` as needed.

## Images

{% include image.html file="/infrastructures/ELIXIR-logo.svg" caption="Figure 1. Image with caption." alt="ELIXIR logo" %}

Code:
{% raw %}
```
{% include image.html file="/infrastructures/ELIXIR-logo.svg" caption="Figure 1. Image with caption." alt="ELIXIR logo" %}
```
{% endraw %}

**Attributes:**
* `file`: Path to image in `/assets/img/` directory (required)
* `alt`: Description for accessibility (required)
* `caption`: Text displayed below image
* `max-width`: Maximum width (e.g., `"10em"` or `"300px"`)
* `click`: Set to `true` to make image clickable
* `url`: Custom link destination
* `inline`: Set to `true` for use in lists

Smaller image example:
{% include image.html file="infrastructures/ELIXIR-logo.svg" alt="ELIXIR logo" max-width="3em" %}

Code:
{% raw %}
```
{% include image.html file="infrastructures/ELIXIR-logo.svg" alt="ELIXIR logo" max-width="3em" %}
```
{% endraw %}

## Tables

```md
| Priority apples | Second priority | Third priority |
|-------|--------|---------|
| ambrosia | gala | red delicious |
| pink lady | jazz | macintosh |
| honeycrisp | granny smith | fuji |
```

**Result:**

| Priority apples | Second priority | Third priority |
|-------|--------|---------|
| ambrosia | gala | red delicious |
| pink lady | jazz | macintosh |
| honeycrisp | granny smith | fuji |

## Icons

We use [Font Awesome](https://fontawesome.com/) icons. Example:

```html
<i class="fa-solid fa-camera-retro"></i> normal
<i class="fa-solid fa-camera-retro fa-2x"></i> 2x size
<i class="fa-solid fa-camera-retro fa-3x"></i> 3x size
```

**Result:**
<i class="fa-solid fa-camera-retro"></i> normal
<i class="fa-solid fa-camera-retro fa-2x"></i> 2x
<i class="fa-solid fa-camera-retro fa-3x"></i> 3x

## Code snippets

Use fenced code blocks with language specification for syntax highlighting:

<pre>
```python
def hello_world():
    print("Hello, world!")
```
</pre>

**Result:**

```python
def hello_world():
    print("Hello, world!")
```

## Links

**External links:**
```md
[GitHub Documentation](https://docs.github.com)
```

**Internal pages:**
```md
[Style guide](style_guide)
```

{% include callout.html type="important" content="If you change file names, internal links must be updated manually." %}

## Additional Markdown syntax

For lists, headings, bold/italic text, emojis, collapsible sections, and other standard Markdown features, refer to:
* [GitHub's Markdown guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
* [Kramdown documentation](https://kramdown.gettalong.org/quickref.html)
* [Emoji cheat sheet](https://github.com/ikatyang/emoji-cheat-sheet)
