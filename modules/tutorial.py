from rich.console import Console
from rich.panel import Panel

console = Console()

def run(db):
    # Displaying a header with rich
    console.print(Panel.fit("📘[bold cyan]Tutorial SQL: Comandos DDL y DML[/bold cyan] 📘"))
    
    try:
        with db.get_cursor() as cur:
            # Create 'categorias' table if not exists
            cur.execute("""
            CREATE TABLE IF NOT EXISTS categorias (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(100),
                descripcion TEXT
            );
            """)
            
            # Create 'productos' table if not exists
            cur.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(100),
                precio DECIMAL(10,2),
                categoria_id INTEGER REFERENCES categorias(id),
                stock INTEGER,
                descripcion TEXT
            );
            """)
            
            # Commit the changes
            db.conn.commit()

            # Success message
            console.print("[green]✓ Tablas creadas correctamente[/green]")
    
    except Exception as e:
        # Handle any errors during table creation
        console.print(f"[bold red]Error al crear las tablas: {str(e)}[/bold red]")

