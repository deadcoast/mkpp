# Command Reference

## `mkpp`

Launch interactive menu interface.

**Usage:**

```bash
mkpp
```

---

## `mkpp install <file>`

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

## `mkpp path`

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

## `mkpp themes`

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
│ Dracula         │ 24.5 KB      │
│ Nord            │ 18.3 KB      │
│ Monokai         │ 22.1 KB      │
└─────────────────┴──────────────┘
```
