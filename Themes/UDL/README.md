# StrawberryMilk UDL Integration for milk++

This directory contains User Defined Language (UDL) files for Notepad++ that integrate seamlessly with the **milk++** theme management system.

## Overview

The StrawberryMilk UDL files provide syntax highlighting for Markdown files that perfectly matches the StrawberryMilk theme variants available in milk++.

## Available UDL Files

| File | Description | Theme Variant |
|------|-------------|---------------|
| `markdown.strawberrymilk.udl.xml` | Main StrawberryMilk UDL | Modern (default) |
| `markdown.strawberrymilk.modern.udl.xml` | Modern variant UDL | Cooler, neutral |
| `markdown.strawberrymilk.classic.udl.xml` | Classic variant UDL | Original warm pink |
| `markdown.strawberrymilk.highcontrast.udl.xml` | High Contrast UDL | Enhanced accessibility |

## Color Scheme Mapping

### StrawberryMilk Modern (Default)

- **Background**: `#141415` (dark purple-gray)
- **Text Primary**: `#E8C5D5` (light pink)
- **Text Secondary**: `#FFB3D1` (bright pink)
- **Accent Colors**: `#FF8DBD`, `#FF6BA8`, `#FFD6E8`
- **Comments**: `#BB889F` (muted pink)

### StrawberryMilk Classic

- **Background**: `#120A14` (darker purple)
- **Text Primary**: `#E8C5D5` (light pink)
- **Comments**: `#D9B8C4` (warmer pink)

### StrawberryMilk High Contrast

- **Background**: `#0F0A0D` (darkest purple)
- **Text Primary**: `#F5E6F0` (brightest pink)
- **Comments**: `#E8C5D5` (light pink)

## Integration with milk++

### Installation via milk++

1. **Install via milk++ CLI**:
   ```bash
   mkpp install Themes/UDL/markdown.strawberrymilk.udl.xml
   mkpp install Themes/UDL/markdown.strawberrymilk.modern.udl.xml
   mkpp install Themes/UDL/markdown.strawberrymilk.classic.udl.xml
   mkpp install Themes/UDL/markdown.strawberrymilk.highcontrast.udl.xml
   ```

2. **Batch Installation**:
   ```bash
   mkpp scan Themes/UDL/
   ```

### Manual Installation

1. Copy the desired UDL file to your Notepad++ user directory:
   - `%APPDATA%\Notepad++\userDefineLangs\`

2. Restart Notepad++

3. In Notepad++, go to **Language** → **User Defined Language** → **Define your language...**

4. Import the UDL file

## Usage

### Activating UDL in Notepad++

1. Open a Markdown file (`.md` or `.markdown`)
2. Go to **Language** → **User Defined Language**
3. Select the appropriate StrawberryMilk variant:
   - **Markdown [StrawberryMilk]** (Modern)
   - **Markdown [StrawberryMilk Classic]**
   - **Markdown [StrawberryMilk High Contrast]**

### Theme Coordination

For best results, use these UDL files with the corresponding StrawberryMilk theme:

- **StrawberryMilk Modern UDL** → **StrawberryMilk Modern Theme**
- **StrawberryMilk Classic UDL** → **StrawberryMilk Classic Theme**
- **StrawberryMilk High Contrast UDL** → **StrawberryMilk High Contrast Theme**

## Features

### Syntax Highlighting Support

- **Headers** (H1-H6): Highlighted with accent colors
- **Bold/Italic text**: Styled with appropriate emphasis
- **Code blocks**: Monospace styling with background
- **Links**: URL highlighting
- **Lists**: Bullet and numbered list styling
- **Tables**: Table structure highlighting
- **Comments**: Muted color for better readability

### Markdown Elements

- Inline code: `code`
- Code blocks: ```language
- Bold text: **bold**
- Italic text: *italic*
- Links: [text](url)
- Images: ![alt](url)
- Headers: # Header 1, ## Header 2, etc.
- Lists: - item, 1. item
- Tables: | column | column |

## Customization

### Modifying Colors

To customize the UDL colors:

1. Open the desired UDL file in a text editor
2. Locate the `<Styles>` section
3. Modify the `fgColor` and `bgColor` attributes
4. Save and reload in Notepad++

### Color Format

Colors are specified in BGR format (Blue-Green-Red) without the `#` prefix:

- `E8C5D5` = Light pink
- `141415` = Dark purple-gray
- `FFB3D1` = Bright pink

## Troubleshooting

### UDL Not Appearing

1. Ensure the file is in the correct directory
2. Restart Notepad++ completely
3. Check file permissions

### Colors Not Matching Theme

1. Verify you're using the correct UDL variant
2. Ensure the corresponding StrawberryMilk theme is active
3. Check that Notepad++ is in Dark Mode

### Performance Issues

1. Disable other UDL files if experiencing conflicts
2. Ensure Notepad++ is up to date (v8.1.3+)
3. Check for conflicting plugins

## Development

### Creating New Variants

To create additional StrawberryMilk variants:

1. Copy an existing UDL file
2. Modify the color values in the `<Styles>` section
3. Update the `name` attribute in the `<UserLang>` tag
4. Test with the corresponding theme variant

### Integration with milk++ Palette Editor

The UDL files are designed to work seamlessly with milk++'s palette editor:

1. Use `mkpp` to open the palette editor
2. Modify colors for any StrawberryMilk variant
3. The UDL files will automatically reflect the new colors when the theme is updated

## Support

For issues or feature requests:

- **GitHub Issues**: [milk++ Issues](https://github.com/ryanf-github/mkpp/issues)
- **Documentation**: See main README.md
- **Development Guide**: See Docs/development.md

---

**milk++** | Professional Theme Management for Notepad++
Built for developers who value efficiency and aesthetic
