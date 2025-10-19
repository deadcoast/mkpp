# Configuration Guide

> **Navigation**: [← Back to README](../README.md) | [Command Reference](command_reference.md) | [Development Guide](development.md)

## Table of Contents

- [Overview](#overview)
- [Directory Structure](#directory-structure)
- [Configuration File](#configuration-file)
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
    └── theme3.xml
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
