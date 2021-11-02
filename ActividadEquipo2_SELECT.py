import sqlite3
from sqlite3 import Error
import sys
try:
    with sqlite3.connect("lafonditachida.db") as conn:
        c = conn.cursor()
        ide = int(input("Ingrese la clave a consultar: "))
        c.execute(f"SELECT * FROM Vendedores WHERE EXISTS (SELECT * FROM Vendedores WHERE {ide} = claveE)")
        registro1 = c.fetchall()
        if registro1:
            c.execute(f"SELECT venta.folioVenta, vendedores.claveE, vendedores.nombre, vendedores.apellidos, venta.fechaventa, venta.monto from Vendedores inner join Venta on Vendedores.claveE = Venta.vendedor WHERE vendedores.claveE = {ide};")
            registros = c.fetchall()
            if len(registros) == 0:
                print("El usuario no tiene ventas")
            else:
                print("Folio","Nombre", "Apellidos", "Fecha","Monto")
                for folio, clave, nombre, apellidos, fecha, monto in registros:
                    if clave == ide:
                        print(folio, nombre, apellidos, fecha, monto)
        else:
            print("La Clave que busca no Existe")
        
except Error as e:
    print(e)
except Exception:
    print(f"Error: {sys.exc_info()[0]}")
finally:
    if conn:
        conn.close()