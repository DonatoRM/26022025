'''
Biblioteca
Autor: Donato Ramos Martínez
'''
# Creamos una nueva biblioteca vacía
biblioteca=[]
# Función para agregar los libros a la biblioteca
def agregar_libro(titulo,autor):
    # diccionario para almacenar los datos del libro
    libro={"titulo":titulo,"autor":autor,"disponible":True}
    biblioteca.append(libro)
    print(f"Libro agregado '{titulo}' de '{autor}' de la biblioteca")
# función para prestar los libros
def prestar_libro(titulo):
    for libro in biblioteca:
        if libro["titulo"]==titulo:
            if libro["disponible"]:
                libro["disponible"]=False
                print(f"libro '{titulo}' prestado.")
            else:
                print(f"libro '{libro}' no está disponible")
            return
        print(f"Libro {libro}' no encontrado en la biblioteca")
# función para devolver el libro
def devolver_libro(titulo):
    for libro in biblioteca:
        if libro["titulo"]==titulo:
            if not libro["disponible"]:
                libro["disponible"]=True
                print(f"Libro {titulo}' devuelto")
            else:
                print(f"Libro '{titulo}' está disponible")
                return
    print(f"Libro '{titulo}' no encontrado en la biblioteca")
# función para mostrar el estado actual en la biblioteca
def mostrar_biblioteca():
    if not biblioteca:
        print("la biblioteca está vacía")
    else:
        print("Estado actual de la biblioteca")
        for libro in biblioteca:
            estado="Disponible" if libro["disponible"] else "Prestado"
            print(f"{libro["titulo"]} de {libro["autor"]} - {estado}")
# menú principal
def menu():
    while True:
        print("\n ---- Gestión de Biblioteca ----")
        print("\n1. Agregar libro")
        print("\n2. Prestar libro")
        print("\n3. Devolver libro")
        print("\n4. Mostrar biblioteca")
        print("\n5. Salir\n")
        opcion=input("seleccione una opción")
        if opcion=="1":
            titulo=input("Ingrese el titulo del libro")
            autor=input("Ingrese el autor del libro")
            agregar_libro(titulo,autor)
        elif opcion=="2":
            titulo=input("Ingrese el titulo del libro a prestar")
            prestar_libro(titulo)
        elif opcion=="3":
            titulo=input("Ingrese el titulo del libro a devolver")
            devolver_libro(titulo)
        elif opcion=="4":
            mostrar_biblioteca()
        elif opcion=="5":
            print("Saliendo del Sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo")
menu()
