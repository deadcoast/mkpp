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

### `mkpp install-udl <file>`

Install a UDL file from a local `.udl.xml` file.

**Arguments:**

- `<file>` - Path to `.udl.xml` UDL file

**Options:**

- `--name <name>` - Custom name for installed UDL

**Examples:**

```bash
mkpp install-udl Themes/UDL/markdown.strawberrymilk.udl.xml
mkpp install-udl file.udl.xml --name "CustomUDL"
```

### `mkpp scan <directory>`

Scan and install all themes and UDL files from a directory.

**Arguments:**

- `<directory>` - Path to directory containing themes and UDL files

**Examples:**

```bash
mkpp scan Themes/UDL/
mkpp scan C:\MyThemes
```

**Features:**

- Automatically detects both `.xml` (themes) and `.udl.xml` (UDL) files
- Shows separate counts for each file type
- Installs both types to their respective Notepad++ directories
- Provides progress tracking for each file type

**Next Steps:**

- [Theme & UDL Activation Guide](../README.md#theme--udl-activation)
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

### `mkpp udls`

List all currently installed UDL files.

**Usage:**

```bash
mkpp udls
```

**Output:**

```bash
┌─ Installed UDL Files ──────────────────────┐
│ UDL Name                       │ File Size │
├────────────────────────────────┼───────────┤
│ markdown.strawberrymilk.udl    │ 5.4 KB    │
│ markdown.strawberrymilk.modern │ 5.7 KB    │
│ markdown.strawberrymilk.classic│ 5.7 KB    │
└────────────────────────────────┴───────────┘
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

# 4. Install a UDL file
mkpp install-udl "C:\MyThemes\markdown.strawberrymilk.udl.xml"

# 5. Verify installations
mkpp themes
mkpp udls
```

### Batch Installation Workflow

```bash
# Scan and install all themes and UDL files
mkpp scan Themes/UDL/

# Or use interactive mode for batch operations
mkpp
# Then select "Scan and Install" option
```

### UDL-Specific Workflow

```bash
# Install all StrawberryMilk UDL variants
mkpp scan Themes/UDL/

# Install individual UDL files
mkpp install-udl Themes/UDL/markdown.strawberrymilk.udl.xml
mkpp install-udl Themes/UDL/markdown.strawberrymilk.modern.udl.xml
mkpp install-udl Themes/UDL/markdown.strawberrymilk.classic.udl.xml
mkpp install-udl Themes/UDL/markdown.strawberrymilk.highcontrast.udl.xml
```

---

## Related Documentation

- **[README](../README.md)** - Project overview and quick start
- **[Development Guide](development.md)** - Technical setup and troubleshooting
- **[Configuration](configuration_file.md)** - Configuration file details
- **[Contributing](../CONTRIBUTING.md)** - How to contribute to the project
