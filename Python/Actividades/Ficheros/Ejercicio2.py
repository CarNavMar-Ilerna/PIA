import os


def crear_listin():
    if not os.path.exists('listin.txt'):
        with open('listin.txt', 'w') as archivo:
            pass


def consultar_telefono(nombre):
    try:
        with open('listin.txt', 'r') as archivo:
            for linea in archivo:
                if ',' in linea:
                    nombre_cliente, telefono = linea.strip().split(',')
                    if nombre_cliente.lower() == nombre.lower():
                        return telefono
        return None
    except FileNotFoundError:
        return None


def anadir_cliente(nombre, telefono):
    crear_listin()
    with open('listin.txt', 'a') as archivo:
        archivo.write(f'{nombre},{telefono}\n')


def eliminar_cliente(nombre):
    try:
        with open('listin.txt', 'r') as archivo:
            lineas = archivo.readlines()
        
        with open('listin.txt', 'w') as archivo:
            encontrado = False
            for linea in lineas:
                if ',' in linea:
                    nombre_cliente, _ = linea.strip().split(',')
                    if nombre_cliente.lower() != nombre.lower():
                        archivo.write(linea)
                    else:
                        encontrado = True
            
            if encontrado:
                print(f'Cliente {nombre} eliminado.')
            else:
                print(f'Cliente {nombre} no encontrado.')
    except FileNotFoundError:
        print('El fichero listin.txt no existe.')


if __name__ == '__main__':
    while True:
        print("\n=== Gestión de Listín Telefónico ===")
        print("1. Añadir cliente")
        print("2. Consultar teléfono")
        print("3. Eliminar cliente")
        print("4. Salir")
        
        opcion = input("\nElige una opción: ")
        
        if opcion == '1':
            nombre = input("Nombre del cliente: ")
            telefono = input("Teléfono del cliente: ")
            anadir_cliente(nombre, telefono)
            print(f'Cliente {nombre} añadido.')
        
        elif opcion == '2':
            nombre = input("Nombre del cliente: ")
            telefono = consultar_telefono(nombre)
            if telefono:
                print(f'El teléfono de {nombre} es {telefono}')
            else:
                print(f'Cliente {nombre} no encontrado.')
        
        elif opcion == '3':
            nombre = input("Nombre del cliente: ")
            eliminar_cliente(nombre)
        
        elif opcion == '4':
            break
        
        else:
            print("Opción no válida.")
