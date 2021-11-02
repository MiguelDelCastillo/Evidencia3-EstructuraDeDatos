import sys
import sqlite3
from sqlite3 import Error

try:
    with sqlite3.connect("lafonditachida.db") as conn:
        mi_cursor = conn.cursor()
        mi_cursor.execute("INSERT INTO Vendedores VALUES(15,'Miguel Angel','Luna');")
#         mi_cursor.execute("INSERT INTO Vendedores VALUES(10,'Miguel','Del Castillo');")
#         print("REGISTRO GUARDADO EXITOSAMENTE")
#         mi_cursor.execute("INSERT INTO Vendedores VALUES(11,'Francisco','Ruiz');")
#         print("REGISTRO GUARDADO EXITOSAMENTE")
#         mi_cursor.execute("INSERT INTO Vendedores VALUES(12,'Claudia','Elizabeth');")
#         print("REGISTRO GUARDADO EXITOSAMENTE")
#         mi_cursor.execute("INSERT INTO Vendedores VALUES(13,'Juan','Garza');")
#         print("REGISTRO GUARDADO EXITOSAMENTE")
#         mi_cursor.execute("INSERT INTO Vendedores VALUES(14,'Paola','Cruz');")
#         print("REGISTRO GUARDADO EXITOSAMENTE")
#         mi_cursor.execute("INSERT INTO Venta VALUES(100,'10-11-2021',100,10);")
#         print("REGISTRO GUARDADO EXITOSAMENTE")
#         mi_cursor.execute("INSERT INTO Venta VALUES(101,'10-11-2021',150,11);")
#         print("REGISTRO GUARDADO EXITOSAMENTE")
#         mi_cursor.execute("INSERT INTO Venta VALUES(102,'11-11-2021',250,12);")
#         print("REGISTRO GUARDADO EXITOSAMENTE")
#         mi_cursor.execute("INSERT INTO Venta VALUES(103,'11-11-2021',80,13);")
#         print("REGISTRO GUARDADO EXITOSAMENTE")
#         mi_cursor.execute("INSERT INTO Venta VALUES(104,'12-11-2021',170,14);")
#         print("REGISTRO GUARDADO EXITOSAMENTE")
#         mi_cursor.execute("INSERT INTO Venta VALUES(105,'12-11-2021',100,10);")
#         print("REGISTRO GUARDADO EXITOSAMENTE")
#         mi_cursor.execute("INSERT INTO Venta VALUES(106,'13-11-2021',250,11);")
#         print("REGISTRO GUARDADO EXITOSAMENTE")
#         mi_cursor.execute("INSERT INTO Venta VALUES(107,'13-11-2021',300,12);")
#         print("REGISTRO GUARDADO EXITOSAMENTE")
#         mi_cursor.execute("INSERT INTO Venta VALUES(108,'14-11-2021',180,13);")
#         print("REGISTRO GUARDADO EXITOSAMENTE")
#         mi_cursor.execute("INSERT INTO Venta VALUES(109,'14-11-2021',50,14);")
#         print("REGISTRO GUARDADO EXITOSAMENTE")
except Error as e:
    print (e)
except Exception:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
finally:
    if conn:
        conn.close()