from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def run(db):
    console.print(Panel.fit("🔧[bold cyan]Módulo CRUD Básico[/bold cyan] 🔧"))

    with db.get_cursor() as cur:
        # Insertando datos en la tabla categorias
        cur.execute("""
        INSERT INTO categorias (nombre, descripcion) VALUES
        ('Libros', 'Categoría de libros')
        ON CONFLICT DO NOTHING;
        """)

        # Insertando datos en la tabla productos
        cur.execute("""
        INSERT INTO productos (nombre, precio, categoria_id, stock, descripcion) VALUES
        ('Libro Python', 39000, 1, 25, 'Guía práctica de Python')
        ON CONFLICT DO NOTHING;
        """)

        db.conn.commit()

        # Seleccionando todos los productos
        cur.execute("SELECT * FROM productos")
        rows = cur.fetchall()

        # Creando la tabla para mostrar los productos
        table = Table(title="Productos")
        
        # Si las filas son tuplas, obtenemos los nombres de las columnas
        column_names = [desc[0] for desc in cur.description]
        for col in column_names:
            table.add_column(col)

        # Agregando las filas de productos
        for row in rows:
            table.add_row(*[str(v) for v in row])

        # Mostrando la tabla
        console.print(table)
