# Palette Template Conversion

> **Note**: This document describes the original StrawberryMilk Palettes. The current system uses an integrated palette editor with multiple theme variants.

## StrawberryMilk Palette Variants

### Classic (ver_001)

- Background: `#120A14` (very dark pink-purple)
- Secondary BG: `#1C1420` (dark pink-purple)
- Surface: `#1f181e` (medium pink-purple)
- Text: `#E8C5D5` (light pink)
- Secondary Text: `#FFB3D1` (bright pink)
- Accent: `#FF8DBD` (bright pink)
- Secondary Accent: `#FF6BA8` (deeper pink)

### Modern (ver_002)

- Background: `#141415` (dark gray)
- Secondary BG: `#161619` (darker gray)
- Surface: `#18181c` (neutral gray)
- Text: `#E8C5D5` (light pink)
- Secondary Text: `#FFB3D1` (bright pink)
- Accent: `#FF8DBD` (bright pink)

### High Contrast (ver_003)

- Background: `#0F0A0D` (very dark)
- Secondary BG: `#1A0F14` (dark)
- Surface: `#251A1F` (medium dark)
- Text: `#F5E6F0` (very light pink)
- Secondary Text: `#FFB3D1` (bright pink)
- Accent: `#FF8DBD` (bright pink)

## Current System: Integrated Palette Editor

The current system no longer uses manual color mapping. Instead, it features:

### Automated Color Management

- **JSON Configuration**: Colors stored in `Themes/color_config.json`
- **Multiple Variants**: Classic, Modern, and High Contrast themes
- **Visual Editor**: Built-in palette editor with live preview
- **Automatic Updates**: XML files and installed themes updated automatically

### Color Categories

- **Background Colors**: Primary, secondary, surface backgrounds
- **Text Colors**: Primary, secondary, muted text
- **Accent Colors**: Syntax highlighting, numbers, strings

### Usage

```bash
mkpp
→ 6                    # Palette Editor
→ 1                    # Edit Classic (ver_001)
→ Edit colors by category
→ Apply Theme to XML
→ Automatic installation update
```

### Original Color Mapping (Legacy)

→ `120A14` (StrawberryMilk primary background)
→ `FFB3D1` (StrawberryMilk primary text)
→ `D9B8C4` (StrawberryMilk muted text)
→ `FF8DBD` (StrawberryMilk accent)
→ `FFD6E8` (StrawberryMilk light accent)
→ `FF6BA8` (StrawberryMilk secondary accent)
→ `E8C5D5` (StrawberryMilk secondary text)

## StrawberryMilk XML

### Color Mapping Applied

| StrawberryMilk Color | Usage                     |
| -------------------- | ------------------------- |
| `#120A14`            | Primary background        |
| `#FFB3D1`            | Primary text              |
| `#D9B8C4`            | Comments & muted text     |
| `#FF8DBD`            | Keywords & syntax         |
| `#FFD6E8`            | Strings & literals        |
| `#FF6BA8`            | Numbers & accents         |
| `#E8C5D5`            | Functions & identifiers   |
| `#E8C5D5`            | Operators & special chars |
| `#FF6BA8`            | Errors & warnings         |
| `#FFD6E8`            | Special syntax            |

### Theme Features

- Consistent StrawberryMilk branding throughout all syntax highlighting
- High contrast maintained for readability
- All language support preserved (Java, C++, Python, JavaScript, etc.)
- UI elements properly themed (tabs, margins, selection, etc.)
- Accessibility maintained with proper color contrast ratios

### CLI Usage

```bash
mkpp install StrawberryMilk.xml --name "StrawberryMilk"
```
