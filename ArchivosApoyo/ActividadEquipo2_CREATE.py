import sys
import sqlite3
from sqlite3 import Error

try:
    with sqlite3.connect("lafonditachida.db") as conn:
        mi_cursor = conn.cursor()
        mi_cursor.execute("CREATE TABLE IF NOT EXISTS Vendedores (claveE INTEGER PRIMARY KEY, nombre TEXT NOT NULL, apellidos TEXT NOT NULL);")
        mi_cursor.execute("CREATE TABLE IF NOT EXISTS Venta (folioVenta INTEGER PRIMARY KEY, fechaVenta TEXT NOT NULL, monto INTEGER NOT NULL, vendedor INTEGER NOT NULL, FOREIGN KEY (vendedor) REFERENCES vendedores(claveE));")
        print("Tabla creada exitosamente")
except Error as e:
    print(e)
except Exception:
    print(f"Error: {sys.exc_info()[0]}")
finally:
    if conn:
        conn.close()