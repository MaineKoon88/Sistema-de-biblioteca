import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from objetos.libro import Libro
from objetos.socio import Socio
from objetos.prestamo import Prestamo

from datos.libroData import guardarLibro, traerLibros, traerLibro, modificarLibro, borrarLibro
from datos.socioData import guardarSocio, traerSocios, traerSocio, modificarSocio, borrarSocio
from datos.prestamoData import guardarPrestamo, traerPrestamos, devolverPrestamo

def menu():
    while True:
        print("\nMenú principal de operaciones de gestión de biblioteca:")
        print("--- GESTIÓN DE LIBROS ---")
        print("1. Agregar Libro")
        print("2. Ver Libros")
        print("3. Consultar Libro")
        print("4. Modificar Libro")
        print("5. Borrar Libro")
        print("--- GESTIÓN DE SOCIOS ---")
        print("6. Crear Socio")
        print("7. Ver Socios")
        print("8. Consultar Socio")
        print("9. Modificar Socio")
        print("10. Borrar Socio")
        print("--- GESTIÓN DE PRÉSTAMOS ---")
        print("11. Registrar Préstamo")
        print("12. Ver Préstamos")
        print("13. Registrar Devolución")
        print("14. Salir de la aplicación")

        opcion = int(input("\nIngrese una opción (1-14): "))

        if opcion == 1:
            titulo = input("Ingrese el Título: ")
            autor = input("Ingrese el Autor: ")
            anio = int(input("Ingrese el Año: "))
            cantidad = int(input("Ingrese la Cantidad: "))
            lib = Libro(titulo, autor, anio, cantidad)
            guardarLibro(lib.Titulo, lib.Autor, lib.Anio, lib.Cantidad)
            print("Libro guardado !!!")

        elif opcion == 2:
            libros = traerLibros()
            print("\nLista de libros:")
            print("\nId - Título - Autor - Año - Cantidad - Disponibles")
            for lib in libros:
                print(lib[0], " - ", lib[1], " - ", lib[2], " - ", lib[3], " - ", lib[4], " - ", lib[5])

        elif opcion == 3:
            id = int(input("Ingrese el ID del libro: "))
            l = traerLibro(id)
            if l:
                l.verDatos()
            else:
                print("No se encontró el libro.")

        elif opcion == 4:
            id = int(input("Ingrese el ID del libro: "))
            titulo = input("Ingrese el Título: ")
            autor = input("Ingrese el Autor: ")
            anio = int(input("Ingrese el Año: "))
            cantidad = int(input("Ingrese la Cantidad: "))
            lib = Libro(titulo, autor, anio, cantidad)
            modificarLibro(lib.Titulo, lib.Autor, lib.Anio, lib.Cantidad, id)
            print("Libro modificado !!!")
            l = traerLibro(id)
            if l:
                l.verDatos()

        elif opcion == 5:
            libros = traerLibros()
            print("\nLista de libros:")
            print("\nId - Título - Autor - Año - Cantidad - Disponibles")
            for lib in libros:
                print(lib[0], " - ", lib[1], " - ", lib[2], " - ", lib[3], " - ", lib[4], " - ", lib[5])
            id = int(input("Ingrese el ID del libro a borrar: "))
            borrarLibro(id)

        elif opcion == 6:
            nomb = input("Ingrese el Nombre: ")
            apel = input("Ingrese el Apellido: ")
            soc = Socio(nomb, apel)
            guardarSocio(soc.Nombre, soc.Apellido)
            print("Socio guardado !!!")

        elif opcion == 7:
            socios = traerSocios()
            print("\nLista de socios:")
            print("\nId - Nombre - Apellido")
            for soc in socios:
                print(soc[0], " - ", soc[1], " - ", soc[2])

        elif opcion == 8:
            id = int(input("Ingrese el ID del socio: "))
            s = traerSocio(id)
            if s:
                s.verDatos()
            else:
                print("No se encontró el socio.")

        elif opcion == 9:
            id = int(input("Ingrese el ID del socio: "))
            nomb = input("Ingrese el Nombre: ")
            apel = input("Ingrese el Apellido: ")
            soc = Socio(nomb, apel)
            modificarSocio(soc.Nombre, soc.Apellido, id)
            print("Socio modificado !!!")
            s = traerSocio(id)
            if s:
                s.verDatos()

        elif opcion == 10:
            socios = traerSocios()
            print("\nLista de socios:")
            print("\nId - Nombre - Apellido")
            for soc in socios:
                print(soc[0], " - ", soc[1], " - ", soc[2])
            id = int(input("Ingrese el ID del socio a borrar: "))
            borrarSocio(id)

        elif opcion == 11:
            socio_id = int(input("Ingrese el ID del socio: "))
            libro_id = int(input("Ingrese el ID del libro: "))
            fecha = input("Ingrese Fecha del Préstamo (YYYY-MM-DD): ")
            vencimiento = input("Ingrese Fecha de Vencimiento (YYYY-MM-DD): ")
            pres = Prestamo(socio_id, libro_id, fecha, vencimiento)
            guardarPrestamo(pres.SocioId, pres.LibroId, pres.Fecha, pres.Vencimiento)

        elif opcion == 12:
            prestamos = traerPrestamos()
            print("\nLista de préstamos:")
            print("\nId - Socio ID - Libro ID - Fecha Préstamo - Vencimiento - Devolución")
            for p in prestamos:
                dev = p[5] if p[5] else "Pendiente"
                print(p[0], " - ", p[1], " - ", p[2], " - ", p[3], " - ", p[4], " - ", dev)

        elif opcion == 13:
            id_pres = int(input("Ingrese el ID del préstamo a devolver: "))
            fecha_dev = input("Ingrese Fecha de Devolución (YYYY-MM-DD): ")
            devolverPrestamo(id_pres, fecha_dev)

        elif opcion == 14:
            print("\nSaliendo de la aplicación")
            break
        else:
            print("ERROR !!! no existe la opción ingresada...")

menu()
