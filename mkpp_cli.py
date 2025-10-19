#!/usr/bin/env python3
"""
milk++ (mkpp) - A Notepad++ CLI Theme Injector for Windows
Universal theme installer for ANY Notepad++ theme
"""

import os
import sys
import stat
import shutil
import subprocess
import json
import re
from pathlib import Path
from typing import Optional, List, Dict
import click
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich import box

console = Console()

# Configuration
CONFIG_DIR = Path.home() / ".mkpp"
CONFIG_FILE = CONFIG_DIR / "config.txt"
DEFAULT_THEME_DIR = Path(os.getenv("APPDATA", "")) / "Notepad++" / "themes"
DEFAULT_UDL_DIR = Path(os.getenv("APPDATA", "")) / "Notepad++" / "userDefineLangs"


def ensure_config_dir():
    """Ensure configuration directory exists"""
    CONFIG_DIR.mkdir(exist_ok=True)


def get_source_path() -> Optional[Path]:
    """Get the configured source path"""
    ensure_config_dir()
    if CONFIG_FILE.exists():
        path_str = CONFIG_FILE.read_text().strip()
        if path_str:
            return Path(path_str)
    return None


def set_source_path(path: Path):
    """Set the source path in config"""
    ensure_config_dir()
    CONFIG_FILE.write_text(str(path))


def print_banner():
    """Print the milk++ banner"""
    banner = """
                milk++
           ================
    A Universal Notepad++ Theme Injector
    """
    console.print(Panel(banner, style="bold magenta", box=box.DOUBLE))


def verify_notepad_installation() -> bool:
    """Check if Notepad++ appears to be installed"""
    if not DEFAULT_THEME_DIR.parent.exists():
        console.print("[bold red][WARNING] Notepad++ directory not found![/bold red]")
        console.print(f"[yellow]Expected: {DEFAULT_THEME_DIR.parent}[/yellow]")
        return False
    return True


def ensure_themes_directory():
    """Ensure the themes directory exists"""
    DEFAULT_THEME_DIR.mkdir(parents=True, exist_ok=True)


def ensure_udl_directory():
    """Ensure the UDL directory exists"""
    DEFAULT_UDL_DIR.mkdir(parents=True, exist_ok=True)


def find_theme_files(directory: Path) -> List[Path]:
    """Find all .xml theme files in a directory (excluding .udl.xml files)"""
    if not directory.exists():
        return []
    # Find .xml files but exclude .udl.xml files
    all_xml = directory.glob("*.xml")
    theme_files = [f for f in all_xml if not f.name.endswith('.udl.xml')]
    return sorted(theme_files)


def find_udl_files(directory: Path) -> List[Path]:
    """Find all .udl.xml files in a directory"""
    if not directory.exists():
        return []
    return sorted(directory.glob("*.udl.xml"))


def install_theme(theme_path: Path, custom_name: Optional[str] = None) -> bool:
    """Install a theme file to Notepad++"""
    if not theme_path.exists():
        console.print(f"[bold red][ERROR] Theme file not found: {theme_path}[/bold red]")
        return False

    if theme_path.suffix.lower() != ".xml":
        console.print("[bold red][ERROR] File must be an .xml file[/bold red]")
        return False

    ensure_themes_directory()

    dest_name = custom_name if custom_name else theme_path.name
    if not dest_name.endswith('.xml'):
        dest_name += '.xml'

    dest_path = DEFAULT_THEME_DIR / dest_name

    try:
        shutil.copy2(theme_path, dest_path)
        console.print(f"[bold green][OK] Theme '{dest_name}' installed![/bold green]")
        console.print(f"[cyan]Location: {dest_path}[/cyan]")
        return True
    except Exception as e:
        console.print(f"[bold red][ERROR] Installation failed: {e}[/bold red]")
        return False


def install_udl(udl_path: Path, custom_name: Optional[str] = None) -> bool:
    """Install a UDL file to Notepad++"""
    if not udl_path.exists():
        console.print(f"[bold red][ERROR] UDL file not found: {udl_path}[/bold red]")
        return False

    if not udl_path.name.endswith('.udl.xml'):
        console.print("[bold red][ERROR] File must be a .udl.xml file[/bold red]")
        return False

    ensure_udl_directory()

    dest_name = custom_name if custom_name else udl_path.name
    if not dest_name.endswith('.udl.xml'):
        dest_name += '.udl.xml'

    dest_path = DEFAULT_UDL_DIR / dest_name

    try:
        shutil.copy2(udl_path, dest_path)
        console.print(f"[bold green][OK] UDL '{dest_name}' installed![/bold green]")
        console.print(f"[cyan]Location: {dest_path}[/cyan]")
        return True
    except Exception as e:
        console.print(f"[bold red][ERROR] Installation failed: {e}[/bold red]")
        return False


def clone_git_repo(repo_url: str, dest: Path) -> bool:
    """Clone a git repository"""
    try:
        subprocess.run(
            ["git", "clone", repo_url, str(dest)],
            check=True,
            capture_output=True
        )
        return True
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        console.print("[yellow][WARNING]  Git not installed[/yellow]")
        return False


def remove_readonly(func, path, excinfo):
    """Error handler for Windows readonly file deletion"""
    os.chmod(path, 0o777)
    func(path)


def safe_rmtree(path: Path):
    """Safely remove directory tree, handling Windows permission issues"""
    if not path.exists():
        return

    try:
        shutil.rmtree(path, onerror=remove_readonly)
    except Exception as e:
        console.print(f"[dim]Warning: Could not clean temp files: {e}[/dim]")


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """milk++ - Universal Notepad++ Theme Injector"""
    if ctx.invoked_subcommand is None:
        print_banner()
        show_main_menu()


def show_install_menu():
    """Display all install options submenu"""
    while True:
        console.print("\n[bold cyan]=== All Install Options ===[/bold cyan]\n")

        table = Table(show_header=False, box=box.SIMPLE)
        table.add_column("Option", style="cyan", width=6)
        table.add_column("Description", style="white")

        table.add_row("1", "Install from File")
        table.add_row("2", "Install from Git Repository")
        table.add_row("3", "Scan and Install (Batch)")
        table.add_row("b", "Back to Main Menu")

        console.print(table)

        choice = Prompt.ask(
            "\n[bold yellow]Select option[/bold yellow]",
            choices=["1", "2", "3", "b"],
            default="b"
        )

        if choice == "1":
            install_from_file()
        elif choice == "2":
            install_from_git()
        elif choice == "3":
            install_batch()
        elif choice == "b":
            break


def show_settings_menu():
    """Display settings submenu"""
    while True:
        console.print("\n[bold cyan]=== Settings ===[/bold cyan]\n")

        table = Table(show_header=False, box=box.SIMPLE)
        table.add_column("Option", style="cyan", width=6)
        table.add_column("Description", style="white")

        table.add_row("1", "Show Paths & Configuration")
        table.add_row("2", "Set Source Path")
        table.add_row("b", "Back to Main Menu")

        console.print(table)

        choice = Prompt.ask(
            "\n[bold yellow]Select option[/bold yellow]",
            choices=["1", "2", "b"],
            default="b"
        )

        if choice == "1":
            show_paths()
        elif choice == "2":
            set_path_interactive()
        elif choice == "b":
            break


def show_main_menu():
    """Display interactive main menu"""
    while True:
        console.print("\n[bold cyan]=== Main Menu ===[/bold cyan]\n")

        table = Table(show_header=False, box=box.SIMPLE)
        table.add_column("Option", style="cyan", width=6)
        table.add_column("Description", style="white")

        table.add_row("1", "Scan and Install")
        table.add_row("2", "Install from Git Repository")
        table.add_row("3", "All Install Options")
        table.add_row("4", "View Installed Themes")
        table.add_row("5", "View Installed UDLs")
        table.add_row("6", "Settings")
        table.add_row("7", "Palette Editor")
        table.add_row("q", "Quit")

        console.print(table)

        choice = Prompt.ask(
            "\n[bold yellow]Select option[/bold yellow]",
            choices=["1", "2", "3", "4", "5", "6", "7", "q"],
            default="q"
        )

        if choice == "1":
            install_batch()
        elif choice == "2":
            install_from_git()
        elif choice == "3":
            show_install_menu()
        elif choice == "4":
            list_themes()
        elif choice == "5":
            list_udls()
        elif choice == "6":
            show_settings_menu()
        elif choice == "7":
            show_palette_editor()
        elif choice == "q":
            console.print("\n[bold magenta]Thanks for using milk++![/bold magenta]\n")
            break


def install_from_file():
    """Install theme from a single file"""
    console.print("\n[bold cyan]Install Theme from File[/bold cyan]\n")

    if not verify_notepad_installation():
        Prompt.ask("\nPress Enter to continue")
        return

    file_path = Prompt.ask("[yellow]Enter theme file path (.xml)[/yellow]")
    theme_path = Path(file_path).expanduser().resolve()

    if install_theme(theme_path):
        console.print(
            "\n[yellow]📝 To activate:[/yellow]"
            "\n   1. Restart Notepad++"
            "\n   2. Settings → Style Configurator"
            "\n   3. Select your theme from dropdown"
        )

    Prompt.ask("\nPress Enter to continue")


def install_from_git():
    """Install theme from Git repository"""
    console.print("\n[bold cyan]Install from Git Repository[/bold cyan]\n")

    if not verify_notepad_installation():
        Prompt.ask("\nPress Enter to continue")
        return

    repo_url = Prompt.ask("[yellow]Enter Git repository URL[/yellow]")

    temp_dir = CONFIG_DIR / "temp_repo"
    safe_rmtree(temp_dir)

    console.print("\n[dim]Cloning repository...[/dim]")

    if clone_git_repo(repo_url, temp_dir):
        themes = find_theme_files(temp_dir)
        udls = find_udl_files(temp_dir)

        if not themes and not udls:
            console.print("[yellow][WARNING]  No .xml theme files or .udl.xml files found in repository[/yellow]")
        else:
            # Show found files
            if themes:
                console.print(f"\n[green]Found {len(themes)} theme(s):[/green]\n")
                for i, theme in enumerate(themes, 1):
                    console.print(f"  {i}. {theme.name}")

            if udls:
                console.print(f"\n[green]Found {len(udls)} UDL file(s):[/green]\n")
                for i, udl in enumerate(udls, len(themes) + 1):
                    console.print(f"  {i}. {udl.name}")

            console.print()
            install_all = Confirm.ask("Install all files?", default=True)

            if install_all:
                installed_themes = 0
                installed_udls = 0

                # Install themes
                for theme in themes:
                    if install_theme(theme):
                        installed_themes += 1

                # Install UDL files
                for udl in udls:
                    if install_udl(udl):
                        installed_udls += 1

                # Summary
                if installed_themes > 0:
                    console.print(f"\n[green][OK] Installed {installed_themes}/{len(themes)} themes[/green]")
                if installed_udls > 0:
                    console.print(f"[green][OK] Installed {installed_udls}/{len(udls)} UDL files[/green]")
            else:
                choice = Prompt.ask("Enter file number to install (or 0 to cancel)")
                try:
                    idx = int(choice) - 1
                    if 0 <= idx < len(themes):
                        install_theme(themes[idx])
                    elif len(themes) <= idx < len(themes) + len(udls):
                        udl_idx = idx - len(themes)
                        install_udl(udls[udl_idx])
                except ValueError:
                    console.print("[red]Invalid choice[/red]")

        safe_rmtree(temp_dir)
    else:
        console.print("[bold red][ERROR] Failed to clone repository[/bold red]")

    Prompt.ask("\nPress Enter to continue")


def install_batch():
    """Install all themes and UDL files from source folder"""
    console.print("\n[bold cyan]Batch Install from Folder[/bold cyan]\n")

    if not verify_notepad_installation():
        Prompt.ask("\nPress Enter to continue")
        return

    source_path = get_source_path()
    if source_path:
        console.print(f"[dim]Current source: {source_path}[/dim]")
        use_current = Confirm.ask("Use this folder?", default=True)
        if use_current:
            folder_path = source_path
        else:
            folder_path = Path(Prompt.ask("[yellow]Enter folder path[/yellow]")).expanduser()
    else:
        folder_path = Path(Prompt.ask("[yellow]Enter folder path[/yellow]")).expanduser()

    if not folder_path.exists():
        console.print("[bold red][ERROR] Folder not found[/bold red]")
        Prompt.ask("\nPress Enter to continue")
        return

    # Find both themes and UDL files
    themes = find_theme_files(folder_path)
    udls = find_udl_files(folder_path)

    if not themes and not udls:
        console.print("[yellow][WARNING]  No .xml theme files or .udl.xml files found[/yellow]")
    else:
        # Show found files
        if themes:
            console.print(f"\n[green]Found {len(themes)} theme(s):[/green]\n")
            for theme in themes:
                console.print(f"  • {theme.name}")

        if udls:
            console.print(f"\n[green]Found {len(udls)} UDL file(s):[/green]\n")
            for udl in udls:
                console.print(f"  • {udl.name}")

        console.print()
        if Confirm.ask("Install all?", default=True):
            installed_themes = 0
            installed_udls = 0

            # Install themes
            for theme in themes:
                if install_theme(theme):
                    installed_themes += 1

            # Install UDL files
            for udl in udls:
                if install_udl(udl):
                    installed_udls += 1

            # Summary
            if installed_themes > 0:
                console.print(f"\n[green][OK] Installed {installed_themes}/{len(themes)} themes[/green]")
            if installed_udls > 0:
                console.print(f"[green][OK] Installed {installed_udls}/{len(udls)} UDL files[/green]")

    Prompt.ask("\nPress Enter to continue")


def list_themes():
    """List installed themes"""
    console.print("\n[bold cyan]Installed Themes[/bold cyan]\n")

    if not DEFAULT_THEME_DIR.exists():
        console.print("[yellow][WARNING]  Themes directory not found[/yellow]")
        console.print(f"[dim]{DEFAULT_THEME_DIR}[/dim]")
        Prompt.ask("\nPress Enter to continue")
        return

    themes = find_theme_files(DEFAULT_THEME_DIR)

    if not themes:
        console.print("[yellow]No themes installed[/yellow]")
    else:
        table = Table(title="[FOLDER] Installed Themes", box=box.ROUNDED)
        table.add_column("Theme Name", style="cyan")
        table.add_column("File Size", style="white")

        for theme in themes:
            size = theme.stat().st_size
            size_str = f"{size:,} bytes" if size < 1024 else f"{size/1024:.1f} KB"
            table.add_row(theme.stem, size_str)

        console.print(table)

    Prompt.ask("\nPress Enter to continue")


def list_udls():
    """List installed UDL files"""
    console.print("\n[bold cyan]Installed UDL Files[/bold cyan]\n")

    if not DEFAULT_UDL_DIR.exists():
        console.print("[yellow][WARNING]  UDL directory not found[/yellow]")
        console.print(f"[dim]{DEFAULT_UDL_DIR}[/dim]")
        Prompt.ask("\nPress Enter to continue")
        return

    udls = find_udl_files(DEFAULT_UDL_DIR)

    if not udls:
        console.print("[yellow]No UDL files installed[/yellow]")
    else:
        table = Table(title="[FOLDER] Installed UDL Files", box=box.ROUNDED)
        table.add_column("UDL Name", style="cyan")
        table.add_column("File Size", style="white")

        for udl in udls:
            size = udl.stat().st_size
            size_str = f"{size:,} bytes" if size < 1024 else f"{size/1024:.1f} KB"
            table.add_row(udl.stem, size_str)

        console.print(table)

    Prompt.ask("\nPress Enter to continue")


def show_paths():
    """Show current paths and configuration"""
    console.print("\n[bold cyan]Paths & Configuration[/bold cyan]\n")

    table = Table(box=box.ROUNDED, show_header=False)
    table.add_column("Setting", style="yellow", width=25)
    table.add_column("Value", style="white")

    table.add_row("Themes Directory", str(DEFAULT_THEME_DIR))
    table.add_row("Themes Exists?", "[OK] Yes" if DEFAULT_THEME_DIR.exists() else "[ERROR] No")

    table.add_row("UDL Directory", str(DEFAULT_UDL_DIR))
    table.add_row("UDL Exists?", "[OK] Yes" if DEFAULT_UDL_DIR.exists() else "[ERROR] No")

    source_path = get_source_path()
    table.add_row(
        "Source Path",
        str(source_path) if source_path else "[dim]Not set[/dim]"
    )

    table.add_row("Config File", str(CONFIG_FILE))

    console.print(table)
    Prompt.ask("\nPress Enter to continue")


def set_path_interactive():
    """Set source path interactively"""
    console.print("\n[bold cyan]Set Source Path[/bold cyan]\n")
    console.print("[dim]Set default folder for batch theme installation[/dim]\n")

    current = get_source_path()
    if current:
        console.print(f"[yellow]Current:[/yellow] {current}\n")

    new_path = Prompt.ask("[yellow]Enter path[/yellow]")
    path = Path(new_path).expanduser().resolve()

    if not path.exists():
        if Confirm.ask("Path doesn't exist. Create it?", default=False):
            try:
                path.mkdir(parents=True, exist_ok=True)
            except Exception as e:
                console.print(f"[bold red][ERROR] Failed: {e}[/bold red]")
                Prompt.ask("\nPress Enter to continue")
                return
        else:
            Prompt.ask("\nPress Enter to continue")
            return

    set_source_path(path)
    console.print(f"[bold green][OK] Source path set: {path}[/bold green]")
    Prompt.ask("\nPress Enter to continue")


@cli.command()
@click.option("--setpath", type=click.Path(), help="Set source path")
def path(setpath):
    """Show or set the source path"""
    print_banner()

    if setpath:
        path_obj = Path(setpath).expanduser().resolve()
        if not path_obj.exists():
            console.print(f"[bold red][ERROR] Path not found: {path_obj}[/bold red]")
            sys.exit(1)

        set_source_path(path_obj)
        console.print(f"[bold green][OK] Source path set: {path_obj}[/bold green]")
    else:
        console.print("\n[bold cyan]Configuration[/bold cyan]\n")
        console.print(f"[yellow]Themes Directory:[/yellow] {DEFAULT_THEME_DIR}")
        console.print(f"[yellow]Themes Exists:[/yellow] {'[OK]' if DEFAULT_THEME_DIR.exists() else '[ERROR]'}")

        console.print(f"\n[yellow]UDL Directory:[/yellow] {DEFAULT_UDL_DIR}")
        console.print(f"[yellow]UDL Exists:[/yellow] {'[OK]' if DEFAULT_UDL_DIR.exists() else '[ERROR]'}")

        source_path = get_source_path()
        if source_path:
            console.print(f"\n[yellow]Source Path:[/yellow] {source_path}")
        else:
            console.print("\n[dim]No source path set[/dim]")


@cli.command()
@click.argument("theme_file", type=click.Path(exists=True))
@click.option("--name", help="Custom name for theme")
def install(theme_file, name):
    """Install a theme file"""
    print_banner()
    theme_path = Path(theme_file)

    if not verify_notepad_installation():
        sys.exit(1)

    if install_theme(theme_path, name):
        console.print("\n[dim]Restart Notepad++ and check Style Configurator[/dim]")


@cli.command()
@click.argument("udl_file", type=click.Path(exists=True))
@click.option("--name", help="Custom name for UDL")
def install_udl_cmd(udl_file, name):
    """Install a UDL file"""
    print_banner()
    udl_path = Path(udl_file)

    if not verify_notepad_installation():
        sys.exit(1)

    if install_udl(udl_path, name):
        console.print("\n[dim]Restart Notepad++ and check Language menu[/dim]")


def load_palette_config():
    """Load palette configuration from JSON file"""
    config_path = Path(__file__).parent / "Themes" / "color_config.json"

    if not config_path.exists():
        console.print(f"[red]Error: color_config.json not found at {config_path}[/red]")
        return {}

    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        console.print(f"[red]Error loading palette config: {e}[/red]")
        return {}

def save_palette_config(config: Dict):
    """Save palette configuration to JSON file"""
    config_path = Path(__file__).parent / "Themes" / "color_config.json"

    try:
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)
        return True
    except Exception as e:
        console.print(f"[red]Error saving palette config: {e}[/red]")
        return False

def update_theme_xml(version: str, xml_file: str = "StrawberryMilk.xml"):
    """Update XML theme file with colors from specified version"""
    config = load_palette_config()

    if version not in config:
        console.print(f"[red]Error: Version '{version}' not found[/red]")
        return False

    colors = config[version]["colors"]
    xml_path = Path(__file__).parent / "Themes" / xml_file

    if not xml_path.exists():
        console.print(f"[red]Error: {xml_file} not found[/red]")
        return False

    # Read XML content
    with open(xml_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply color replacements
    replacements = [
        (r'bgColor="120A14"', f'bgColor="{colors["bg_primary"]}"'),
        (r'bgColor="1C1420"', f'bgColor="{colors["bg_secondary"]}"'),
        (r'bgColor="1f181e"', f'bgColor="{colors["bg_surface"]}"'),
        (r'bgColor="3D2F42"', f'bgColor="{colors["bg_surface_alt"]}"'),
        (r'fgColor="E8C5D5"', f'fgColor="{colors["text_primary"]}"'),
        (r'fgColor="FFB3D1"', f'fgColor="{colors["text_secondary"]}"'),
        (r'fgColor="D9B8C4"', f'fgColor="{colors["text_muted"]}"'),
        (r'fgColor="BB889F"', f'fgColor="{colors["text_muted"]}"'),
        (r'fgColor="FF8DBD"', f'fgColor="{colors["accent_primary"]}"'),
        (r'fgColor="FF6BA8"', f'fgColor="{colors["accent_secondary"]}"'),
        (r'fgColor="FFD6E8"', f'fgColor="{colors["accent_light"]}"'),
    ]

    # Apply all replacements
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)

    # Write updated content to source file
    with open(xml_path, 'w', encoding='utf-8') as f:
        f.write(content)

    console.print(f"[green]Updated {xml_file} with {version} colors[/green]")

    # Check if theme is already installed and update it
    installed_path = DEFAULT_THEME_DIR / xml_file
    if installed_path.exists():
        # Copy updated theme to Notepad++ themes directory
        try:
            shutil.copy2(xml_path, installed_path)
            console.print(f"[green]Updated installed theme in Notepad++[/green]")
            console.print("[yellow]Restart Notepad++ to see the changes[/yellow]")
        except Exception as e:
            console.print(f"[red]Warning: Could not update installed theme: {e}[/red]")
            console.print("[dim]You may need to reinstall the theme manually[/dim]")

    return True

def show_color_preview(colors: Dict[str, str]):
    """Display visual color preview"""
    console.print("\n[bold cyan]Color Preview:[/bold cyan]")

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Element", style="cyan", width=20)
    table.add_column("Color", style="white", width=10)
    table.add_column("Preview", style="white", width=15)

    color_map = {
        "bg_primary": "Background",
        "bg_secondary": "Current Line",
        "bg_surface": "Selected Text",
        "text_primary": "Default Text",
        "text_secondary": "Keywords",
        "text_muted": "Comments",
        "accent_primary": "Syntax",
        "accent_secondary": "Numbers",
        "accent_light": "Strings"
    }

    for key, name in color_map.items():
        if key in colors:
            color = colors[key]
            preview = f"[#{color}]######[/]"
            table.add_row(name, f"#{color}", preview)

    console.print(table)

def show_palette_editor():
    """Display palette editor menu"""
    while True:
        config = load_palette_config()

        console.print("\n[bold cyan]=== Palette Editor ===[/bold cyan]\n")

        table = Table(show_header=False, box=box.SIMPLE)
        table.add_column("Option", style="cyan", width=6)
        table.add_column("Description", style="white")

        table.add_row("1", "Edit StrawberryMilk Classic (ver_001)")
        table.add_row("2", "Edit StrawberryMilk Modern (ver_002)")
        table.add_row("3", "Edit StrawberryMilk High Contrast (ver_003)")
        table.add_row("4", "Preview All Palettes")
        table.add_row("5", "Apply Theme to XML")
        table.add_row("b", "Back to Main Menu")

        console.print(table)

        choice = Prompt.ask(
            "\n[bold yellow]Select option[/bold yellow]",
            choices=["1", "2", "3", "4", "5", "b"],
            default="b"
        )

        if choice == "1":
            edit_palette("ver_001", config)
        elif choice == "2":
            edit_palette("ver_002", config)
        elif choice == "3":
            edit_palette("ver_003", config)
        elif choice == "4":
            preview_all_palettes(config)
        elif choice == "5":
            apply_theme_to_xml()
        elif choice == "b":
            break

def edit_palette(version: str, config: Dict):
    """Edit a specific palette"""
    if version not in config:
        console.print(f"[red]Error: Version '{version}' not found[/red]")
        return

    palette = config[version]
    colors = palette["colors"]

    console.print(f"\n[bold cyan]Editing {palette['name']}[/bold cyan]")
    console.print(f"[dim]{palette['description']}[/dim]\n")

    # Show current colors
    show_color_preview(colors)

    while True:
        console.print(f"\n[bold yellow]Edit {version} Colors:[/bold yellow]")

        table = Table(show_header=False, box=box.SIMPLE)
        table.add_column("Option", style="cyan", width=6)
        table.add_column("Description", style="white")

        table.add_row("1", "Edit Background Colors")
        table.add_row("2", "Edit Text Colors")
        table.add_row("3", "Edit Accent Colors")
        table.add_row("4", "Preview Changes")
        table.add_row("5", "Save Palette")
        table.add_row("b", "Back to Palette Editor")

        console.print(table)

        choice = Prompt.ask(
            "\n[bold yellow]Select option[/bold yellow]",
            choices=["1", "2", "3", "4", "5", "b"],
            default="b"
        )

        if choice == "1":
            edit_background_colors(colors)
        elif choice == "2":
            edit_text_colors(colors)
        elif choice == "3":
            edit_accent_colors(colors)
        elif choice == "4":
            show_color_preview(colors)
        elif choice == "5":
            if save_palette_config(config):
                console.print(f"[green]Saved {version} palette[/green]")
        elif choice == "b":
            break

def edit_background_colors(colors: Dict):
    """Edit background colors"""
    console.print("\n[bold cyan]Background Colors:[/bold cyan]")

    bg_colors = {
        "bg_primary": "Primary Background",
        "bg_secondary": "Secondary Background",
        "bg_surface": "Surface Background",
        "bg_surface_alt": "Alternative Surface"
    }

    for key, name in bg_colors.items():
        current = colors.get(key, "000000")
        console.print(f"\n[cyan]{name}:[/cyan] #{current}")

        new_color = Prompt.ask(
            f"Enter new color (hex, no #)",
            default=current
        )

        if new_color and len(new_color) == 6:
            colors[key] = new_color.upper()

def edit_text_colors(colors: Dict):
    """Edit text colors"""
    console.print("\n[bold cyan]Text Colors:[/bold cyan]")

    text_colors = {
        "text_primary": "Primary Text",
        "text_secondary": "Secondary Text",
        "text_muted": "Muted Text"
    }

    for key, name in text_colors.items():
        current = colors.get(key, "000000")
        console.print(f"\n[cyan]{name}:[/cyan] #{current}")

        new_color = Prompt.ask(
            f"Enter new color (hex, no #)",
            default=current
        )

        if new_color and len(new_color) == 6:
            colors[key] = new_color.upper()

def edit_accent_colors(colors: Dict):
    """Edit accent colors"""
    console.print("\n[bold cyan]Accent Colors:[/bold cyan]")

    accent_colors = {
        "accent_primary": "Primary Accent",
        "accent_secondary": "Secondary Accent",
        "accent_light": "Light Accent"
    }

    for key, name in accent_colors.items():
        current = colors.get(key, "000000")
        console.print(f"\n[cyan]{name}:[/cyan] #{current}")

        new_color = Prompt.ask(
            f"Enter new color (hex, no #)",
            default=current
        )

        if new_color and len(new_color) == 6:
            colors[key] = new_color.upper()

def preview_all_palettes(config: Dict):
    """Preview all available palettes"""
    console.print("\n[bold cyan]All Available Palettes:[/bold cyan]\n")

    for version, palette in config.items():
        console.print(f"[bold magenta]{palette['name']} ({version})[/bold magenta]")
        console.print(f"[dim]{palette['description']}[/dim]")
        show_color_preview(palette["colors"])
        console.print()

def apply_theme_to_xml():
    """Apply a palette to the XML theme file"""
    config = load_palette_config()

    console.print("\n[bold cyan]Apply Theme to XML:[/bold cyan]\n")

    table = Table(show_header=False, box=box.SIMPLE)
    table.add_column("Option", style="cyan", width=6)
    table.add_column("Description", style="white")

    # Create numbered options for better UX
    version_list = list(config.keys())
    for i, version in enumerate(version_list, 1):
        palette = config[version]
        table.add_row(str(i), palette["name"])

    table.add_row("b", "Back to Palette Editor")

    console.print(table)

    # Create choices list with numbers
    choices = [str(i) for i in range(1, len(version_list) + 1)] + ["b"]

    choice = Prompt.ask(
        "\n[bold yellow]Select palette to apply[/bold yellow]",
        choices=choices,
        default="b"
    )

    if choice != "b" and choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(version_list):
            version = version_list[index]
            if update_theme_xml(version):
                console.print(f"\n[green]Successfully applied {config[version]['name']} to StrawberryMilk.xml[/green]")
                console.print("[dim]If not already installed, use: mkpp install Themes/StrawberryMilk.xml[/dim]")

@cli.command()
def themes():
    """List installed themes"""
    print_banner()
    list_themes()


@cli.command()
def udls():
    """List installed UDL files"""
    print_banner()
    list_udls()


@cli.command()
@click.argument("directory", type=click.Path(exists=True))
def scan(directory):
    """Scan and install all themes and UDL files from a directory"""
    print_banner()
    folder_path = Path(directory).expanduser().resolve()

    if not verify_notepad_installation():
        sys.exit(1)

    # Find both themes and UDL files
    themes = find_theme_files(folder_path)
    udls = find_udl_files(folder_path)

    if not themes and not udls:
        console.print("[yellow][WARNING]  No .xml theme files or .udl.xml files found[/yellow]")
        return

    # Show found files
    if themes:
        console.print(f"\n[green]Found {len(themes)} theme(s):[/green]\n")
        for theme in themes:
            console.print(f"  • {theme.name}")

    if udls:
        console.print(f"\n[green]Found {len(udls)} UDL file(s):[/green]\n")
        for udl in udls:
            console.print(f"  • {udl.name}")

    console.print()
    if Confirm.ask("Install all?", default=True):
        installed_themes = 0
        installed_udls = 0

        # Install themes
        for theme in themes:
            if install_theme(theme):
                installed_themes += 1

        # Install UDL files
        for udl in udls:
            if install_udl(udl):
                installed_udls += 1

        # Summary
        if installed_themes > 0:
            console.print(f"\n[green][OK] Installed {installed_themes}/{len(themes)} themes[/green]")
        if installed_udls > 0:
            console.print(f"[green][OK] Installed {installed_udls}/{len(udls)} UDL files[/green]")


if __name__ == "__main__":
    cli()
