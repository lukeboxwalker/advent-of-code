from rich.console import Console
from rich.theme import Theme

console = Console(color_system="windows", theme=Theme({"repr.number": "bold green"}))