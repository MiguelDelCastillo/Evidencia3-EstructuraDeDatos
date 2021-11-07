from collections import namedtuple
import csv
import sqlite3
import sys
from sqlite3 import Error

Datos = namedtuple("Ventas",("descripcion", "cantidad_pzas","precio_venta", "fecha"))
lista_ventas = []
diccionario_ventas = {}

folioNuevo = 0
try:
    with open("datosprueba.csv","r", newline = "") as archivo:
        
        lector = csv.reader(archivo)
        next(lector)
        contador = 0
        
        for folio, descripcion, CantidadPzas, PrecioVenta, FechaVenta in lector:
            if contador == 0:
                folioNuevo = int(folio)
                contador =+1 
                
            if int(folio) == folioNuevo:
                ventas = Datos(descripcion,CantidadPzas, PrecioVenta, FechaVenta)
                lista_ventas.append(ventas)   
            else:
                lista_ventas = []
                ventas = Datos(descripcion,CantidadPzas, PrecioVenta, FechaVenta)
                lista_ventas.append(ventas)
                folioNuevo = int(folio)
                contador =-1
                
            diccionario_ventas[int(folio)] = lista_ventas
except Exception:
    print("Primer Diccionario")

while True:
    print("***********************************************")
    print("\tLlantas Michelin")
    print("")
    print("1) Registrar una venta")
    print("2) Busqueda especifica de una venta")
    print("3) Guardar datos a CSV")
    print("4) Busqueda por fecha")
    print("5) Salir")
    print("\nPuede ingresar la opcion mediante \nel teclado numerico")
    respuesta = int(input("Elija una opción: "))
    
    if respuesta == 1:
        lista_ventas = []
        while True:
            folio = int(input('\nIngrese el folio de la venta: '))
            if folio in diccionario_ventas.keys():
                print('Esta clave ya existe, porfavor ingresa otra')
            else:
                fecha_venta = input('Ingrese la fecha de venta: ')
                break
            
        while True:
            # Insercion de datos
            descripcion = input('Ingrese la descripcion de la llanta: ')
            cantidad_pzas = input('Ingrese la cantidad de piezas a comprar: ')
            precio_venta = input('Ingrese el precio unitario de cada pieza: ')
            
            print("-----------------------------------------------------------\n")
            # Lista
            ventas = Datos(descripcion,cantidad_pzas, precio_venta, fecha_venta)
            lista_ventas.append(ventas)
            
            # Diccionario
            diccionario_ventas[folio] = lista_ventas
            
            # Seguir agregando
            respuesta1 = int(input('¿Quieres seguir agregando productos?\n\t 1: Si\n\t 2: No\n\t'))
            
            # En caso de que no quiera seguir agregando
            if (respuesta1 != 1):
                total_ventas = 0
                for items in diccionario_ventas[folio]:
                    total_ventas = (int(items.precio_venta) * int(items.cantidad_pzas)) + total_ventas
                print(f"Total de las ventas: {total_ventas}")
                print(f"El iva aplicable es de: {total_ventas * .16}")
                print(f"El total con iva aplicado es de: {round(total_ventas*1.16, 2)}")
                break
                
    elif respuesta == 2:
        #Insercion de la busqueda
        busqueda = int(input("Ingresa el folio de la venta a buscar: "))
        total_ventas = 0
        #Iteracion de la busqueda
        if busqueda in diccionario_ventas.keys():
            print(f"\nFolio de la venta: {busqueda}")
            print("*"*90)
            print("{0:<10} {1:<20} {2:<20} {3:<20} {4:<20}".format("Folio","Descripcion","Cantidad","Precio Unitario","Fecha"))
            for items in diccionario_ventas[busqueda]:
                print("{0:<10} {1:<20} {2:<20} {3:<20} {4:<20}".format(busqueda,items.descripcion,items.cantidad_pzas,items.precio_venta,items.fecha))
                total_ventas = (int(items.precio_venta) * int(items.cantidad_pzas)) + total_ventas
            print(f"Total de las ventas: {total_ventas}")
            print(f"El iva aplicable es de: {total_ventas * .16}")
            print(f"El total con iva aplicado es de: {round(total_ventas*1.16, 2)}")
            print("**********************************************\n")
        else:
            print("La clave no esta registrada")
            
    elif respuesta == 3:
        
        with open("datosprueba.csv","w",newline="") as archivo:
            total_ventas = 0
            grabador = csv.writer(archivo)
            grabador.writerow(("Folio","Descripcion","CantidadPzas","PrecioVenta","FechaVenta"))
            for datos in diccionario_ventas:
                for items in diccionario_ventas[datos]:
                    grabador.writerows([[datos,items.descripcion,items.cantidad_pzas,items.precio_venta,items.fecha]])
            print("*"*20)
            print(f"\nCargado Exitosamente \n")
            print("*"*20)
    
    elif respuesta == 4:
        busqueda = input('\nIngrese la fecha a buscar: ')
        print("{0:<10} {1:<20} {2:<20} {3:<20} {4:<20}".format("Folio","Descripcion","Cantidad","Precio Unitario","Fecha"))         
        total_ventas = 0
        for datos in diccionario_ventas:
            for items in diccionario_ventas[datos]:
                if items.fecha == busqueda:
                    print("{0:<10} {1:<20} {2:<20} {3:<20} {4:<20}".format(datos,items.descripcion,items.cantidad_pzas,items.precio_venta,items.fecha))
                    total_ventas = (int(items.precio_venta) * int(items.cantidad_pzas)) + total_ventas
        print(f"Total de las ventas: {total_ventas}")
        print(f"El iva aplicable es de: {total_ventas * .16}")
        print(f"El total con iva aplicado es de: {round(total_ventas*1.16, 2)}")

    elif respuesta == 5:
        print("Finalizando")
        break
    
    
    elif respuesta == 7:
    # Opcion oculta al usuario, borrado de datos de la tabla
        try:
            with sqlite3.connect("Evidencia3.db") as conn:
                mi_cursor = conn.cursor()
                mi_cursor.execute("DELETE FROM Venta")
                mi_cursor.execute("DELETE FROM FechaID")
        except Error as e:
            print(e)
        except Exception:
            print(f"Error: {sys.exc_info()[0]}")
        finally:
            if conn:
                conn.close()
# Cargado de datos a sqlite3
try:
    with sqlite3.connect("Evidencia3.db") as conn:
        mi_cursor = conn.cursor()
        for folio in diccionario_ventas:
            cFolio = True
            for items in diccionario_ventas[folio]:
                if cFolio:
                    mi_cursor.execute(f"SELECT * FROM FechaID WHERE folio = ?",(folio,))
                    registro1 = mi_cursor.fetchall()
                    if registro1:
                        print(f"Dato con el folio: {folio}, ya existe")
                        break
                    else:
                        mi_cursor.execute(f"INSERT INTO FechaID VALUES(?, ?);",(folio, items.fecha))
                    cFolio = False
                mi_cursor.execute(f"INSERT INTO Venta VALUES(?, ?, ?, ?);",(folio, items.descripcion, items.cantidad_pzas, items.precio_venta))
except Error as e:
    print(e)
except Exception:
    print(f"Error: {sys.exc_info()[0]}")
finally:
    if conn:
        conn.close()