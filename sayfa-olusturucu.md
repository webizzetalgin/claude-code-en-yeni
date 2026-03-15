---
name: elementor-json-generator
description: Generate valid Elementor Template JSON files that can be directly imported into WordPress Elementor. Use this skill whenever a user wants to create an Elementor page template, asks for Elementor JSON, mentions 'Elementor şablon', 'Elementor template', 'Elementor JSON', 'Elementor import', or wants to build a WordPress page layout as an importable JSON file. Also trigger when the user provides section-by-section content and wants it turned into an Elementor-compatible page, or mentions 'sayfa şablonu', 'landing page JSON', 'hizmet sayfası şablonu', or any request combining page content with Elementor output. This skill handles the full Elementor JSON structure including sections, columns, widgets, styling, and responsive settings — producing a file ready for Elementor's import feature.
---

# Elementor JSON Template Generator

Generate valid, import-ready Elementor Template JSON files from user-provided content, reference design cues, and color preferences. The output is a `.json` file the user can directly import via Elementor > Templates > Import.

## When This Skill Triggers

- User wants to create a WordPress page using Elementor and needs a JSON template
- User provides section-by-section content (headings, paragraphs, buttons) and wants Elementor output
- User mentions Elementor JSON, Elementor şablon, Elementor template, Elementor import
- User asks for a landing page, service page, about page, or any page type as an Elementor file
- User provides a reference URL + content + color and expects an importable template

## Required Inputs (5 Items)

Before generating, confirm the user has provided:

1. **Referans Kaynak Linki** — A reference URL for layout/design inspiration
2. **Sayfa Türü / Amacı** — Page type (landing page, service page, about page, etc.)
3. **Ana Renk** — Primary color hex code (e.g., `#2563EB`)
4. **Bölüm Bölüm İçerikler** — Section-by-section content (headings, paragraphs, button text)
5. **JSON Formatı Bildirimi** — Confirmation that output should be Elementor Template JSON

If any input is missing, ask for it before proceeding. Do not guess or fill in missing content.

## Core Rules (Non-Negotiable)

### Rule 1: Strict Content Fidelity
- Use ONLY the exact text the user provides — headings, paragraphs, button labels, nothing more
- NEVER invent, supplement, or add placeholder text (no lorem ipsum, no "Learn More" unless user said it)
- If a section seems incomplete, leave it as-is; do not fill gaps with assumed content
- Map user's "1. Bölüm", "2. Bölüm" etc. directly to sequential Elementor sections

### Rule 2: Design & Reference Alignment
- Analyze the reference URL's layout pattern: hero sections, grid layouts, spacing rhythm, typography hierarchy
- Use the reference's structural patterns (section ordering, column ratios, whitespace) as a guide
- Apply the user's primary color to buttons, accent elements, icon colors, and section highlights
- Keep the structure clean: Section > Column > Widget hierarchy, avoid unnecessary nesting
- Use standard Elementor spacing: sections typically 60-100px padding top/bottom, content areas 20-40px gaps

### Rule 3: SEO & UX Best Practices
- Use proper heading hierarchy (only one H1 per page, then H2 for sections, H3 for subsections)
- Keep the widget tree flat — avoid inner sections unless a multi-column layout genuinely requires them
- Include responsive padding/margin adjustments in `_responsive_settings` where appropriate

### Rule 4: Isolation & Safety
- The template must be a Page Template only — no theme overrides
- Do not include global styles, theme builder settings, or site-wide CSS
- Do not include header/footer sections — only page content sections
- Avoid custom CSS that could leak into the global scope

### Rule 5: Valid Elementor JSON Structure
- Output must be a complete, valid JSON file importable via Elementor Templates > Import
- Use standard Elementor widget types: `heading`, `text-editor`, `button`, `image`, `spacer`, `icon-box`, `divider`, etc.
- Every element must have a unique `id` (8-character random hex string)
- Include proper `page_settings`, `version`, and `type` metadata

## JSON Structure Reference

The output JSON must follow this exact top-level structure:

```json
{
  "title": "Page Title",
  "type": "page",
  "version": "0.4",
  "page_settings": {
    "template": "elementor_canvas"
  },
  "content": [
    {
      "id": "abc12345",
      "elType": "section",
      "settings": { ... },
      "elements": [
        {
          "id": "def67890",
          "elType": "column",
          "settings": { "_column_size": 100 },
          "elements": [
            {
              "id": "ghi11223",
              "elType": "widget",
              "widgetType": "heading",
              "settings": {
                "title": "User's Exact Heading Text",
                "header_size": "h2",
                "align": "center",
                "title_color": "#2563EB",
                "typography_typography": "custom",
                "typography_font_family": "Poppins",
                "typography_font_size": { "unit": "px", "size": 36 },
                "typography_font_weight": "600"
              },
              "elements": []
            }
          ]
        }
      ]
    }
  ]
}
```

## Widget Templates

### Heading Widget
```json
{
  "id": "UNIQUE_8CHAR",
  "elType": "widget",
  "widgetType": "heading",
  "settings": {
    "title": "EXACT USER TEXT",
    "header_size": "h1|h2|h3",
    "align": "left|center|right",
    "title_color": "#HEX",
    "typography_typography": "custom",
    "typography_font_family": "Font Name",
    "typography_font_size": { "unit": "px", "size": 36 },
    "typography_font_weight": "600"
  },
  "elements": []
}
```

### Text Editor Widget
```json
{
  "id": "UNIQUE_8CHAR",
  "elType": "widget",
  "widgetType": "text-editor",
  "settings": {
    "editor": "<p>EXACT USER PARAGRAPH TEXT</p>",
    "align": "left|center|justify",
    "text_color": "#333333",
    "typography_typography": "custom",
    "typography_font_family": "Open Sans",
    "typography_font_size": { "unit": "px", "size": 16 },
    "typography_line_height": { "unit": "em", "size": 1.7 }
  },
  "elements": []
}
```

### Button Widget
```json
{
  "id": "UNIQUE_8CHAR",
  "elType": "widget",
  "widgetType": "button",
  "settings": {
    "text": "EXACT USER BUTTON TEXT",
    "align": "center",
    "size": "md",
    "background_color": "#PRIMARY_COLOR",
    "button_text_color": "#FFFFFF",
    "border_radius": { "unit": "px", "top": "8", "right": "8", "bottom": "8", "left": "8", "isLinked": true },
    "typography_typography": "custom",
    "typography_font_family": "Poppins",
    "typography_font_size": { "unit": "px", "size": 16 },
    "typography_font_weight": "600",
    "button_hover_color": "#DARKER_PRIMARY",
    "link": { "url": "#", "is_external": false, "nofollow": false }
  },
  "elements": []
}
```

### Image Widget
```json
{
  "id": "UNIQUE_8CHAR",
  "elType": "widget",
  "widgetType": "image",
  "settings": {
    "image": {
      "url": "https://placeholder.co/800x400",
      "id": ""
    },
    "image_size": "full",
    "align": "center",
    "caption": ""
  },
  "elements": []
}
```

### Spacer Widget
```json
{
  "id": "UNIQUE_8CHAR",
  "elType": "widget",
  "widgetType": "spacer",
  "settings": {
    "space": { "unit": "px", "size": 40 }
  },
  "elements": []
}
```

### Divider Widget
```json
{
  "id": "UNIQUE_8CHAR",
  "elType": "widget",
  "widgetType": "divider",
  "settings": {
    "style": "solid",
    "weight": { "unit": "px", "size": 2 },
    "width": { "unit": "%", "size": 20 },
    "color": "#PRIMARY_COLOR",
    "align": "center",
    "gap": { "unit": "px", "size": 20 }
  },
  "elements": []
}
```

## Section Settings Patterns

### Standard Content Section
```json
{
  "padding": {
    "unit": "px",
    "top": "80",
    "right": "0",
    "bottom": "80",
    "left": "0",
    "isLinked": false
  },
  "background_background": "classic",
  "background_color": "#FFFFFF"
}
```

### Colored Background Section
```json
{
  "padding": {
    "unit": "px",
    "top": "80",
    "right": "0",
    "bottom": "80",
    "left": "0",
    "isLinked": false
  },
  "background_background": "classic",
  "background_color": "#F8F9FA"
}
```

### Hero Section (Full Width)
```json
{
  "padding": {
    "unit": "px",
    "top": "120",
    "right": "0",
    "bottom": "120",
    "left": "0",
    "isLinked": false
  },
  "background_background": "classic",
  "background_color": "#PRIMARY_COLOR",
  "layout": "full_width"
}
```

## Multi-Column Layouts

For sections that need multiple columns (e.g., features grid, services):

```json
{
  "id": "SECTION_ID",
  "elType": "section",
  "settings": {
    "structure": "30",
    "padding": { "unit": "px", "top": "80", "right": "0", "bottom": "80", "left": "0", "isLinked": false }
  },
  "elements": [
    {
      "id": "COL1_ID",
      "elType": "column",
      "settings": { "_column_size": 33 },
      "elements": [ /* widgets */ ]
    },
    {
      "id": "COL2_ID",
      "elType": "column",
      "settings": { "_column_size": 33 },
      "elements": [ /* widgets */ ]
    },
    {
      "id": "COL3_ID",
      "elType": "column",
      "settings": { "_column_size": 33 },
      "elements": [ /* widgets */ ]
    }
  ]
}
```

Column structures: `10` = 1 col (100%), `20` = 2 col (50/50), `30` = 3 col (33/33/33), `40` = 4 col (25x4).
For asymmetric: use `_column_size` values that sum to 100 (e.g., 60 + 40 for a 60/40 split).

## Page Type Patterns

### Landing Page
- Hero section with large heading (H1), subtitle paragraph, CTA button
- Features/benefits section (multi-column grid)
- Detail sections (alternating image + text)
- CTA section at bottom

### Hizmet (Service) Sayfası
- Hero with service title (H1) and brief description
- Service details in content sections
- Benefits or process steps
- Contact CTA

### Hakkımızda (About) Sayfası
- Company intro hero
- Story/mission section
- Team or values section
- CTA section

### İletişim (Contact) Sayfası
- Contact heading
- Contact info (address, phone, email as text-editor widgets)
- Map placeholder image
- Simple CTA or form placeholder note

## Step-by-Step Workflow

### 1. Validate Inputs
Confirm all 5 required inputs are present. If missing, ask before proceeding.

### 2. Fetch & Analyze Reference
```bash
# Use web_fetch to analyze the reference URL's structure
```
Identify from the reference:
- Section ordering and layout patterns
- Column ratios (full-width, 50/50, 60/40, 33/33/33)
- Spacing rhythm (padding, margins between elements)
- Typography hierarchy (heading sizes, body font)
- Visual accents (colored sections, dividers, icons)

### 3. Map Content to Sections
Take the user's numbered sections and assign each to an Elementor section:
- "1. Bölüm" → First `elType: section` in the content array
- "2. Bölüm" → Second section, and so on
- Within each section, map headings to `heading` widgets, paragraphs to `text-editor` widgets, button text to `button` widgets

### 4. Generate IDs
Every element needs a unique 8-character hex ID. Generate them randomly:
```python
import random
def gen_id():
    return ''.join(random.choices('0123456789abcdef', k=8))
```

### 5. Build the JSON
Assemble the full structure following the JSON Structure Reference above. Apply:
- The user's primary color to buttons, accents, heading highlights
- Section padding based on the reference pattern
- Proper heading hierarchy (H1 only in hero, H2 for section titles, H3 for sub-items)
- Clean widget tree — no unnecessary nesting

### 6. Validate & Output
- Verify the JSON is valid (parseable, no trailing commas, proper nesting)
- Save to `/mnt/user-data/outputs/elementor-template.json`
- Present using `present_files`

## ID Generation

Use Python to generate the template with proper random IDs:

```python
import json
import random
import string

def generate_id():
    return ''.join(random.choices(string.hexdigits[:16], k=8))

# Build the template structure
template = {
    "title": "PAGE_TITLE",
    "type": "page",
    "version": "0.4",
    "page_settings": {
        "template": "elementor_canvas"
    },
    "content": []
}

# ... build sections, columns, widgets with generate_id() for each ...

# Write output
with open('/mnt/user-data/outputs/elementor-template.json', 'w', encoding='utf-8') as f:
    json.dump(template, f, ensure_ascii=False, indent=2)
```

## Quality Checklist (Verify Before Output)

- [ ] All text content matches user input EXACTLY — no added or changed words
- [ ] Only one H1 heading on the entire page (in the hero/first section)
- [ ] Every element has a unique 8-character hex `id`
- [ ] Primary color is applied to buttons, accents, and key visual elements
- [ ] Section structure matches the reference URL's layout pattern
- [ ] JSON is valid and parseable (no syntax errors)
- [ ] No global styles, theme overrides, or header/footer elements
- [ ] `page_settings.template` is set to `elementor_canvas` or appropriate value
- [ ] `type` is `page` and `version` is `0.4`
- [ ] Responsive padding/font adjustments included where appropriate
- [ ] No lorem ipsum or placeholder text in content areas
- [ ] Button links default to `#` unless user specified a URL
- [ ] Image widgets use placeholder URLs with clear comments for replacement

## Common Mistakes to Avoid

1. **Adding text the user didn't provide** — This is the #1 violation. If the user gave 3 sections, output exactly 3 sections.
2. **Wrong heading hierarchy** — Don't use multiple H1s. The page should have one H1, then H2s for sections.
3. **Missing element IDs** — Every section, column, and widget MUST have a unique `id`.
4. **Invalid JSON** — Trailing commas, mismatched brackets, or unescaped characters in text content will break the import.
5. **Nested inner sections** — Keep the structure flat. Only use inner sections if the layout genuinely requires a grid within a grid.
6. **Hardcoding font sizes without units** — Always use the `{ "unit": "px", "size": N }` format for sizes.
7. **Forgetting `elements: []`** — Every widget must have an empty `elements` array, even leaf nodes.

## Final Output

- Write the complete JSON to `/mnt/user-data/outputs/elementor-template.json`
- Use `present_files` to share with the user
- Before the JSON file, provide 1-2 sentences confirming what was built
- If the user wants the raw JSON in chat as well, provide it in a code block AFTER the file
