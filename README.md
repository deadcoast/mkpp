# milk++ Theme Injector

<div align="center">

**Universal Theme Management for Notepad++**

A professional command-line interface for installing, managing, and organizing Notepad++ themes from multiple sources with an elegant terminal experience.

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![Click](https://img.shields.io/badge/Click-000000?style=for-the-badge&logo=python&logoColor=white)](https://click.palletsprojects.com/)
[![Rich](https://img.shields.io/badge/Rich-009485?style=for-the-badge&logo=python&logoColor=white)](https://rich.readthedocs.io/)
[![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://www.microsoft.com/windows)

[Installation](#installation) • [Usage](#usage) • [Commands](#command-reference) • [Contributing](#contributing)

</div>

---

## Overview

**milk++** (`mkpp`) is a streamlined CLI tool designed to simplify Notepad++ theme management on Windows. Install themes from local files, Git repositories, or batch-process entire directories through an intuitive menu-driven interface or direct command execution.

### Key Features

- **Multi-Source Installation** - Support for local files, Git repositories, and batch folder scanning
- **Interactive Menu System** - Organized, hierarchical menus for all operations
- **Automatic Path Detection** - Locates Notepad++ installation and theme directories
- **Batch Processing** - Install multiple themes simultaneously from any directory
- **Configuration Management** - Persistent settings for default source paths
- **Git Integration** - Clone and extract themes from any GitHub repository
- **Rich Terminal UI** - Professional styled output with tables, panels, and progress indicators

---

## Requirements

| Component | Version | Required |
|-----------|---------|----------|
| Windows | 7+ | Yes |
| Python | 3.7+ | Yes |
| Notepad++ | Any | Yes |
| Git | 2.0+ | Optional* |

*Required only for Git repository installations

---

## Installation

### Quick Install

```bash
git clone https://github.com/yourusername/milk-pp.git
cd milk-pp
install.bat
```

The installer will:
1. Verify Python installation
2. Install required dependencies
3. Register `mkpp` as a system command

### Manual Installation

```bash
# Clone repository
git clone https://github.com/yourusername/milk-pp.git
cd milk-pp

# Install dependencies
pip install -r requirements.txt

# Install as system command
pip install -e .
```

### Verification

```bash
mkpp --help
```

Expected output:
```
Usage: mkpp [OPTIONS] COMMAND [ARGS]...
  milk++ - Universal Notepad++ Theme Injector
```

---

## Usage

### Interactive Mode

Launch the interactive menu system:

```bash
mkpp
```

#### Main Menu Structure

```
Main Menu
├── Scan and Install              # Batch install from folder
├── Install from Git Repository   # Clone and install from Git
├── All Install Options           # Submenu with all methods
│   ├── Install from File
│   ├── Install from Git Repository
│   └── Scan and Install (Batch)
├── View Installed Themes         # List current themes
├── Settings                      # Configuration submenu
│   ├── Show Paths & Configuration
│   └── Set Source Path
└── Quit
```

### Direct Command Execution

```bash
# Install single theme file
mkpp install path/to/theme.xml

# Install with custom name
mkpp install theme.xml --name "CustomTheme"

# View configuration
mkpp path

# Set default source directory
mkpp path --setpath "C:\Themes"

# List installed themes
mkpp themes
```

---

## Command Reference

### `mkpp`
Launch interactive menu interface.

**Usage:**
```bash
mkpp
```

---

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

---

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

---

### `mkpp themes`
List all currently installed themes.

**Usage:**
```bash
mkpp themes
```

**Output:**
```
┌─ Installed Themes ─────────────┐
│ Theme Name      │ File Size    │
├─────────────────┼──────────────┤
│ Dracula         │ 24.5 KB      │
│ Nord            │ 18.3 KB      │
│ Monokai         │ 22.1 KB      │
└─────────────────┴──────────────┘
```

---

## Configuration

### Directory Structure

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

---

## Theme Activation

After installing themes:

1. **Restart Notepad++** completely
2. Navigate to **Settings** → **Style Configurator**
3. Select theme from dropdown menu at top
4. Click **Save & Close**

Changes apply immediately after selection.

---

## Theme Sources

### Recommended Repositories

| Repository | Description | URL |
|-----------|-------------|-----|
| Dracula | Dark theme for many applications | `github.com/dracula/notepad-plus-plus` |
| Material Theme | Material Design colors | `github.com/Codextor/npp-material-theme` |
| Monokai | Classic Monokai port | `github.com/Dayle-Rees/notepad-plus-plus-themes` |

### Finding Themes

- **GitHub**: Search "notepad++ theme"
- **Notepad++ Forums**: Community themes section
- **DeviantArt**: Notepad++ theme category
- Any `.xml` theme file compatible with Notepad++ Style Configurator

---

## Troubleshooting

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

## Development

### Project Structure

```
milk-pp/
├── mkpp_cli.py              # Main application logic
├── setup.py                 # Package configuration
├── requirements.txt         # Python dependencies
├── install.bat             # Windows installer
├── README.md               # This file
├── LICENSE                 # MIT License
└── PROJECT_STRUCTURE.md    # Development guide
```

### Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| click | ≥8.0.0 | CLI framework and command parsing |
| rich | ≥10.0.0 | Terminal styling and UI components |
| requests | ≥2.25.0 | HTTP operations (future use) |

### Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/enhancement`
3. Commit changes: `git commit -m 'Add enhancement'`
4. Push to branch: `git push origin feature/enhancement`
5. Submit Pull Request

### Development Setup

```bash
# Clone repository
git clone https://github.com/yourusername/milk-pp.git
cd milk-pp

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

---

## Technical Details

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

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Click Framework**: Command-line interface foundation
- **Rich Library**: Terminal styling and UI components
- **Notepad++ Community**: Inspiration and theme ecosystem

---

## Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/milk-pp/issues)
- **Documentation**: [Full Documentation](https://github.com/yourusername/milk-pp/wiki)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/milk-pp/discussions)

---

<div align="center">

**milk++** | Professional Theme Management for Notepad++

Built for developers who value efficiency and aesthetic

</div>