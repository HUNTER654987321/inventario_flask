import sqlite3

conn = sqlite3.connect("inventario.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    categoria TEXT NOT NULL,
    precio REAL NOT NULL,
    stock INTEGER NOT NULL
)
""")
conn.commit()
conn.close()
