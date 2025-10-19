# Configuration Guide

> **Navigation**: [← Back to README](../README.md) | [Command Reference](command_reference.md) | [Development Guide](development.md)

## Table of Contents

- [Overview](#overview)
- [Directory Structure](#directory-structure)
- [Configuration File](#configuration-file)
- [Palette Configuration](#palette-configuration)
- [Usage Examples](#usage-examples)
- [Related Documentation](#related-documentation)

## Overview

This guide explains how to configure milk++ for optimal usage, including source path management and directory structure.

## Directory Structure

```
%USERPROFILE%\.mkpp\
└── config.txt              # Source path configuration

%AppData%\Notepad++\
└── themes\
    ├── theme1.xml
    ├── theme2.xml
    ├── theme3.xml
    └── StrawberryMilk.xml   # Default theme (auto-updated)

mkpp\Themes\
├── StrawberryMilk.xml      # Source theme file
├── StrawberryMilk.md       # Color palette documentation
└── color_config.json       # Palette configuration
```

### Configuration File

Location: `%USERPROFILE%\.mkpp\config.txt`

Contents: Single line containing the default source path for batch operations.

**Example:**

```
C:\Users\Username\Documents\NotepadThemes
```

**How to set:**

```bash
mkpp path --setpath "C:\MyThemes"
```

---

## Palette Configuration

The palette editor uses a JSON configuration file to manage color variants.

### Color Configuration File

**Location:** `Themes/color_config.json`

**Structure:**

```json
{
  "ver_001": {
    "name": "StrawberryMilk Classic",
    "description": "Original warm pink theme",
    "colors": {
      "bg_primary": "120A14",
      "bg_secondary": "1C1420",
      "bg_surface": "1f181e",
      "bg_surface_alt": "3D2F42",
      "text_primary": "E8C5D5",
      "text_secondary": "FFB3D1",
      "text_muted": "D9B8C4",
      "accent_primary": "FF8DBD",
      "accent_secondary": "FF6BA8",
      "accent_light": "FFD6E8"
    }
  }
}
```

### Color Categories

| Category | Description | Elements |
|----------|-------------|----------|
| `bg_*` | Background colors | Primary, secondary, surface backgrounds |
| `text_*` | Text colors | Primary, secondary, muted text |
| `accent_*` | Accent colors | Syntax highlighting, numbers, strings |

### Automatic Updates

When using the palette editor:

1. Changes are saved to `color_config.json`
2. XML files are automatically updated
3. Installed themes are updated (if present)
4. No manual reinstallation required

---

## Usage Examples

### Setting Up Your Environment

```bash
# 1. Check current configuration
mkpp path

# 2. Set your theme source directory
mkpp path --setpath "C:\Users\YourName\Documents\Themes"

# 3. Verify the setting
mkpp path
```

### Batch Operations

Once configured, you can use the interactive menu for batch operations:

```bash
mkpp
# Select "Scan and Install" to use your configured source path
```

---

## Related Documentation

- **[README](../README.md)** - Project overview and quick start
- **[Command Reference](command_reference.md)** - Complete CLI documentation
- **[Development Guide](development.md)** - Technical setup and troubleshooting
- **[Contributing](../CONTRIBUTING.md)** - How to contribute to the project
