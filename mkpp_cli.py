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
from pathlib import Path
from typing import Optional, List
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
                ░██░██ ░██                       
                   ░██ ░██                       
░█████████████  ░██░██ ░██    ░██  ░██     ░██   
░██   ░██   ░██ ░██░██ ░██   ░██ ░██████ ░██████ 
░██   ░██   ░██ ░██░██ ░███████    ░██     ░██   
░██   ░██   ░██ ░██░██ ░██   ░██                 
░██   ░██   ░██ ░██░██ ░██    ░██     (mkpp)             
                                                                                                                                          
A Universal Notepad++ Theme Injector
    """
    console.print(Panel(banner, style="bold magenta", box=box.DOUBLE))


def verify_notepad_installation() -> bool:
    """Check if Notepad++ appears to be installed"""
    if not DEFAULT_THEME_DIR.parent.exists():
        console.print("[bold red]⚠️  Notepad++ directory not found![/bold red]")
        console.print(f"[yellow]Expected: {DEFAULT_THEME_DIR.parent}[/yellow]")
        return False
    return True


def ensure_themes_directory():
    """Ensure the themes directory exists"""
    DEFAULT_THEME_DIR.mkdir(parents=True, exist_ok=True)


def find_theme_files(directory: Path) -> List[Path]:
    """Find all .xml theme files in a directory"""
    if not directory.exists():
        return []
    return sorted(directory.glob("*.xml"))


def install_theme(theme_path: Path, custom_name: Optional[str] = None) -> bool:
    """Install a theme file to Notepad++"""
    if not theme_path.exists():
        console.print(f"[bold red]❌ Theme file not found: {theme_path}[/bold red]")
        return False

    if theme_path.suffix.lower() != ".xml":
        console.print("[bold red]❌ File must be an .xml file[/bold red]")
        return False

    ensure_themes_directory()
    
    dest_name = custom_name if custom_name else theme_path.name
    if not dest_name.endswith('.xml'):
        dest_name += '.xml'
    
    dest_path = DEFAULT_THEME_DIR / dest_name

    try:
        shutil.copy2(theme_path, dest_path)
        console.print(f"[bold green]✅ Theme '{dest_name}' installed![/bold green]")
        console.print(f"[cyan]Location: {dest_path}[/cyan]")
        return True
    except Exception as e:
        console.print(f"[bold red]❌ Installation failed: {e}[/bold red]")
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
        console.print("[yellow]⚠️  Git not installed[/yellow]")
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
        console.print("\n[bold cyan]═══ All Install Options ═══[/bold cyan]\n")
        
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
        console.print("\n[bold cyan]═══ Settings ═══[/bold cyan]\n")
        
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
        console.print("\n[bold cyan]═══ Main Menu ═══[/bold cyan]\n")
        
        table = Table(show_header=False, box=box.SIMPLE)
        table.add_column("Option", style="cyan", width=6)
        table.add_column("Description", style="white")
        
        table.add_row("1", "Scan and Install")
        table.add_row("2", "Install from Git Repository")
        table.add_row("3", "All Install Options")
        table.add_row("4", "View Installed Themes")
        table.add_row("5", "Settings")
        table.add_row("q", "Quit")
        
        console.print(table)
        
        choice = Prompt.ask(
            "\n[bold yellow]Select option[/bold yellow]",
            choices=["1", "2", "3", "4", "5", "q"],
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
            show_settings_menu()
        elif choice == "q":
            console.print("\n[bold magenta]Thanks for using milk++! 🥛[/bold magenta]\n")
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
        
        if not themes:
            console.print("[yellow]⚠️  No .xml theme files found in repository[/yellow]")
        else:
            console.print(f"\n[green]Found {len(themes)} theme(s):[/green]\n")
            
            for i, theme in enumerate(themes, 1):
                console.print(f"  {i}. {theme.name}")
            
            console.print()
            install_all = Confirm.ask("Install all themes?", default=True)
            
            if install_all:
                installed = 0
                for theme in themes:
                    if install_theme(theme):
                        installed += 1
                console.print(f"\n[green]✅ Installed {installed}/{len(themes)} themes[/green]")
            else:
                choice = Prompt.ask("Enter theme number to install (or 0 to cancel)")
                try:
                    idx = int(choice) - 1
                    if 0 <= idx < len(themes):
                        install_theme(themes[idx])
                except ValueError:
                    console.print("[red]Invalid choice[/red]")
        
        safe_rmtree(temp_dir)
    else:
        console.print("[bold red]❌ Failed to clone repository[/bold red]")
    
    Prompt.ask("\nPress Enter to continue")


def install_batch():
    """Install all themes from source folder"""
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
        console.print("[bold red]❌ Folder not found[/bold red]")
        Prompt.ask("\nPress Enter to continue")
        return
    
    themes = find_theme_files(folder_path)
    
    if not themes:
        console.print("[yellow]⚠️  No .xml theme files found[/yellow]")
    else:
        console.print(f"\n[green]Found {len(themes)} theme(s):[/green]\n")
        for theme in themes:
            console.print(f"  • {theme.name}")
        
        console.print()
        if Confirm.ask("Install all?", default=True):
            installed = 0
            for theme in themes:
                if install_theme(theme):
                    installed += 1
            console.print(f"\n[green]✅ Installed {installed}/{len(themes)} themes[/green]")
    
    Prompt.ask("\nPress Enter to continue")


def list_themes():
    """List installed themes"""
    console.print("\n[bold cyan]Installed Themes[/bold cyan]\n")
    
    if not DEFAULT_THEME_DIR.exists():
        console.print("[yellow]⚠️  Themes directory not found[/yellow]")
        console.print(f"[dim]{DEFAULT_THEME_DIR}[/dim]")
        Prompt.ask("\nPress Enter to continue")
        return
    
    themes = find_theme_files(DEFAULT_THEME_DIR)
    
    if not themes:
        console.print("[yellow]No themes installed[/yellow]")
    else:
        table = Table(title="📁 Installed Themes", box=box.ROUNDED)
        table.add_column("Theme Name", style="cyan")
        table.add_column("File Size", style="white")
        
        for theme in themes:
            size = theme.stat().st_size
            size_str = f"{size:,} bytes" if size < 1024 else f"{size/1024:.1f} KB"
            table.add_row(theme.stem, size_str)
        
        console.print(table)
    
    Prompt.ask("\nPress Enter to continue")


def show_paths():
    """Show current paths and configuration"""
    console.print("\n[bold cyan]Paths & Configuration[/bold cyan]\n")
    
    table = Table(box=box.ROUNDED, show_header=False)
    table.add_column("Setting", style="yellow", width=25)
    table.add_column("Value", style="white")
    
    table.add_row("Themes Directory", str(DEFAULT_THEME_DIR))
    table.add_row("Exists?", "✅ Yes" if DEFAULT_THEME_DIR.exists() else "❌ No")
    
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
                console.print(f"[bold red]❌ Failed: {e}[/bold red]")
                Prompt.ask("\nPress Enter to continue")
                return
        else:
            Prompt.ask("\nPress Enter to continue")
            return
    
    set_source_path(path)
    console.print(f"[bold green]✅ Source path set: {path}[/bold green]")
    Prompt.ask("\nPress Enter to continue")


@cli.command()
@click.option("--setpath", type=click.Path(), help="Set source path")
def path(setpath):
    """Show or set the source path"""
    print_banner()
    
    if setpath:
        path_obj = Path(setpath).expanduser().resolve()
        if not path_obj.exists():
            console.print(f"[bold red]❌ Path not found: {path_obj}[/bold red]")
            sys.exit(1)
        
        set_source_path(path_obj)
        console.print(f"[bold green]✅ Source path set: {path_obj}[/bold green]")
    else:
        console.print("\n[bold cyan]Configuration[/bold cyan]\n")
        console.print(f"[yellow]Themes Directory:[/yellow] {DEFAULT_THEME_DIR}")
        console.print(f"[yellow]Exists:[/yellow] {'✅' if DEFAULT_THEME_DIR.exists() else '❌'}")
        
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
def themes():
    """List installed themes"""
    print_banner()
    list_themes()


if __name__ == "__main__":
    cli()