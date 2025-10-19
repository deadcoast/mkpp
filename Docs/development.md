# Development Guide

> **Navigation**: [← Back to README](../README.md) | [Command Reference](command_reference.md) | [Configuration](configuration_file.md)

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Development Setup](#development-setup)
- [Troubleshooting](#troubleshooting)
- [Related Documentation](#related-documentation)

## Overview

This guide covers development setup, technical implementation details, and troubleshooting for milk++ contributors and advanced users.

## Project Structure

```
milk-pp/
├── mkpp_cli.py              # Main application logic
├── setup.py                 # Package configuration
├── requirements.txt         # Python dependencies
├── install.bat             # Windows installer
├── install.ps1             # PowerShell installer
├── README.md               # This file
├── LICENSE                 # MIT License
├── Themes/                 # Theme files and palette editor
│   ├── StrawberryMilk.xml  # Default theme file
│   ├── StrawberryMilk.md   # Color palette documentation
│   └── color_config.json   # Palette configuration
└── Docs/                   # Documentation
    ├── command_reference.md
    ├── development.md
    ├── configuration_file.md
    └── template_logic.md
```

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| click | ≥8.0.0 | CLI framework and command parsing |
| rich | ≥10.0.0 | Terminal styling and UI components |
| json | built-in | Palette configuration management |
| re | built-in | XML color pattern replacement |
| requests | ≥2.25.0 | HTTP operations (future use) |

## Contributing

For detailed contributing guidelines, see the [Contributing Guide](../CONTRIBUTING.md).

**Quick Start:**

1. Fork the repository
2. Create feature branch: `git checkout -b feature/enhancement`
3. Commit changes: `git commit -m 'Add enhancement'`
4. Push to branch: `git push origin feature/enhancement`
5. Submit Pull Request

## Development Setup

```bash
# Clone repository
git clone https://github.com/ryanf-github/mkpp.git
cd mkpp

# Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate

# Install in development mode
pip install -e .

# Make changes to mkpp_cli.py

# Test immediately
mkpp
```

Changes are reflected immediately due to editable install (`-e` flag).

## Palette Editor Implementation

The palette editor is integrated directly into the main CLI application (`mkpp_cli.py`).

### Key Components

#### Color Configuration (`Themes/color_config.json`)

```json
{
  "ver_001": {
    "name": "StrawberryMilk Classic",
    "description": "Original warm pink theme",
    "colors": {
      "bg_primary": "120A14",
      "bg_secondary": "1C1420",
      "text_primary": "E8C5D5",
      // ... more colors
    }
  }
}
```

#### Core Functions

- `load_palette_config()` - Loads color definitions from JSON
- `save_palette_config()` - Saves modified color configurations
- `update_theme_xml()` - Applies color changes to XML files
- `show_color_preview()` - Displays visual color previews
- `show_palette_editor()` - Main palette editor interface

#### Color Replacement Logic
The system uses regex pattern matching to replace colors in XML files:

```python
replacements = [
    (r'bgColor="120A14"', f'bgColor="{colors["bg_primary"]}"'),
    (r'fgColor="E8C5D5"', f'fgColor="{colors["text_primary"]}"'),
    # ... more patterns
]
```

#### Automatic Theme Updates
When applying a palette, the system:

1. Updates the source XML file in `Themes/StrawberryMilk.xml`
2. Checks if theme is installed in Notepad++ directory
3. Automatically copies updated theme to installed location
4. Provides user feedback about restart requirements

---

## Troubleshooting

### Installation Process

1. **Path Detection**: Locates `%AppData%\Notepad++\themes` directory
2. **Validation**: Verifies `.xml` file format
3. **File Copy**: Transfers theme to themes directory
4. **Verification**: Confirms successful installation

### Git Integration Workflow

1. **Clone**: Repository cloned to temporary directory (`%USERPROFILE%\.mkpp\temp_repo`)
2. **Scan**: Searches for all `.xml` files
3. **Selection**: User chooses themes to install
4. **Installation**: Copies selected themes to Notepad++ directory
5. **Cleanup**: Removes temporary directory with permission handling

### Windows Permission Handling

The tool includes specialized handling for Windows file permissions, particularly for Git repositories containing read-only files. The `safe_rmtree()` function modifies permissions before deletion to prevent access denied errors.

### Notepad++ Directory Not Found

**Symptoms:** Error message about missing Notepad++ directory

**Solutions:**

1. Verify Notepad++ is installed
2. Run Notepad++ once to initialize directories
3. Check `%AppData%\Notepad++` exists

---

### Theme Not Appearing

**Symptoms:** Theme not visible in Style Configurator after installation

**Solutions:**

1. Restart Notepad++ completely (close all windows)
2. Verify file exists in `%AppData%\Notepad++\themes`
3. Confirm file has `.xml` extension
4. Check file is not corrupted (valid XML)

---

### Command Not Found

**Symptoms:** `'mkpp' is not recognized as an internal or external command`

**Solutions:**

1. Reinstall with `pip install -e .` in project directory
2. Add Python Scripts directory to PATH
3. Restart terminal/command prompt
4. Verify installation: `pip list | findstr milk`

---

### Permission Errors

**Symptoms:** Access denied errors during installation

**Solutions:**

1. Run terminal as Administrator
2. Install in user mode: `pip install -e . --user`
3. Check Notepad++ directory permissions

---

### Git Clone Failures

**Symptoms:** Repository clone operations fail

**Solutions:**

1. Verify Git is installed: `git --version`
2. Check internet connectivity
3. Confirm repository URL is valid
4. Try HTTPS URL instead of SSH

---

## Related Documentation

- **[README](../README.md)** - Project overview and quick start
- **[Command Reference](command_reference.md)** - Complete CLI documentation
- **[Configuration](configuration_file.md)** - Configuration file details
- **[Contributing](../CONTRIBUTING.md)** - How to contribute to the project
