---
name: wp-embeddable-html
description: >
  Generate WordPress-embeddable, fully isolated single-file HTML code from a reference design
  (ZIP containing HTML/CSS/JS/images). Use this skill whenever a user uploads a ZIP file of a
  website and wants a new page coded in the same design language — specifically for embedding
  inside a WordPress content area (HTML block). Also trigger when the user mentions 'WordPress
  embed', 'WordPress HTML block', 'isolated HTML for WordPress', 'WP içerik alanı', 'tek parça
  kod', or asks to replicate/adapt a site design for WordPress insertion. Trigger even if the
  user just says 'make this design WordPress-compatible' or 'embed this in WordPress'. This skill
  handles CSS scoping, JS isolation via IIFE, removal of global tags, and content sectioning —
  all critical for WordPress compatibility.
---

# WordPress-Embeddable Isolated HTML Generator

Generate a single, self-contained HTML snippet from a reference website ZIP — fully isolated and
ready to paste into a WordPress HTML block without breaking the theme.

---

## Table of Contents

1. [When This Skill Triggers](#when-this-skill-triggers)
2. [Step-by-Step Workflow](#step-by-step-workflow)
3. [WordPress Isolation Rules (CRITICAL)](#wordpress-isolation-rules-critical)
4. [Design Fidelity Guidelines](#design-fidelity-guidelines)
5. [Content Insertion Protocol](#content-insertion-protocol)
6. [Output Structure Template](#output-structure-template)
7. [Advanced Techniques](#advanced-techniques)
8. [Quality Checklist](#quality-checklist)
9. [Common Mistakes & Fixes](#common-mistakes--fixes)
10. [Final Output Protocol](#final-output-protocol)

---

## When This Skill Triggers

- User uploads a ZIP containing a website (index.html + CSS/JS/images)
- User wants a new page coded in the same visual style
- Output must be embeddable inside WordPress (HTML block / Custom HTML widget)
- User explicitly mentions WordPress embedding, content area insertion, or theme isolation
- Keywords: "WordPress embed", "WP HTML block", "tek parça kod", "içerik alanı", "izole HTML"

**IMPORTANT:** This skill is about generating NEW content pages that MATCH the design language
of the uploaded reference — it is NOT about converting the reference file itself into WordPress.

---

## Step-by-Step Workflow

### Phase 1: Extract & Analyze the ZIP

```bash
# Create workspace
mkdir -p /home/claude/wp-work
cp /mnt/user-data/uploads/*.zip /home/claude/wp-work/
cd /home/claude/wp-work

# Extract
unzip -o *.zip -d extracted/

# List full structure
find extracted/ -type f | head -80
```

Examine EVERY file type present:

| File Type | What to Extract |
|-----------|----------------|
| `index.html` (and other .html) | DOM structure, section layout, class naming conventions, component patterns, semantic hierarchy |
| `.css` files | Color palette, font stacks, spacing system, grid/flexbox patterns, animations, hover states, shadows, border-radius, responsive breakpoints |
| `.js` files | Interactive behaviors (sliders, accordions, tabs, scroll effects, counters, modals, lazy loading) |
| Images (`.png`, `.jpg`, `.svg`, `.webp`) | Hero banners, icons, background patterns, decorative elements — note dimensions and usage context |
| Font files (`.woff`, `.woff2`, `.ttf`) | Custom fonts not on Google Fonts — will need base64 embedding or external URL |

**Read EVERY CSS and JS file thoroughly.** Do not skim. The design fidelity depends entirely on
understanding every visual detail.

### Phase 2: Build a Design Token Map

Before writing ANY code, document these tokens explicitly. This is non-negotiable:

```
═══════════════════════════════════════════════
DESIGN TOKENS EXTRACTED FROM REFERENCE
═══════════════════════════════════════════════

COLOR PALETTE:
  Primary:          #______
  Secondary:        #______
  Accent:           #______
  Text Primary:     #______
  Text Secondary:   #______
  Text Muted:       #______
  Background:       #ffffff  (forced per spec)
  Surface/Card BG:  #______
  Border Color:     #______
  Success:          #______
  Warning:          #______
  Error:            #______

TYPOGRAPHY:
  Font Heading:     '________', ________
  Font Body:        '________', ________
  Font Accent/UI:   '________', ________ (if distinct)
  H1 Size:          __px  |  Weight: __  |  Line-Height: __
  H2 Size:          __px  |  Weight: __  |  Line-Height: __
  H3 Size:          __px  |  Weight: __  |  Line-Height: __
  H4 Size:          __px  |  Weight: __  |  Line-Height: __
  Body Size:        __px  |  Weight: __  |  Line-Height: __
  Small Text:       __px  |  Weight: __  |  Line-Height: __
  Letter Spacing:   __px or __em (if any)

SPACING:
  Section Padding (Desktop):   __px top / __px bottom
  Section Padding (Tablet):    __px top / __px bottom
  Section Padding (Mobile):    __px top / __px bottom
  Content Gap (grid/flex):     __px
  Card Internal Padding:       __px
  Element Margin Bottom:       __px

LAYOUT:
  Grid System:       __ columns  |  Gap: __px
  Container Padding: __px (desktop) / __px (mobile)
  Max Width:         1280px (forced per spec)

DECORATIVE:
  Border Radius:    __px (cards) / __px (buttons) / __px (images)
  Box Shadow:       ______________________________
  Hover Shadow:     ______________________________
  Divider Style:    ______________________________
  Accent Line:      ______________________________

ANIMATION:
  Transition:       ______________________________
  Hover Effects:    ______________________________
  Scroll Animations: ______________________________

RESPONSIVE BREAKPOINTS:
  Desktop:          > ____px
  Tablet:           ____px — ____px
  Mobile:           < ____px
  Small Mobile:     < ____px
═══════════════════════════════════════════════
```

### Phase 3: Generate the Isolated HTML

Follow the **WordPress Isolation Rules** below EXACTLY. Every rule is mandatory.

Write the output as a single `.html` file. Build iteratively for complex designs (>400 lines):

1. **First pass:** HTML structure with semantic sections
2. **Second pass:** Complete CSS with all tokens applied
3. **Third pass:** Responsive breakpoints
4. **Fourth pass:** JavaScript interactions
5. **Final pass:** Review against checklist

---

## WordPress Isolation Rules (CRITICAL)

These rules are **non-negotiable**. Violating ANY rule WILL break the WordPress site.

### Rule 1: No Root Tags — ABSOLUTE BAN

```
FORBIDDEN — NEVER output these:
  <!DOCTYPE html>
  <html>
  <head>
  <body>
  <meta>
  <title>
  <link rel="stylesheet">  (use @import inside <style> instead)
```

The output starts DIRECTLY with the wrapper div:
```html
<div id="ozel-tasarim-alani-XXXX">
```

Where `XXXX` is a **unique random 4-digit number** (e.g., `ozel-tasarim-alani-7429`).
This prevents ID collisions if multiple embeds exist on the same WordPress page.

### Rule 2: CSS Scoping — EVERY SINGLE RULE

ALL CSS selectors MUST begin with `#ozel-tasarim-alani-XXXX`. Zero exceptions.

```css
/* ═══ WRONG — These WILL bleed into the WordPress theme ═══ */
h1 { font-size: 36px; }
.card { padding: 20px; }
* { box-sizing: border-box; }
a { color: blue; }
img { max-width: 100%; }
p { margin-bottom: 1em; }
ul { list-style: disc; }

/* ═══ CORRECT — Scoped to our container only ═══ */
#ozel-tasarim-alani-XXXX h1 { font-size: 36px; }
#ozel-tasarim-alani-XXXX .card { padding: 20px; }
#ozel-tasarim-alani-XXXX *,
#ozel-tasarim-alani-XXXX *::before,
#ozel-tasarim-alani-XXXX *::after { box-sizing: border-box; }
#ozel-tasarim-alani-XXXX a { color: blue; }
#ozel-tasarim-alani-XXXX img { max-width: 100%; }
#ozel-tasarim-alani-XXXX p { margin-bottom: 1em; }
#ozel-tasarim-alani-XXXX ul { list-style: disc; }
```

**Additional CSS Scoping Requirements:**

```css
/* CSS Custom Properties — scope to wrapper, NOT :root */
#ozel-tasarim-alani-XXXX {
  --ozel-primary: #2563eb;
  --ozel-secondary: #1e40af;
  --ozel-accent: #f59e0b;
  /* prefix variable names with 'ozel-' to avoid theme collision */
}

/* @keyframes — prefix animation names */
@keyframes ozelFadeIn { from { opacity: 0; } to { opacity: 1; } }
@keyframes ozelSlideUp { from { transform: translateY(30px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }

/* Pseudo-elements — still need scoping */
#ozel-tasarim-alani-XXXX .divider::after { content: ''; ... }

/* Specificity boost against aggressive themes */
#ozel-tasarim-alani-XXXX h2.section-title { ... }
/* If theme still overrides, use: */
div#ozel-tasarim-alani-XXXX h2.section-title { ... }
```

**Google Fonts:**
```css
<style>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Open+Sans:wght@400;600&display=swap');

  /* Font applied ONLY within our scope */
  #ozel-tasarim-alani-XXXX {
    font-family: 'Open Sans', sans-serif;
  }
  #ozel-tasarim-alani-XXXX h1,
  #ozel-tasarim-alani-XXXX h2,
  #ozel-tasarim-alani-XXXX h3 {
    font-family: 'Montserrat', sans-serif;
  }
</style>
```

### Rule 3: JS Isolation — IIFE Wrapping (Mandatory)

ALL JavaScript MUST be wrapped in an IIFE:

```html
<script>
(function() {
  'use strict';

  // ── Configuration ──
  var ROOT_ID = 'ozel-tasarim-alani-XXXX';
  var root = document.getElementById(ROOT_ID);
  if (!root) return;  // Safety: exit if container not found

  // ── DOM Queries — ALWAYS scope to root ──
  // CORRECT:
  var buttons = root.querySelectorAll('.btn');
  var heroSection = root.querySelector('.hero');

  // WRONG — NEVER do this:
  // var buttons = document.querySelectorAll('.btn');  // Selects ALL .btn on page!
  // var el = document.getElementById('some-id');      // Escapes our scope!

  // ── Event Listeners ──
  buttons.forEach(function(btn) {
    btn.addEventListener('click', function(e) {
      // handle click
    });
  });

  // ── Scroll/Resize — scope awareness ──
  function handleScroll() {
    var rect = root.getBoundingClientRect();
    if (rect.top > window.innerHeight || rect.bottom < 0) return;
    // Only execute when our container is visible
  }
  window.addEventListener('scroll', handleScroll, { passive: true });

  // ── Intersection Observer (preferred for scroll animations) ──
  if ('IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('ozel-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -50px 0px' });

    root.querySelectorAll('.ozel-animate').forEach(function(el) {
      observer.observe(el);
    });
  }

})();
</script>
```

**JS Hard Rules:**
- **No `var`, `let`, `const` in global scope** — everything inside IIFE
- **No `document.querySelector`** for internal elements — use `root.querySelector`
- **No `window.onload = ...`** — use `addEventListener` if needed
- **No `window.$` or global jQuery** — if jQuery needed, use `jQuery.noConflict()` inside IIFE
- **No `setTimeout`/`setInterval` that reference global** — capture references inside IIFE
- **No inline event handlers** in HTML (e.g., `onclick="..."`). Bind from JS instead.

### Rule 4: No Header / No Footer

The output MUST NOT include:
- ❌ Navigation bars / header menus
- ❌ Top bars (announcement bars, language selectors)
- ❌ Footer sections (sitemap, copyright, contact rows)
- ❌ "Back to top" floating buttons
- ❌ Fixed/sticky position elements (`position: fixed` escapes the container!)
- ❌ Cookie consent banners
- ❌ Chat widgets or floating buttons

Only **content sections** are generated.

### Rule 5: Container Specification

```css
#ozel-tasarim-alani-XXXX {
  max-width: 1280px;
  width: 100%;
  margin: 0 auto;
  padding: 0;
  background-color: #ffffff;
  box-sizing: border-box;
  overflow: hidden;           /* Prevent horizontal scroll bleed */
  position: relative;         /* Contain absolutely positioned children */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
```

### Rule 6: Image Handling Strategy

Since this code will be pasted into WordPress, images require special handling:

| Scenario | Strategy |
|----------|----------|
| Small icons/logos < 30KB | Base64 inline: `src="data:image/svg+xml;base64,..."` |
| Decorative patterns | CSS gradients, SVG inline, or CSS patterns |
| Hero/banner images | Placeholder with instruction comment |
| Content images | Placeholder with instruction comment |

**Placeholder format:**
```html
<img
  src="https://placehold.co/800x400/HEXCOLOR/TEXTCOLOR?text=Gorsel+Buraya"
  alt="Açıklayıcı alt metin"
  class="hero-img"
  loading="lazy"
>
<!-- WP-MEDIA-INSTRUCTION: Bu görseli WordPress Medya Kütüphanesi'ne yükleyip
     src değerini güncelleyin. Önerilen boyut: 800x400px -->
```

**SVG Icons — Inline preferred:**
```html
<svg class="icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
  <path d="M..."/>
</svg>
```

### Rule 7: Responsive Design (Scoped)

Three mandatory breakpoints, all scoped:

```css
/* ── Tablet ── */
@media (max-width: 1024px) {
  #ozel-tasarim-alani-XXXX .grid-3 {
    grid-template-columns: 1fr 1fr;
  }
  #ozel-tasarim-alani-XXXX .section {
    padding: 60px 24px;
  }
}

/* ── Mobile ── */
@media (max-width: 768px) {
  #ozel-tasarim-alani-XXXX {
    padding: 0 16px;
  }
  #ozel-tasarim-alani-XXXX .grid-3,
  #ozel-tasarim-alani-XXXX .grid-2 {
    grid-template-columns: 1fr;
  }
  #ozel-tasarim-alani-XXXX .section {
    padding: 40px 0;
  }
  #ozel-tasarim-alani-XXXX h1 { font-size: 28px; }
  #ozel-tasarim-alani-XXXX h2 { font-size: 24px; }
}

/* ── Small Mobile ── */
@media (max-width: 480px) {
  #ozel-tasarim-alani-XXXX {
    padding: 0 12px;
  }
  #ozel-tasarim-alani-XXXX h1 { font-size: 24px; }
  #ozel-tasarim-alani-XXXX h2 { font-size: 20px; }
}
```

---

## Design Fidelity Guidelines

The generated code must be **visually indistinguishable** from the reference design in:

### Color & Palette
- Extract EXACT hex values from the reference CSS
- Map every usage: backgrounds, text, borders, buttons, hover states, shadows
- Do not approximate — use the exact values

### Typography
- Match font family, weight, size, line-height, letter-spacing for EVERY text level
- If the reference uses a custom font not on Google Fonts, note it in a comment
- Preserve text transform (uppercase, capitalize) where used

### Spacing & Rhythm
- Match section padding precisely
- Match element margins and gaps
- Preserve the vertical rhythm between headings, paragraphs, and components
- Match card/component internal padding

### Component Patterns
- Replicate card designs exactly (shadows, borders, radius, hover states)
- Replicate button styles (padding, radius, background, hover transition)
- Replicate list/grid layouts (columns, gaps, alignment)
- Replicate dividers, accent lines, decorative elements

### Visual Effects
- Match box-shadow values exactly
- Match transition/animation timing and easing
- Match gradient definitions
- Match overlay/opacity effects
- Match hover states and interactive feedback

---

## Content Insertion Protocol

The user provides content as numbered sections. For each section:

1. **Map to a visual section** from the reference design's layout
2. **Apply the reference's heading hierarchy** (h2 for section titles, h3 for sub-sections)
3. **Use the reference's component patterns** (cards, grids, lists, feature blocks)
4. **Maintain the reference's decorative elements** (accent lines, icons, dividers)

### Section Mapping Strategy

```
User Content          →  Visual Treatment
─────────────────────────────────────────────
1. Bölüm (Main/Hero)  →  Full-width prominent section with large heading
2. Bölüm (Features)   →  Card grid or feature list layout
3. Bölüm (Details)    →  Two-column or alternating image-text layout
4. Bölüm (CTA/Closing)→  Highlight box or call-to-action section
```

Adapt the mapping based on the reference design's actual section patterns. If the reference
has a specific style for testimonials, stats, or galleries, use those patterns where the
content fits.

---

## Output Structure Template

```html
<!-- WordPress Embeddable Component — Fully Isolated -->
<div id="ozel-tasarim-alani-XXXX">

<style>
  /* ══════════════════════════════════════════
     Google Fonts Import (if needed)
     ══════════════════════════════════════════ */
  @import url('https://fonts.googleapis.com/css2?family=...&display=swap');

  /* ══════════════════════════════════════════
     CSS Custom Properties (scoped)
     ══════════════════════════════════════════ */
  #ozel-tasarim-alani-XXXX {
    --ozel-primary: #______;
    --ozel-secondary: #______;
    --ozel-accent: #______;
    --ozel-text: #______;
    --ozel-text-light: #______;
    --ozel-bg: #ffffff;
    --ozel-surface: #______;
    --ozel-border: #______;
    --ozel-radius: __px;
    --ozel-shadow: 0 __px __px rgba(0,0,0,0.__);
    --ozel-transition: all 0.3s ease;
  }

  /* ══════════════════════════════════════════
     Base Reset (scoped)
     ══════════════════════════════════════════ */
  #ozel-tasarim-alani-XXXX {
    max-width: 1280px;
    width: 100%;
    margin: 0 auto;
    padding: 0;
    background-color: var(--ozel-bg);
    box-sizing: border-box;
    font-family: '...', sans-serif;
    color: var(--ozel-text);
    line-height: 1.6;
    overflow: hidden;
    position: relative;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  #ozel-tasarim-alani-XXXX *,
  #ozel-tasarim-alani-XXXX *::before,
  #ozel-tasarim-alani-XXXX *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  #ozel-tasarim-alani-XXXX img {
    max-width: 100%;
    height: auto;
    display: block;
  }

  #ozel-tasarim-alani-XXXX a {
    text-decoration: none;
    color: inherit;
  }

  /* ══════════════════════════════════════════
     Typography (scoped)
     ══════════════════════════════════════════ */
  #ozel-tasarim-alani-XXXX h1 { ... }
  #ozel-tasarim-alani-XXXX h2 { ... }
  #ozel-tasarim-alani-XXXX h3 { ... }
  #ozel-tasarim-alani-XXXX h4 { ... }
  #ozel-tasarim-alani-XXXX p  { ... }

  /* ══════════════════════════════════════════
     Section Styles
     ══════════════════════════════════════════ */
  #ozel-tasarim-alani-XXXX .ozel-section { ... }
  #ozel-tasarim-alani-XXXX .ozel-section-1 { ... }
  #ozel-tasarim-alani-XXXX .ozel-section-2 { ... }
  #ozel-tasarim-alani-XXXX .ozel-section-3 { ... }

  /* ══════════════════════════════════════════
     Component Styles
     ══════════════════════════════════════════ */
  #ozel-tasarim-alani-XXXX .ozel-card { ... }
  #ozel-tasarim-alani-XXXX .ozel-btn { ... }
  #ozel-tasarim-alani-XXXX .ozel-grid { ... }

  /* ══════════════════════════════════════════
     Animations (prefixed keyframes)
     ══════════════════════════════════════════ */
  @keyframes ozelFadeIn { ... }
  @keyframes ozelSlideUp { ... }

  #ozel-tasarim-alani-XXXX .ozel-animate {
    opacity: 0;
    transform: translateY(20px);
    transition: opacity 0.6s ease, transform 0.6s ease;
  }
  #ozel-tasarim-alani-XXXX .ozel-visible {
    opacity: 1;
    transform: translateY(0);
  }

  /* ══════════════════════════════════════════
     Responsive — Tablet
     ══════════════════════════════════════════ */
  @media (max-width: 1024px) {
    #ozel-tasarim-alani-XXXX ... { ... }
  }

  /* ══════════════════════════════════════════
     Responsive — Mobile
     ══════════════════════════════════════════ */
  @media (max-width: 768px) {
    #ozel-tasarim-alani-XXXX ... { ... }
  }

  /* ══════════════════════════════════════════
     Responsive — Small Mobile
     ══════════════════════════════════════════ */
  @media (max-width: 480px) {
    #ozel-tasarim-alani-XXXX ... { ... }
  }
</style>

  <!-- ════════ Section 1: [Bölüm Adı] ════════ -->
  <section class="ozel-section ozel-section-1">
    <div class="ozel-container">
      ...
    </div>
  </section>

  <!-- ════════ Section 2: [Bölüm Adı] ════════ -->
  <section class="ozel-section ozel-section-2">
    <div class="ozel-container">
      ...
    </div>
  </section>

  <!-- ════════ Section 3: [Bölüm Adı] ════════ -->
  <section class="ozel-section ozel-section-3">
    <div class="ozel-container">
      ...
    </div>
  </section>

<script>
(function() {
  'use strict';

  var ROOT_ID = 'ozel-tasarim-alani-XXXX';
  var root = document.getElementById(ROOT_ID);
  if (!root) return;

  // ── Scroll Animations (IntersectionObserver) ──
  if ('IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('ozel-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    root.querySelectorAll('.ozel-animate').forEach(function(el) {
      observer.observe(el);
    });
  }

  // ── Additional Interactions ──
  // ... all scoped to root ...

})();
</script>

</div>
<!-- /WordPress Embeddable Component -->
```

---

## Advanced Techniques

### CSS Class Naming Convention

Prefix ALL custom classes with `ozel-` to prevent collision with WordPress theme classes:

```
✅ ozel-hero, ozel-card, ozel-grid, ozel-btn, ozel-section
❌ hero, card, grid, btn, section (common names — WILL collide)
```

### Handling Complex Interactions

**Tabs:**
```javascript
var tabBtns = root.querySelectorAll('.ozel-tab-btn');
var tabPanels = root.querySelectorAll('.ozel-tab-panel');

tabBtns.forEach(function(btn, i) {
  btn.addEventListener('click', function() {
    tabBtns.forEach(function(b) { b.classList.remove('ozel-active'); });
    tabPanels.forEach(function(p) { p.classList.remove('ozel-active'); });
    btn.classList.add('ozel-active');
    tabPanels[i].classList.add('ozel-active');
  });
});
```

**Accordion:**
```javascript
root.querySelectorAll('.ozel-accordion-header').forEach(function(header) {
  header.addEventListener('click', function() {
    var item = this.parentElement;
    var isOpen = item.classList.contains('ozel-open');

    // Close all others (optional)
    root.querySelectorAll('.ozel-accordion-item').forEach(function(el) {
      el.classList.remove('ozel-open');
    });

    if (!isOpen) item.classList.add('ozel-open');
  });
});
```

**Counter Animation:**
```javascript
function animateCounters() {
  root.querySelectorAll('.ozel-counter').forEach(function(counter) {
    var target = parseInt(counter.getAttribute('data-target'), 10);
    var duration = 2000;
    var start = 0;
    var startTime = null;

    function step(timestamp) {
      if (!startTime) startTime = timestamp;
      var progress = Math.min((timestamp - startTime) / duration, 1);
      counter.textContent = Math.floor(progress * target);
      if (progress < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  });
}
```

### Handling WordPress Theme Interference

If the WordPress theme is known to be aggressive with global styles:

```css
/* Nuclear reset for the container */
#ozel-tasarim-alani-XXXX,
#ozel-tasarim-alani-XXXX * {
  all: unset;
  display: revert;
  box-sizing: border-box;
}

/* Then reapply your styles with high specificity */
div#ozel-tasarim-alani-XXXX { ... }
div#ozel-tasarim-alani-XXXX p { ... }
```

⚠️ Use the nuclear reset ONLY when explicitly asked or when the user reports theme conflicts.

### External Libraries (Use Sparingly)

If the reference design uses a library (Swiper, AOS, etc.):

```html
<script>
(function() {
  'use strict';
  var ROOT_ID = 'ozel-tasarim-alani-XXXX';
  var root = document.getElementById(ROOT_ID);
  if (!root) return;

  // Check if library already loaded (WordPress might have it)
  if (typeof Swiper === 'undefined') {
    var script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js';
    script.onload = initSlider;
    document.head.appendChild(script);

    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css';
    document.head.appendChild(link);
  } else {
    initSlider();
  }

  function initSlider() {
    new Swiper(root.querySelector('.ozel-swiper'), {
      slidesPerView: 1,
      spaceBetween: 30,
      pagination: { el: root.querySelector('.ozel-swiper-pagination') },
      navigation: {
        nextEl: root.querySelector('.ozel-swiper-next'),
        prevEl: root.querySelector('.ozel-swiper-prev')
      }
    });
  }
})();
</script>
```

---

## Quality Checklist (Verify EVERY Item Before Output)

### Isolation Checks (CRITICAL — any failure = broken WordPress)

- [ ] ❌ No `<!DOCTYPE>`, `<html>`, `<head>`, `<body>`, `<meta>`, `<title>` tags
- [ ] ✅ Output starts with `<div id="ozel-tasarim-alani-XXXX">`
- [ ] ✅ Unique numeric suffix on wrapper ID
- [ ] ✅ EVERY CSS rule prefixed with `#ozel-tasarim-alani-XXXX`
- [ ] ✅ No bare element selectors (`h1 {}`, `p {}`, `a {}`, `img {}`, `div {}`)
- [ ] ✅ No `:root` CSS variable declarations (use wrapper ID instead)
- [ ] ✅ All `@keyframes` names prefixed with `ozel`
- [ ] ✅ All CSS custom properties prefixed with `--ozel-`
- [ ] ✅ All CSS class names prefixed with `ozel-`
- [ ] ✅ JS wrapped in IIFE `(function() { ... })();`
- [ ] ✅ JS uses `root.querySelector` NOT `document.querySelector` for internals
- [ ] ✅ No global JS variables or functions
- [ ] ✅ No inline event handlers (onclick, onmouseover, etc.)
- [ ] ✅ No `position: fixed` anywhere
- [ ] ✅ No header/nav/footer elements

### Container Checks

- [ ] ✅ `max-width: 1280px`
- [ ] ✅ `width: 100%`
- [ ] ✅ `margin: 0 auto`
- [ ] ✅ `background-color: #ffffff`
- [ ] ✅ `box-sizing: border-box`
- [ ] ✅ `overflow: hidden` (or `overflow-x: hidden` minimum)

### Design Fidelity Checks

- [ ] ✅ Color palette matches reference exactly
- [ ] ✅ Fonts match reference (with Google Fonts import if needed)
- [ ] ✅ Font sizes, weights, line-heights match per level
- [ ] ✅ Spacing/padding matches reference rhythm
- [ ] ✅ Card/component styles replicated (shadows, borders, radius)
- [ ] ✅ Button styles replicated (padding, colors, hover states)
- [ ] ✅ Hover/transition effects present
- [ ] ✅ Visual hierarchy preserved

### Responsive Checks

- [ ] ✅ Breakpoints at 1024px, 768px, and 480px (minimum)
- [ ] ✅ All breakpoint rules scoped with wrapper ID
- [ ] ✅ Grid/flex layouts collapse properly on mobile
- [ ] ✅ Font sizes reduce appropriately on mobile
- [ ] ✅ Images are responsive (`max-width: 100%; height: auto;`)
- [ ] ✅ No horizontal scroll on mobile

### Content Checks

- [ ] ✅ All user-provided section content inserted in correct order
- [ ] ✅ Section content wrapped in appropriate visual containers
- [ ] ✅ No header/footer content included
- [ ] ✅ Images have placeholder comments with upload instructions
- [ ] ✅ Alt text on all images

---

## Common Mistakes & Fixes

| # | Mistake | Fix |
|---|---------|-----|
| 1 | `:root { --color: ... }` | Use `#ozel-tasarim-alani-XXXX { --ozel-color: ... }` |
| 2 | `position: fixed` on any element | Use `position: sticky` or `absolute` within `relative` parent |
| 3 | Bare `.card { }` selector | Always `#ozel-tasarim-alani-XXXX .ozel-card { }` |
| 4 | `document.getElementById('hero')` | `root.querySelector('.ozel-hero')` |
| 5 | Global `$` or `jQuery` usage | Wrap in IIFE, check existence: `if (typeof jQuery !== 'undefined')` |
| 6 | `@keyframes fadeIn` | `@keyframes ozelFadeIn` |
| 7 | `<script src="external.js">` | Load dynamically inside IIFE with existence check |
| 8 | `onclick="doSomething()"` | Bind via `addEventListener` inside IIFE |
| 9 | Forgetting responsive scoping | Every `@media` rule must include `#ozel-tasarim-alani-XXXX` prefix |
| 10 | Using common class names (`.container`, `.row`, `.btn`) | Prefix: `.ozel-container`, `.ozel-row`, `.ozel-btn` |
| 11 | `<link rel="stylesheet" href="...">` | Use `@import url(...)` inside `<style>` |
| 12 | IDs inside sections (`id="hero"`) | Prefix: `id="ozel-hero"` or better, use classes |
| 13 | `z-index: 9999` on elements | Keep z-index values reasonable (1-100) within container |
| 14 | `100vh` heights | Use `min-height` values in px/rem — `100vh` can cause issues in WP |

---

## Final Output Protocol

1. Write the complete code to `/mnt/user-data/outputs/wordpress-embed.html`
2. Use `present_files` to share with the user
3. Do NOT add explanatory prose — the user wants copy-paste-ready code ONLY
4. If the design is complex (>500 lines), build iteratively in `/home/claude/wp-work/` and copy final to outputs
5. File name can be customized if the user specifies one, otherwise default to `wordpress-embed.html`

**REMEMBER:** The user will literally copy-paste this code into a WordPress HTML block.
It MUST work perfectly on first paste with zero modifications (except image URLs).
