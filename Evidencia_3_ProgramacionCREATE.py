import sys
import sqlite3
from sqlite3 import Error

try:
    with sqlite3.connect("Evidencia3.db") as conn:
        mi_cursor = conn.cursor()
        mi_cursor.execute("CREATE TABLE IF NOT EXISTS FechaID (folio INTEGER PRIMARY KEY, fecha TEXT NOT NULL);")
        mi_cursor.execute("CREATE TABLE IF NOT EXISTS Venta (folio INTEGER NOT NULL, descripcion TEXT NOT NULL, canitdad INTEGER NOT NULL, precio INTEGER NOT NULL, FOREIGN KEY (folio) REFERENCES FechaID(folio));")
        print("Tabla creada exitosamente")
except Error as e:
    print(e)
except Exception:
    print(f"Error: {sys.exc_info()[0]}")
finally:
    if conn:
        conn.close()
