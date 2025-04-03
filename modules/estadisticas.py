from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def run(db):
    # Print the Panel with title
    console.print(Panel.fit("📈[bold cyan]Estadísticas del Sistema[/bold cyan] 📈"))

    with db.get_cursor() as cur:
        # Execute the SQL query to get database size info
        cur.execute("""
        SELECT current_database() AS base, pg_size_pretty(pg_database_size(current_database()))
        AS tamaño;
        """)

        row = cur.fetchone()  # Fetch the result

        # Create a table to display the data
        table = Table(title="Uso de Base de Datos")
        
        # Add columns for 'Métrica' and 'Valor'
        table.add_column("Métrica")
        table.add_column("Valor")
        
        # Add the values fetched from the query
        for k, v in row.items():
            table.add_row(k, v)
        
        # Print the table
        console.print(table)

# Example of calling the run function
# Assuming `db` is already defined and connected to your PostgreSQL database.
