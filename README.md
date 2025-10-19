# milk++

> [!IMPORTANT]
> Build for the notepad++ editor
> Function: CLI Theme Editing and Installation

<div align="center">

## Universal Theme Management for Notepad++

A professional command-line interface for installing, managing, and organizing Notepad++ themes from multiple sources with an elegant terminal experience.

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![Click](https://img.shields.io/badge/Click-000000?style=for-the-badge&logo=python&logoColor=white)](https://click.palletsprojects.com/)
[![Rich](https://img.shields.io/badge/Rich-009485?style=for-the-badge&logo=python&logoColor=white)](https://rich.readthedocs.io/)
[![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://www.microsoft.com/windows)

[Installation](#installation) • [Usage](#usage) • [Commands](#commands) • [Contributing](#contributing)

</div>

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
    - [Interactive Mode](#interactive-mode)
    - [Direct Commands](#direct-command-execution)
    - [Commands](#commands)
- [Theme Activation](#theme-activation)
- [Theme Sources](#theme-sources)
- [Documentation](#documentation)
- [License](#license)
- [Contributing](#contributing)
- [Support](#support)

## Quick Navigation

| For... | Go to... |
|--------|----------|
| **Getting Started** | [Installation](#installation) |
| **Using the Tool** | [Usage](#usage) or [Command Reference](Docs/command_reference.md) |
| **Configuration** | [Configuration Guide](Docs/configuration_file.md) |
| **Development** | [Development Guide](Docs/development.md) |
| **Contributing** | [Contributing Guide](CONTRIBUTING.md) |
| **Troubleshooting** | [Development Guide](Docs/development.md#troubleshooting) |

---

## Overview

**milk++** (`mkpp`) is a streamlined CLI tool designed to simplify Notepad++ theme management on Windows. Install themes from local files, Git repositories, or batch-process entire directories through an intuitive menu-driven interface or direct command execution.

### Key Features

- **Multi-Source Installation** - Support for local files, Git repositories, and batch folder scanning
- **Interactive Menu System** - Organized, hierarchical menus for all operations
- **Visual Palette Editor** - Built-in color editor with live preview and multiple theme variants
- **Automatic Path Detection** - Locates Notepad++ installation and theme directories
- **Batch Processing** - Install multiple themes simultaneously from any directory
- **Configuration Management** - Persistent settings for default source paths
- **Git Integration** - Clone and extract themes from any GitHub repository
- **Rich Terminal UI** - Professional styled output with tables, panels, and progress indicators
- **Live Theme Updates** - Automatically updates installed themes without reinstalling

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

**PowerShell (Recommended):**

```powershell
git clone https://github.com/ryanf-github/mkpp.git
cd mkpp
.\install.ps1
```

**Command Prompt:**

```cmd
git clone https://github.com/ryanf-github/mkpp.git
cd mkpp
.\install.bat
```

The installer will:

1. Verify Python installation
2. Install required dependencies
3. Register `mkpp` as a system command

### Manual Installation

**Command Prompt:**

```cmd
# Clone repository
git clone https://github.com/ryanf-github/mkpp.git
cd mkpp

# Install dependencies
pip install -r requirements.txt

# Install as system command
pip install -e .
```

**PowerShell:**

```powershell
# Clone repository
git clone https://github.com/ryanf-github/mkpp.git
cd mkpp

# Install dependencies
pip install -r requirements.txt

# Install as system command
pip install -e .
```

**With Virtual Environment (Recommended):**

```powershell
# Clone repository
git clone https://github.com/ryanf-github/mkpp.git
cd mkpp

# Create virtual environment
python -m venv .venv

# Activate virtual environment (PowerShell)
.\.venv\Scripts\Activate.ps1

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

### Troubleshooting Installation

**PowerShell Execution Policy Issues:**

```powershell
# If you get execution policy errors, run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Virtual Environment Activation (Windows):**

```powershell
# PowerShell
.\.venv\Scripts\Activate.ps1

# Command Prompt
.venv\Scripts\activate.bat
```

**If `mkpp` command not found:**

```bash
# Reinstall in development mode
pip install -e .

# Or add Python Scripts to PATH
# Add %USERPROFILE%\AppData\Roaming\Python\Python3x\Scripts to your PATH
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
├── Palette Editor                # Visual theme color editor
│   ├── Edit StrawberryMilk Classic
│   ├── Edit StrawberryMilk Modern
│   ├── Edit StrawberryMilk High Contrast
│   ├── Preview All Palettes
│   └── Apply Theme to XML
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

### Palette Editor

Access the built-in visual theme editor through the interactive menu:

```bash
mkpp
# Select option 6: Palette Editor
```

**Features:**

- **Visual Color Preview** - See color changes in real-time
- **Multiple Theme Variants** - Classic, Modern, and High Contrast versions
- **Live Editing** - Modify colors by category (Background, Text, Accent)
- **Instant Application** - Apply changes directly to XML and installed themes
- **No Reinstallation Required** - Updates existing themes automatically

### Commands

For detailed command reference, see [Command Reference](Docs/command_reference.md).

#### User Workflow Guide

**New Users:**

1. [Install milk++](#installation)
2. [Try the interactive mode](#interactive-mode)
3. [Learn about theme activation](#theme-activation)

**Regular Users:**

1. [Use direct commands](#direct-command-execution)
2. [Configure your source paths](Docs/configuration_file.md)
3. [Explore theme sources](#theme-sources)

**Developers:**

1. [Read the development guide](Docs/development.md)
2. [Check the contributing guidelines](CONTRIBUTING.md)
3. [Set up your development environment](Docs/development.md#development-setup)

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

## Documentation

- **[Command Reference](Docs/command_reference.md)** - Complete CLI documentation
- **[Development Guide](Docs/development.md)** - Setup and technical details
- **[Configuration](Docs/configuration_file.md)** - Configuration options
- **[Contributing](CONTRIBUTING.md)** - How to contribute to the project

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Click Framework**: Command-line interface foundation
- **Rich Library**: Terminal styling and UI components
- **Notepad++ Community**: Inspiration and theme ecosystem

---

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details on how to get started.

## Support

- **Issues**: [GitHub Issues](https://github.com/ryanf-github/mkpp/issues)
- **Discussions**: [GitHub Discussions](https://github.com/ryanf-github/mkpp/discussions)

---

<div align="center">

**milk++** | Professional Theme Management for Notepad++

Built for developers who value efficiency and aesthetic

</div>
