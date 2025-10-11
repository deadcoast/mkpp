# 🥛 milk++ (mkpp)

**Universal CLI theme injector for Notepad++ on Windows**

Install ANY Notepad++ theme from files, Git repos, or folders with a beautiful CLI interface.

---

## ✨ Features

- 📁 **Install from Files** - Install any `.xml` theme file
- 🔗 **Install from Git** - Clone and install themes from any Git repository
- 📦 **Batch Install** - Install multiple themes from a folder at once
- 🖼️ **Beautiful CLI** - Rich, framed ASCII interface
- 🗂️ **Theme Browser** - View all installed themes
- ⚙️ **Path Management** - Set default source directories
- 🚀 **Native Command** - Run `mkpp` from anywhere

---

## 📋 Requirements

- **Windows** (7, 8, 10, 11)
- **Python 3.7+**
- **Notepad++** installed
- **Git** (optional, for Git repository installs)

---

## 🚀 Installation

### Quick Install (Windows)

```bash
# Navigate to project folder
cd milk-pp

# Run installer
install.bat
```

### Manual Install

```bash
pip install -r requirements.txt
pip install -e .
```

---

## 📖 Usage

### Interactive Menu

```bash
mkpp
```

Menu options:
1. Install Theme from File
2. Install from Git Repository
3. Install from Source Folder (Batch)
4. View Installed Themes
5. Show Paths & Configuration
6. Set Source Path

### Command-Line

```bash
# Install a theme file
mkpp install path/to/theme.xml

# Install with custom name
mkpp install theme.xml --name "My Custom Theme"

# Show configuration
mkpp path

# Set source folder
mkpp path --setpath "C:\MyThemes"

# List installed themes
mkpp themes
```

---

## 🎨 Examples

### Install Single Theme

```bash
mkpp install "C:\Downloads\CoolTheme.xml"
```

### Install from GitHub

```bash
# In interactive menu, select option 2
# Enter: https://github.com/username/notepad-theme
```

Popular theme repos:
- `https://github.com/dracula/notepad-plus-plus`
- `https://github.com/oivva/st-material-theme`
- Any repo with `.xml` theme files

### Batch Install

```bash
# Set your themes folder
mkpp path --setpath "D:\MyThemes"

# Then use option 3 in menu to install all .xml files
```

---

## 📂 How It Works

1. **Locates Notepad++**: Finds `%AppData%\Notepad++\themes`
2. **Copies Theme Files**: Installs `.xml` files to themes directory
3. **Ready to Use**: Restart Notepad++ and select theme in Style Configurator

### Activating Installed Themes

1. Restart Notepad++
2. Go to **Settings** → **Style Configurator**
3. Select your theme from the dropdown
4. Enjoy!

---

## 🛠️ Configuration

Config stored in: `%USERPROFILE%\.mkpp\config.txt`

Default theme directory: `%AppData%\Notepad++\themes`

---

## 🐛 Troubleshooting

**"Notepad++ directory not found"**
- Install Notepad++ first
- Run Notepad++ once to create directories

**"Theme doesn't appear"**
- Restart Notepad++ completely
- Check file is in `%AppData%\Notepad++\themes`
- Verify file is `.xml` format

**"mkpp: command not found"**
- Run `pip install -e .` in project folder
- Restart terminal
- Check Python's Scripts folder is in PATH

---

## 📝 License

MIT License - See LICENSE file

---

## 🎨 Where to Find Themes

- GitHub: Search "notepad++ theme"
- DeviantArt: Notepad++ theme section
- Notepad++ forums: User-created themes
- Any `.xml` theme file works

---

Made with 🥛 for Notepad++ users