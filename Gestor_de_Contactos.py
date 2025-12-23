"""
Gestor de Contactos 
    - Usa funciones para cada acción
    - Usa listas
    - Usa strings
    - Usa while + menú
    - Nada de diccionarios aún
    - Código claro y ordenado
"""

contacts = []

def add_contact(contacts):
    """
    Agrega un contacto a la lista
    """
    name = input("Nombre: ").strip().lower()
    phone = input("Teléfono: ").strip()
    contact = f"{name} - {phone}"
    contacts.append(contact)
    print("Contacto agregado.")

def show_contacts(contacts):
    """
    Muestra la lista de contactos
    """
    if not contacts:
        print("No hay contactos.")
        return

    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact}")

def search_contact(contacts):
    """
    Busca un contacto
    """
    name = input("Nombre a buscar: ").strip().lower()
    found = False

    for contact in contacts:
        if name in contact:
            print(contact)
            found = True

    if not found:
        print("Contacto no encontrado.")

def delete_contact(contacts):
    """
    Eliminar un contacto
    """
    name = input("Nombre a eliminar: ").strip().lower()

    for contact in contacts:
        if name in contact:
            contacts.remove(contact)
            print("Contacto eliminado.")
            return

    print("Contacto no encontrado.")

while True:
    print("\n--- MENÚ ---")
    print("1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

    option = input("Elige una opción: ")

    if option == "1":
        add_contact(contacts)
    elif option == "2":
        show_contacts(contacts)
    elif option == "3":
        search_contact(contacts)
    elif option == "4":
        delete_contact(contacts)
    elif option == "5":
        print("Saliendo...")
        break
    else:
        print("Opción inválida.")
