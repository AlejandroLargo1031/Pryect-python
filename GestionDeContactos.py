class Contacts:
    def __init__(self, nombre,telefono):
        self.nombre = nombre
        self.telefono = telefono

def showMenu():
    print("Gestion de Contactos")
    print("1. Agregar Contacto")
    print("2. Mostrar Contacto")
    print("3. Buscar Contacto")
    print("4. Eliminar Contacto")
    print("5. Salir")

contactos = []

while True:
    showMenu()
    opcion = input("Elige una opcion: ")

    if opcion == "5":
        print("Salir del programa")
        break

    if opcion == "1":
        nombre = input("Ingrese el nombre: ")
        telefono = input("ingrese el numero de telefono: ")
        contact = Contacts(nombre, telefono)
        contactos.append(contact)
        print("contacto agregado")
    elif opcion == "2":
        for c in contactos:
            print(f"Nombre: {c.nombre}, Telefono: {c.telefono}")
    elif opcion == "3":
        nombre = input("Ingrese el nombre: ")
        encontrado = False
        for c in contactos:
            if c.nombre == nombre:
                print(f"Nombre: {c.nombre}, Telefono: {c.telefono}")
                encontrado = True
                break
        if not encontrado:
            print("contacto no encontrado")
    elif opcion == "4":
        nombre = input("Ingrese el nombre: ")
        for c in contactos:
            if c.nombre == nombre:
                contactos.remove(c)
                print("Contacto eliminado")
                break
    else:
        print("opcion no valida intentar de nuevo")