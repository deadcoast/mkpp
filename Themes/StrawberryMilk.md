# StrawberryMilk Theme Palette

## StrawberryMilk Ver 001 - Notepad++ Theme Colors

```css
:root {
    /* BACKGROUND COLORS */
    --bg-primary: #120A14;        /* Main background (Global override, Default Style) */
    --bg-secondary: #1C1420;      /* Secondary background (Current line, tabs) */
    --bg-surface: #1f181e;        /* Surface elements (Selected text, margins) */
    --bg-surface-alt: #3D2F42;    /* Alternative surface (Multi-selected text) */

    /* TEXT COLORS */
    --text-primary: #E8C5D5;      /* Primary text (Default, operators) */
    --text-secondary: #FFB3D1;    /* Secondary text (Keywords, functions) */
    --text-muted: #D9B8C4;        /* Muted text (Comments, whitespace) */

    /* ACCENT COLORS */
    --accent-primary: #FF8DBD;    /* Primary accent (Keywords, syntax) */
    --accent-secondary: #FF6BA8;  /* Secondary accent (Numbers, errors) */
    --accent-light: #FFD6E8;      /* Light accent (Strings, literals) */

    /* UI ELEMENTS */
    --border-color: rgba(255, 179, 209, 0.2);  /* Border transparency */
    --shadow: 0 20px 60px rgba(0, 0, 0, 0.4); /* Shadow effects */

    /* GRADIENTS */
    --gradient-primary: linear-gradient(135deg, #FF6BA8 0%, #FF8DBD 50%, #FFB3D1 100%);
    --gradient-bg: linear-gradient(145deg, #1A0F1D 0%, #241724 25%, #2A1B2E 50%, #241724 75%, #1A0F1D 100%);
}
```

## StrawberryMilk Ver 002 - Notepad++ Theme Colors

```css
:root {
    /* BACKGROUND COLORS */
    --bg-primary: #141415;        /* Main background (Global override, Default Style) */
    --bg-secondary: #161619;      /* Secondary background (Current line, tabs) */
    --bg-surface: #18181c;        /* Surface elements (Selected text, margins) */
    --bg-surface-alt: #1c181c;    /* Alternative surface (Multi-selected text) */

    /* TEXT COLORS */
    --text-primary: #E8C5D5;      /* Primary text (Default, operators) */
    --text-secondary: #FFB3D1;    /* Secondary text (Keywords, functions) */
    --text-muted: #BB889F;        /* Muted text (Comments, whitespace) */

    /* ACCENT COLORS */
    --accent-primary: #FF8DBD;    /* Primary accent (Keywords, syntax) */
    --accent-secondary: #FF6BA8;  /* Secondary accent (Numbers, errors) */
    --accent-light: #FFD6E8;      /* Light accent (Strings, literals) */

    /* UI ELEMENTS */
    --border-color: rgba(255, 179, 209, 0.2);  /* Border transparency */
    --shadow: 0 20px 60px rgba(0, 0, 0, 0.4); /* Shadow effects */

    /* GRADIENTS */
    --gradient-primary: linear-gradient(135deg, #FF6BA8 0%, #FF8DBD 50%, #FFB3D1 100%);
    --gradient-bg: linear-gradient(145deg, #1A0F1D 0%, #241724 25%, #2A1B2E 50%, #241724 75%, #1A0F1D 100%);
}
```

## Notepad++ Theme Mapping Guide

### Background Colors (bgColor)

- `--bg-primary` → Main editor background
- `--bg-secondary` → Current line background, tab background
- `--bg-surface` → Selected text background, margins
- `--bg-surface-alt` → Multi-selected text background

### Text Colors (fgColor)

- `--text-primary` → Default text, operators, identifiers
- `--text-secondary` → Keywords, function names, important syntax
- `--text-muted` → Comments, documentation, whitespace symbols

### Accent Colors (fgColor)

- `--accent-primary` → Keywords, preprocessor directives, types
- `--accent-secondary` → Numbers, errors, line numbers
- `--accent-light` → Strings, character literals, regex

### Usage Examples

```xml
<!-- Main background -->
<WidgetStyle name="Default Style" bgColor="120A14" fgColor="FFB3D1"/>

<!-- Keywords -->
<WordsStyle name="KEYWORDS" fgColor="FF8DBD" bgColor="120A14"/>

<!-- Comments -->
<WordsStyle name="COMMENT" fgColor="D9B8C4" bgColor="120A14"/>

<!-- Strings -->
<WordsStyle name="STRING" fgColor="FFD6E8" bgColor="120A14"/>

<!-- Numbers -->
<WordsStyle name="NUMBER" fgColor="FF6BA8" bgColor="120A14"/>
```
