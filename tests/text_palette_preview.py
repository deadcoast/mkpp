#!/usr/bin/env python3
"""Test the color preview functionality"""

from rich.console import Console
from rich.table import Table

console = Console()

def show_color_preview(colors):
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

# Test with sample colors
test_colors = {
    "bg_primary": "120A14",
    "bg_secondary": "1C1420",
    "bg_surface": "1f181e",
    "text_primary": "E8C5D5",
    "text_secondary": "FFB3D1",
    "text_muted": "D9B8C4",
    "accent_primary": "FF8DBD",
    "accent_secondary": "FF6BA8",
    "accent_light": "FFD6E8"
}

show_color_preview(test_colors)
