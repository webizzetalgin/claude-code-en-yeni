---
name: elementor-json-template
description: Generate Elementor-importable JSON page templates from user-provided content, reference website, and brand colors. Use this skill whenever the user asks to create an Elementor template, Elementor JSON, Elementor page layout, Elementor section, or any importable Elementor structure. Also trigger when the user mentions 'Elementor şablonu', 'Elementor JSON', 'Elementor sayfa tasarımı', 'Elementor içe aktar', 'Elementor template', 'sayfa JSON', or asks for a page design that should work inside Elementor. Trigger even if the user simply says 'create a landing page for Elementor', 'Elementor hizmet sayfası', or 'make this design Elementor-compatible'. This skill handles full JSON structure generation with responsive settings, widget configuration, and Elementor-native formatting.
---

# Elementor JSON Template Generator

Generate production-ready, Elementor-importable JSON page templates that faithfully reproduce a reference website's layout using only the content the user provides.

## When This Skill Triggers

- User wants an Elementor page template as JSON
- User asks for an importable Elementor layout/structure
- User provides a reference website + content sections + brand color and expects Elementor output
- User mentions Elementor JSON, Elementor şablonu, Elementor template, sayfa tasarımı
- User wants to convert a design concept into Elementor-ready format

## Required User Inputs

Before generating, collect these from the user:

1. **Referans Linki** — The reference website URL to analyze for layout/structure
2. **Sayfa Türü** — Page type (landing page, service page, contact, about, etc.)
3. **Ana Renk** — Primary brand color in HEX format
4. **İçerik (Bölüm Bölüm)** — Numbered sections with exact headings and body text

If any of these are missing, ask the user before proceeding.

## Absolute Rules

These rules are non-negotiable. Violating any one produces a broken or unusable template.

### Rule 1: Zero Text Invention
Use ONLY the exact text the user provides. Never add placeholder text, lorem ipsum, extra subheadings, taglines, CTAs, or any words not explicitly given. If a section has only a heading and no body text, output only the heading widget. If the user gives no button text, do not create a button.

### Rule 2: Reference-Faithful Structure
Analyze the reference website's layout patterns (hero sections, grid columns, card layouts, spacing rhythm) and replicate them structurally in the JSON. The Elementor structure should mirror the reference's visual hierarchy — section divisions, column ratios, spacing proportions, and alignment patterns.

### Rule 3: Valid Elementor JSON Format
The output must be a valid Elementor template JSON that can be imported via Elementor > Templates > Import. Follow the exact schema Elementor expects (see JSON Structure section below).

### Rule 4: Full Responsive Configuration
Every section, column, and widget must include `_responsive_settings` or device-specific overrides for desktop, tablet, and mobile. No horizontal overflow allowed on any breakpoint.

### Rule 5: Color Hierarchy
Apply the user's primary color (Ana Renk) strategically:
- Buttons: background color
- Icons and accent elements: icon color
- Highlight backgrounds: section overlays or accent bars
- Headings or links: only if the reference uses colored headings

Do NOT flood every element with the primary color. Follow the reference's color distribution pattern.

### Rule 6: Clean & Isolated
The template must not depend on external plugins beyond Elementor (Free or Pro). Use only native Elementor widgets. Do not include custom CSS that could break the rest of the site.

## JSON Structure Reference

### Top-Level Wrapper

```json
{
  "title": "Page Title",
  "type": "page",
  "version": "0.4",
  "page_settings": {
    "hide_title": "yes",
    "template": "elementor_canvas"
  },
  "content": [
    // Array of section elements
  ]
}
```

### Section Element

```json
{
  "id": "unique_8char_hex",
  "elType": "section",
  "settings": {
    "layout": "boxed",
    "content_width": {
      "size": 1140,
      "unit": "px"
    },
    "gap": "default",
    "padding": {
      "unit": "px",
      "top": "80",
      "right": "0",
      "bottom": "80",
      "left": "0",
      "isLinked": false
    },
    "padding_tablet": {
      "unit": "px",
      "top": "60",
      "right": "20",
      "bottom": "60",
      "left": "20",
      "isLinked": false
    },
    "padding_mobile": {
      "unit": "px",
      "top": "40",
      "right": "16",
      "bottom": "40",
      "left": "16",
      "isLinked": false
    },
    "background_background": "classic",
    "background_color": "#FFFFFF"
  },
  "elements": [
    // Array of column elements
  ],
  "isInner": false
}
```

### Column Element

```json
{
  "id": "unique_8char_hex",
  "elType": "column",
  "settings": {
    "_column_size": 50,
    "_inline_size": 50,
    "_inline_size_tablet": 100,
    "_inline_size_mobile": 100,
    "padding": {
      "unit": "px",
      "top": "0",
      "right": "15",
      "bottom": "0",
      "left": "15",
      "isLinked": false
    }
  },
  "elements": [
    // Array of widget elements
  ],
  "isInner": false
}
```

Column size rules:
- Full width: `_column_size: 100`, `_inline_size: 100`
- Two equal columns: `_column_size: 50`, `_inline_size: 50`
- Three equal columns: `_column_size: 33`, `_inline_size: 33.33`
- 2/3 + 1/3: `_column_size: 66` + `_column_size: 33`
- On tablet and mobile, most columns should become `_inline_size_tablet: 100` (full width stack)

### Widget Elements

#### Heading Widget
```json
{
  "id": "unique_8char_hex",
  "elType": "widget",
  "widgetType": "heading",
  "settings": {
    "title": "Exact User-Provided Heading",
    "header_size": "h2",
    "align": "left",
    "align_tablet": "center",
    "align_mobile": "center",
    "title_color": "#222222",
    "typography_typography": "custom",
    "typography_font_family": "Poppins",
    "typography_font_size": {
      "unit": "px",
      "size": 36
    },
    "typography_font_size_tablet": {
      "unit": "px",
      "size": 28
    },
    "typography_font_size_mobile": {
      "unit": "px",
      "size": 24
    },
    "typography_font_weight": "700",
    "typography_line_height": {
      "unit": "em",
      "size": 1.3
    }
  },
  "elements": []
}
```

#### Text Editor Widget
```json
{
  "id": "unique_8char_hex",
  "elType": "widget",
  "widgetType": "text-editor",
  "settings": {
    "editor": "<p>Exact user-provided paragraph text</p>",
    "align": "left",
    "align_tablet": "center",
    "align_mobile": "center",
    "text_color": "#555555",
    "typography_typography": "custom",
    "typography_font_family": "Open Sans",
    "typography_font_size": {
      "unit": "px",
      "size": 16
    },
    "typography_font_size_tablet": {
      "unit": "px",
      "size": 15
    },
    "typography_font_size_mobile": {
      "unit": "px",
      "size": 14
    },
    "typography_line_height": {
      "unit": "em",
      "size": 1.7
    }
  },
  "elements": []
}
```

#### Button Widget
```json
{
  "id": "unique_8char_hex",
  "elType": "widget",
  "widgetType": "button",
  "settings": {
    "text": "User-Provided Button Text",
    "link": {
      "url": "#",
      "is_external": false,
      "nofollow": false
    },
    "align": "left",
    "size": "md",
    "button_type": "default",
    "background_color": "#PRIMARY_COLOR",
    "button_text_color": "#FFFFFF",
    "border_radius": {
      "unit": "px",
      "top": "6",
      "right": "6",
      "bottom": "6",
      "left": "6",
      "isLinked": true
    },
    "typography_typography": "custom",
    "typography_font_family": "Poppins",
    "typography_font_size": {
      "unit": "px",
      "size": 16
    },
    "typography_font_weight": "600",
    "button_hover_color": "#FFFFFF",
    "button_hover_background_color": "#DARKER_PRIMARY"
  },
  "elements": []
}
```

#### Image Widget
```json
{
  "id": "unique_8char_hex",
  "elType": "widget",
  "widgetType": "image",
  "settings": {
    "image": {
      "url": "https://placeholder.co/800x500",
      "id": ""
    },
    "image_size": "full",
    "align": "center",
    "width": {
      "unit": "%",
      "size": 100
    },
    "border_radius": {
      "unit": "px",
      "top": "8",
      "right": "8",
      "bottom": "8",
      "left": "8",
      "isLinked": true
    }
  },
  "elements": []
}
```

#### Spacer Widget
```json
{
  "id": "unique_8char_hex",
  "elType": "widget",
  "widgetType": "spacer",
  "settings": {
    "space": {
      "unit": "px",
      "size": 30
    },
    "space_tablet": {
      "unit": "px",
      "size": 20
    },
    "space_mobile": {
      "unit": "px",
      "size": 15
    }
  },
  "elements": []
}
```

#### Divider Widget
```json
{
  "id": "unique_8char_hex",
  "elType": "widget",
  "widgetType": "divider",
  "settings": {
    "style": "solid",
    "weight": {
      "unit": "px",
      "size": 3
    },
    "width": {
      "unit": "%",
      "size": 15
    },
    "color": "#PRIMARY_COLOR",
    "align": "left",
    "gap": {
      "unit": "px",
      "size": 20
    }
  },
  "elements": []
}
```

#### Icon Box Widget
```json
{
  "id": "unique_8char_hex",
  "elType": "widget",
  "widgetType": "icon-box",
  "settings": {
    "selected_icon": {
      "value": "fas fa-check",
      "library": "fa-solid"
    },
    "title_text": "User-Provided Title",
    "description_text": "User-provided description",
    "icon_color": "#PRIMARY_COLOR",
    "title_color": "#222222",
    "description_color": "#555555",
    "title_typography_typography": "custom",
    "title_typography_font_family": "Poppins",
    "title_typography_font_size": {
      "unit": "px",
      "size": 18
    },
    "title_typography_font_weight": "600"
  },
  "elements": []
}
```

## ID Generation

Every `id` field must be a unique 7-8 character lowercase hexadecimal string. Generate them randomly for each element. Example: `"a1b2c3d"`, `"f4e5d6c"`. No two elements in the template should share the same ID.

## Step-by-Step Workflow

### Step 1: Fetch & Analyze Reference
Use `web_fetch` to load the reference URL. Analyze:
- Overall page structure (number of sections, their purpose)
- Grid system (column ratios per section)
- Spacing rhythm (padding between sections, gaps between elements)
- Typography hierarchy (heading sizes, body text size, font families)
- Color usage pattern (where the accent color appears)
- Component patterns (cards, icon boxes, CTAs, hero layouts)

Document your findings as internal notes before generating.

### Step 2: Map User Content to Sections
Take the user's numbered content sections and map each one to a corresponding section type from the reference. Determine:
- Which section layout pattern to use for each content block
- Column structure for each section
- Which widgets are needed (heading, text-editor, button, image, icon-box, etc.)
- How the content flows within each section

### Step 3: Generate the JSON
Build the complete JSON following the structure reference above. For each section:
1. Create the section element with appropriate padding and background
2. Create columns matching the reference's grid ratios
3. Insert widgets with the user's exact text content
4. Apply the primary color according to the reference's accent pattern
5. Set responsive overrides for tablet and mobile

### Step 4: Validate
Before outputting, check:
- [ ] Every element has a unique `id`
- [ ] No text exists that the user did not provide
- [ ] Column `_column_size` values in each section sum correctly
- [ ] Responsive padding/margin/font-size set for all three breakpoints
- [ ] Primary color applied only to accent elements (buttons, icons, dividers)
- [ ] JSON is valid and parseable
- [ ] Widget types are all native Elementor (no third-party dependencies)

### Step 5: Output
Write the JSON to `/mnt/user-data/outputs/elementor-template.json` and present it to the user via `present_files`. Output ONLY the JSON file — no explanatory prose, no conversation, no commentary after delivering the file.

## Common Page Type Patterns

### Landing Page
- Hero section: full-width background, centered heading + subtext + CTA button
- Features/services: 3 or 4 column grid with icon boxes
- About/intro: 2-column (text + image)
- Testimonials: cards in grid or single column
- CTA section: colored background, centered text + button

### Service Page (Hizmet Sayfası)
- Hero: section title + brief description
- Service detail sections: alternating 2-column (image left/text right, then swap)
- Benefits: icon box grid
- CTA: bottom call-to-action

### Contact Page (İletişim)
- Hero: page title
- 2-column: contact info + map or form placeholder
- Address/phone/email as icon boxes

### About Page (Hakkımızda)
- Hero: company tagline
- Story section: 2-column text + image
- Team section: 3-4 column grid with image + name + role
- Values/mission: icon box grid

## Typography Defaults

If the reference site's fonts cannot be determined, use these sensible defaults:
- Headings: `Poppins`, weight 700
- Body: `Open Sans`, weight 400
- Button text: `Poppins`, weight 600

Font size scale (desktop / tablet / mobile):
- H1: 42 / 34 / 28
- H2: 36 / 28 / 24
- H3: 24 / 20 / 18
- Body: 16 / 15 / 14
- Small text: 14 / 13 / 13

## Spacing Defaults

If the reference's exact spacing cannot be determined:
- Section vertical padding: 80px / 60px / 40px (desktop / tablet / mobile)
- Column gap: 15px padding each side
- Between widgets (spacer): 30px / 20px / 15px
- Section horizontal padding on mobile: 16px

## Color Utility

When the user provides a primary HEX color, derive these variants:
- **Primary**: as given (buttons, icons, accent elements)
- **Primary Dark**: 15% darker (button hover states)
- **Primary Light/10%**: 10% opacity version (background tints for accent sections)
- **Text Dark**: `#222222` (headings)
- **Text Body**: `#555555` (paragraphs)
- **Background Light**: `#F8F9FA` (alternating section backgrounds)
- **White**: `#FFFFFF` (default section backgrounds)

## Error Prevention

- If the reference URL is unreachable, inform the user and ask for an alternative or proceed with the page type's default pattern
- If user content sections don't clearly map to a structure, ask for clarification before generating
- If the user requests a widget or feature that requires Elementor Pro, note this in a JSON comment or inform the user — do not use widgets that won't work in the free version without warning
- Always validate the JSON is syntactically correct before outputting

## Final Output Checklist

Run through before delivering:

- [ ] Valid JSON (parseable, no trailing commas, no comments)
- [ ] Template importable via Elementor > Templates > Import Templates
- [ ] All IDs unique
- [ ] Zero invented text
- [ ] Responsive values for all three breakpoints
- [ ] Primary color applied with hierarchy discipline
- [ ] Section structure mirrors reference layout
- [ ] No external plugin dependencies
- [ ] File written to `/mnt/user-data/outputs/elementor-template.json`
