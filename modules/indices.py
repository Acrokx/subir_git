from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import psycopg2  # Assuming you're using psycopg2 for PostgreSQL

console = Console()

def run(db):
    # Print the header panel
    console.print(Panel.fit("📌[bold cyan]Gestión de Índices[/bold cyan] 📌"))
    
    try:
        # Create index on 'productos' table for 'precio' column
        with db.get_cursor() as cur:
            cur.execute("""
            CREATE INDEX IF NOT EXISTS idx_productos_precio ON productos(precio);
            """)
            db.conn.commit()
            
            # Fetch existing indexes on 'productos' table
            cur.execute("SELECT * FROM pg_indexes WHERE tablename = 'productos'")
            rows = cur.fetchall()

            # Check if rows exist and process them
            if rows:
                # Create the table for displaying indexes
                table = Table(title="Índices de productos")
                
                # Add columns dynamically based on the first row's keys
                for col in rows[0].keys():
                    table.add_column(col)

                # Add rows to the table
                for row in rows:
                    table.add_row(*[str(v) for v in row.values()])

                # Print the table to the console
                console.print(table)
            else:
                console.print("[bold red]No se encontraron índices en la tabla 'productos'.[/bold red]")
    
    except Exception as e:
        # In case of an error, print the error message
        console.print(f"[bold red]Error: {str(e)}[/bold red]")

