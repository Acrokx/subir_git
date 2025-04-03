from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def run(db):
    console.print(Panel.fit("📊[bold cyan]Consultas y Agregaciones[/bold cyan] 📊"))
    
    # Execute the query
    with db.get_cursor() as cur:
        cur.execute("""
            SELECT categoria_id, COUNT(*) AS total, AVG(precio) AS promedio
            FROM productos
            GROUP BY categoria_id
        """)
        rows = cur.fetchall()
    
    # Create the table and add column names
    table = Table(title="Resumen por Categoría")
    
    if rows:
        # Add columns dynamically based on keys from the first row (assuming rows are dict-like)
        for col in rows[0].keys():
            table.add_column(col)

        # Add rows to the table
        for row in rows:
            table.add_row(*[str(v) for v in row.values()])
    
        # Print the table
        console.print(table)
    else:
        console.print("No data found", style="bold red")
