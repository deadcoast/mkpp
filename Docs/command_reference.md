# Command Reference

> **Navigation**: [← Back to README](../README.md) | [Development Guide](development.md) | [Configuration](configuration_file.md)

## Table of Contents

- [Overview](#overview)
- [Interactive Commands](#interactive-commands)
- [Installation Commands](#installation-commands)
- [Configuration Commands](#configuration-commands)
- [Palette Editor Commands](#palette-editor-commands)
- [Utility Commands](#utility-commands)
- [Examples](#examples)
- [Related Documentation](#related-documentation)

## Overview

This document provides comprehensive reference for all milk++ CLI commands and their usage patterns.

## Interactive Commands

### `mkpp`

Launch interactive menu interface.

**Usage:**

```bash
mkpp
```

**What it does:**

- Opens the main interactive menu
- Provides guided installation options
- Access to Palette Editor for theme customization
- No arguments required

---

## Installation Commands

### `mkpp install <file>`

Install a theme from a local XML file.

**Arguments:**

- `<file>` - Path to `.xml` theme file

**Options:**

- `--name <name>` - Custom name for installed theme

**Examples:**

```bash
mkpp install Downloads/nord-theme.xml
mkpp install theme.xml --name "Nord Dark"
```

**Next Steps:**

- [Theme Activation Guide](../README.md#theme-activation)
- [Configuration Setup](configuration_file.md)

---

## Palette Editor Commands

### Palette Editor (Interactive)

Access the built-in visual theme editor through the main menu.

**Access:**

```bash
mkpp
# Select option 6: Palette Editor
```

**Features:**

#### 1. Edit Theme Variants

- **StrawberryMilk Classic** - Original warm pink theme
- **StrawberryMilk Modern** - Cooler, more neutral variant
- **StrawberryMilk High Contrast** - Enhanced contrast for accessibility

#### 2. Color Editing Categories

- **Background Colors** - Primary, secondary, surface backgrounds
- **Text Colors** - Primary, secondary, muted text
- **Accent Colors** - Syntax highlighting, numbers, strings

#### 3. Visual Preview

- **Real-time color preview** with colored blocks
- **Live editing** - see changes before saving
- **Multiple palette comparison**

#### 4. Apply Changes

- **Apply Theme to XML** - Updates source files
- **Automatic installation update** - Updates installed themes
- **No reinstallation required**

**Example Workflow:**

```bash
mkpp
→ 6                    # Palette Editor
→ 1                    # Edit Classic (ver_001)
→ 1                    # Edit Background Colors
→ Enter new hex values # FF0000, etc.
→ 4                    # Preview Changes
→ 5                    # Save Palette
→ 5                    # Apply Theme to XML
→ 1                    # Select StrawberryMilk Classic
→ Success!             # Theme updated
```

---

## Configuration Commands

### `mkpp path`

Display current configuration paths.

**Options:**

- `--setpath <path>` - Set default source directory

**Examples:**

```bash
# Show current paths
mkpp path

# Set source directory
mkpp path --setpath "D:\NotepadThemes"
```

**Related:**

- [Configuration Documentation](configuration_file.md)

---

## Utility Commands

### `mkpp themes`

List all currently installed themes.

**Usage:**

```bash
mkpp themes
```

**Output:**

```bash
┌─ Installed Themes ─────────────┐
│ Theme Name      │ File Size    │
├─────────────────┼──────────────┤
│ StrawberryMilk  │ 24.5 KB      │
│ Dracula         │ 18.3 KB      │
│ Nord            │ 22.1 KB      │
└─────────────────┴──────────────┘
```

---

## Examples

### Complete Workflow Example

```bash
# 1. Check current configuration
mkpp path

# 2. Set source directory
mkpp path --setpath "C:\MyThemes"

# 3. Install a theme
mkpp install "C:\MyThemes\dracula.xml" --name "Dracula Dark"

# 4. Verify installation
mkpp themes
```

### Batch Installation Workflow

```bash
# Use interactive mode for batch operations
mkpp
# Then select "Scan and Install" option
```

---

## Related Documentation

- **[README](../README.md)** - Project overview and quick start
- **[Development Guide](development.md)** - Technical setup and troubleshooting
- **[Configuration](configuration_file.md)** - Configuration file details
- **[Contributing](../CONTRIBUTING.md)** - How to contribute to the project
