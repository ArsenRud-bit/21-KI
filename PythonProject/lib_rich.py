from rich.console import Console
from rich.table import Table


def demo_rich():
    try:
        console = Console()
        table = Table(title="Бібліотеки")
        table.add_column("Назва", style="cyan")
        table.add_column("Призначення", style="green")
        table.add_row("rich", "Гарний вивід")
        table.add_row("tqdm", "Прогрес-бари")
        console.print(table)
    except Exception as e:
        print("Помилка rich:", e)