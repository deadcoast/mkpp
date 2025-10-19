# UDL Integration Guide

> **Navigation**: [← Back to README](../README.md) | [Command Reference](command_reference.md) | [Development Guide](development.md)

## Table of Contents

- [Overview](#overview)
- [UDL File Structure](#udl-file-structure)
- [Installation Methods](#installation-methods)
- [StrawberryMilk UDL Variants](#strawberrymilk-udl-variants)
- [Integration with Themes](#integration-with-themes)
- [Usage Examples](#usage-examples)
- [Troubleshooting](#troubleshooting)
- [Related Documentation](#related-documentation)

## Overview

User Defined Languages (UDL) in Notepad++ allow custom syntax highlighting for languages not natively supported. milk++ provides comprehensive UDL management alongside theme management, enabling coordinated installation and management of both file types.

## UDL File Structure

### File Format

- **Extension**: `.udl.xml`
- **Location**: `%AppData%\Notepad++\userDefineLangs\`
- **Structure**: XML-based syntax highlighting definitions

### Key Components

- **Language Definition**: Name and description
- **Keywords**: Reserved words and operators
- **Comments**: Single-line and multi-line comment patterns
- **Numbers**: Numeric literal patterns
- **Strings**: String literal patterns
- **Operators**: Special characters and operators

## Installation Methods

### Direct Installation

```bash
# Install single UDL file
mkpp install-udl path/to/file.udl.xml

# Install with custom name
mkpp install-udl file.udl.xml --name "CustomUDL"
```

### Batch Installation

```bash
# Scan and install all UDL files from directory
mkpp scan Themes/UDL/

# Scan mixed directory (themes + UDL files)
mkpp scan path/to/directory/
```

### Interactive Installation

```bash
mkpp
# Select "Scan and Install" option
# Automatically detects and installs both themes and UDL files
```

## StrawberryMilk UDL Variants

### Available Variants

| UDL File | Description | Theme Match |
|----------|-------------|-------------|
| `markdown.strawberrymilk.udl.xml` | Modern variant (default) | StrawberryMilk Modern |
| `markdown.strawberrymilk.modern.udl.xml` | Cooler, neutral colors | StrawberryMilk Modern |
| `markdown.strawberrymilk.classic.udl.xml` | Original warm pink | StrawberryMilk Classic |
| `markdown.strawberrymilk.highcontrast.udl.xml` | Enhanced accessibility | StrawberryMilk High Contrast |

### Color Scheme Mapping

#### StrawberryMilk Modern (Default)

- **Background**: `#141415` (dark purple-gray)
- **Text Primary**: `#E8C5D5` (light pink)
- **Text Secondary**: `#FFB3D1` (bright pink)
- **Accent Colors**: `#FF8DBD`, `#FF6BA8`, `#FFD6E8`
- **Comments**: `#BB889F` (muted pink)

#### StrawberryMilk Classic

- **Background**: `#120A14` (darker purple)
- **Text Primary**: `#E8C5D5` (light pink)
- **Comments**: `#D9B8C4` (warmer pink)

#### StrawberryMilk High Contrast

- **Background**: `#0F0A0D` (darkest purple)
- **Text Primary**: `#F5E6F0` (brightest pink)
- **Comments**: `#E8C5D5` (light pink)

## Integration with Themes

### Coordinated Installation

```bash
# Install matching theme and UDL
mkpp install Themes/StrawberryMilk.xml
mkpp install-udl Themes/UDL/markdown.strawberrymilk.udl.xml

# Or install all variants at once
mkpp scan Themes/UDL/
```

### Activation Workflow

1. **Install Theme**: `mkpp install theme.xml`
2. **Install UDL**: `mkpp install-udl udl.udl.xml`
3. **Restart Notepad++**
4. **Activate Theme**: Settings → Style Configurator
5. **Activate UDL**: Language → User Defined Language

## Usage Examples

### Complete UDL Workflow

```bash
# 1. Check current UDL installations
mkpp udls

# 2. Install all StrawberryMilk UDL variants
mkpp scan Themes/UDL/

# 3. Install individual UDL files
mkpp install-udl Themes/UDL/markdown.strawberrymilk.udl.xml
mkpp install-udl Themes/UDL/markdown.strawberrymilk.modern.udl.xml
mkpp install-udl Themes/UDL/markdown.strawberrymilk.classic.udl.xml
mkpp install-udl Themes/UDL/markdown.strawberrymilk.highcontrast.udl.xml

# 4. Verify installations
mkpp udls
```

### Batch Processing

```bash
# Set UDL directory as source
mkpp path --setpath "Themes/UDL"

# Use interactive mode for batch operations
mkpp
# Select "Scan and Install" option
```

### Git Repository Integration

```bash
# Clone repository with both themes and UDL files
mkpp
# Select "Install from Git Repository"
# Enter repository URL
# Choose files to install (themes and UDL files)
```

## Troubleshooting

### UDL Not Appearing

**Symptoms:** UDL not visible in Language menu after installation

**Solutions:**

1. Restart Notepad++ completely (close all windows)
2. Verify file exists in `%AppData%\Notepad++\userDefineLangs`
3. Confirm file has `.udl.xml` extension
4. Check file is not corrupted (valid XML)
5. Navigate to **Language** → **User Defined Language** to find your UDL

### Installation Failures

**Symptoms:** UDL installation fails with error messages

**Solutions:**

1. Check file permissions on target directory
2. Verify UDL file is valid XML
3. Ensure Notepad++ is installed
4. Run as Administrator if needed

### Color Mismatch

**Symptoms:** UDL colors don't match theme colors

**Solutions:**

1. Ensure you're using matching theme and UDL variants
2. Restart Notepad++ after installation
3. Check that both theme and UDL are properly installed
4. Verify color codes in UDL file match theme colors

## Related Documentation

- **[README](../README.md)** - Project overview and quick start
- **[Command Reference](command_reference.md)** - Complete CLI documentation
- **[Development Guide](development.md)** - Technical setup and troubleshooting
- **[Configuration](configuration_file.md)** - Configuration file details
- **[Contributing](../CONTRIBUTING.md)** - How to contribute to the project
