from idlelib.configdialog import is_int
from operator import index


class Product :
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

def showMenu():
    print("Sistema de inventario")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Salir del programa")

inventario = []

while True:
    showMenu()
    opcion = input("Ingrese una opcion: ")

    if opcion == "6":
        print("Saliendo del programa")
        break

    if opcion == "1":
        try:
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad de productos: "))
            precio = float(input("Ingrese precio del producto: "))
            producto = Product(nombre, cantidad, precio)
            inventario.append(producto)
            print("producto ingresado correctamente")

        except ValueError:
            print("Error: entrada no valida")
    elif opcion == "2":
        try:
            for c in inventario:
                print(f"Nombre: {c.nombre}, Cantidad: {c.cantidad}, Precio: {c.precio}")
        except ValueError:
            print("Error: No se pudo mostrar la informacion")
    elif opcion == "3":
        try:
            nombre = input("Ingrese nombre del producto: ")
            for c in inventario:
                if c.nombre == nombre:
                    print(f"Producto encontrado:\n Nombre: {c.nombre}, Cantidad: {c.cantidad}, Precio: {c.precio}")
        except ValueError:
            print("Error: Error de busqueda")
    elif opcion == "4":
        try:
            nombre = input("Ingrese el nombre del producto: ")
            encontrado = False
            for c in inventario:
                if c.nombre == nombre:
                    c.nombre = input("Ingrese Nuevo nombre: ")
                    c.cantidad = int(input("Ingrese nueva cantidad: "))
                    c.precio = float(input("Ingrese nuevo precio: "))
                    print("Producto modificado correctamente.")
                    encontrado = True
                    break

            if not encontrado:
                print("Producto no encontrado en el inventario.")

        except ValueError:
            print("Error: No se pudo actualizar el producto")

    elif opcion == "5":
        try:
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            for c in inventario:
                if c.nombre == nombre:
                    inventario.remove(c)
                    print("Producto eliminado")
                    break
        except ValueError:
            print("Error: no se pudo eliminar el producto")