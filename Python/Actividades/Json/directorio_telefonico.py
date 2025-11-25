import json
import os

ARCHIVO_JSON = "directorio_telefonico.json"

def cargar_contactos():
    if os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    else:
        return {"contactos": []}

def guardar_contactos(datos):
    with open(ARCHIVO_JSON, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)

def inicializar_contactos():
    contactos_iniciales = {
        "contactos": [
            {"nombre": "Juan", "apellidos": "Pérez", "telefono": "612345678", "correo": "juan@example.com"},
            {"nombre": "Laura", "apellidos": "Gómez", "telefono": "623456789", "correo": "laura@example.com"},
            {"nombre": "Carlos", "apellidos": "Martínez", "telefono": "634567890", "correo": "carlos@example.com"},
            {"nombre": "Ana", "apellidos": "López", "telefono": "645678901", "correo": "ana@example.com"},
            {"nombre": "Miguel", "apellidos": "Sánchez", "telefono": "656789012", "correo": "miguel@example.com"},
            {"nombre": "Elena", "apellidos": "Fernández", "telefono": "667890123", "correo": "elena@example.com"},
            {"nombre": "David", "apellidos": "García", "telefono": "678901234", "correo": "david@example.com"},
            {"nombre": "Sara", "apellidos": "Rodríguez", "telefono": "689012345", "correo": "sara@example.com"},
            {"nombre": "Pablo", "apellidos": "Hernández", "telefono": "690123456", "correo": "pablo@example.com"},
            {"nombre": "Marta", "apellidos": "Díaz", "telefono": "601234567", "correo": "marta@example.com"}
        ]
    }
    guardar_contactos(contactos_iniciales)
    print("✓ Directorio inicializado con 10 contactos")

def buscar_contacto(nombre):
    datos = cargar_contactos()
    resultados = [c for c in datos["contactos"] if nombre.lower() in c["nombre"].lower()]
    
    if resultados:
        print(f"\n--- Resultados de búsqueda para '{nombre}' ---")
        for contacto in resultados:
            print(f"Nombre: {contacto['nombre']} {contacto['apellidos']}")
            print(f"Teléfono: {contacto['telefono']}")
            print(f"Correo: {contacto['correo']}\n")
    else:
        print(f"No se encontraron contactos con el nombre '{nombre}'")
    
    return resultados

def actualizar_telefono(nombre, nuevo_telefono):
    datos = cargar_contactos()
    encontrado = False
    
    for contacto in datos["contactos"]:
        if nombre.lower() in contacto["nombre"].lower():
            contacto["telefono"] = nuevo_telefono
            encontrado = True
            print(f"✓ Teléfono de {contacto['nombre']} {contacto['apellidos']} actualizado a {nuevo_telefono}")
    
    if encontrado:
        guardar_contactos(datos)
    else:
        print(f"No se encontró el contacto '{nombre}'")

def agregar_contacto(nombre, apellidos, telefono, correo):
    datos = cargar_contactos()
    nuevo_contacto = {
        "nombre": nombre,
        "apellidos": apellidos,
        "telefono": telefono,
        "correo": correo
    }
    datos["contactos"].append(nuevo_contacto)
    guardar_contactos(datos)
    print(f"✓ Contacto {nombre} {apellidos} agregado correctamente")

def eliminar_contacto(nombre):
    datos = cargar_contactos()
    contactos_originales = len(datos["contactos"])
    datos["contactos"] = [c for c in datos["contactos"] if nombre.lower() not in c["nombre"].lower()]
    
    if len(datos["contactos"]) < contactos_originales:
        guardar_contactos(datos)
        print(f"✓ Contacto(s) con nombre '{nombre}' eliminado(s)")
    else:
        print(f"No se encontró el contacto '{nombre}'")

def listar_contactos():
    datos = cargar_contactos()
    print("\n--- DIRECTORIO TELEFÓNICO ---")
    for i, contacto in enumerate(datos["contactos"], 1):
        print(f"{i}. {contacto['nombre']} {contacto['apellidos']}")
        print(f"   Tel: {contacto['telefono']} | Email: {contacto['correo']}")
    print(f"\nTotal de contactos: {len(datos['contactos'])}\n")

def menu():
    while True:
        print("\n=== DIRECTORIO TELEFÓNICO ===")
        print("1. Listar todos los contactos")
        print("2. Buscar contacto por nombre")
        print("3. Agregar contacto")
        print("4. Actualizar teléfono")
        print("5. Eliminar contacto")
        print("6. Inicializar con datos de ejemplo")
        print("0. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            listar_contactos()
        elif opcion == "2":
            nombre = input("Ingrese el nombre a buscar: ")
            buscar_contacto(nombre)
        elif opcion == "3":
            nombre = input("Nombre: ")
            apellidos = input("Apellidos: ")
            telefono = input("Teléfono: ")
            correo = input("Correo: ")
            agregar_contacto(nombre, apellidos, telefono, correo)
        elif opcion == "4":
            nombre = input("Nombre del contacto: ")
            nuevo_telefono = input("Nuevo teléfono: ")
            actualizar_telefono(nombre, nuevo_telefono)
        elif opcion == "5":
            nombre = input("Nombre del contacto a eliminar: ")
            eliminar_contacto(nombre)
        elif opcion == "6":
            inicializar_contactos()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()
