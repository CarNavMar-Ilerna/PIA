"""
Sistema de Gestión de Biblioteca - Interfaz de Usuario

Este es el archivo principal del sistema que proporciona una interfaz de menú
para gestionar libros, usuarios y préstamos de la biblioteca.
"""

import os
from library_manager import LibraryManager


def limpiar_pantalla():
    """
    Limpia la pantalla de la consola.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    """
    Pausa la ejecución hasta que el usuario presione Enter.
    """
    input("\nPresione Enter para continuar...")


def mostrar_menu_principal():
    """
    Muestra el menú principal del sistema.
    """
    print("\n" + "="*60)
    print(" "*15 + "SISTEMA DE GESTIÓN DE BIBLIOTECA")
    print("="*60)
    print("1. Gestión de Libros")
    print("2. Gestión de Usuarios")
    print("3. Gestión de Préstamos")
    print("4. Salir")
    print("="*60)


def mostrar_menu_libros():
    """
    Muestra el menú de gestión de libros.
    """
    print("\n" + "="*60)
    print(" "*20 + "GESTIÓN DE LIBROS")
    print("="*60)
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Modificar libro")
    print("4. Listar libros")
    print("5. Volver al menú principal")
    print("="*60)


def mostrar_menu_usuarios():
    """
    Muestra el menú de gestión de usuarios.
    """
    print("\n" + "="*60)
    print(" "*19 + "GESTIÓN DE USUARIOS")
    print("="*60)
    print("1. Agregar usuario")
    print("2. Eliminar usuario")
    print("3. Modificar usuario")
    print("4. Listar usuarios")
    print("5. Volver al menú principal")
    print("="*60)


def mostrar_menu_prestamos():
    """
    Muestra el menú de gestión de préstamos.
    """
    print("\n" + "="*60)
    print(" "*18 + "GESTIÓN DE PRÉSTAMOS")
    print("="*60)
    print("1. Registrar préstamo")
    print("2. Devolver libro")
    print("3. Listar préstamos pendientes")
    print("4. Volver al menú principal")
    print("="*60)


def gestionar_libros(manager):
    """
    Gestiona las operaciones relacionadas con libros.
    
    Args:
        manager (LibraryManager): Instancia del gestor de biblioteca
    """
    while True:
        limpiar_pantalla()
        mostrar_menu_libros()
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == '1':
            # Agregar libro
            print("\n--- AGREGAR LIBRO ---")
            isbn = input("ISBN: ").strip()
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            año = input("Año de publicación: ").strip()
            
            if isbn and titulo and autor and año:
                try:
                    año = int(año)
                    manager.agregar_libro(isbn, titulo, autor, año)
                except ValueError:
                    print("Error: El año debe ser un número válido.")
            else:
                print("Error: Todos los campos son obligatorios.")
            pausar()
        
        elif opcion == '2':
            # Eliminar libro
            print("\n--- ELIMINAR LIBRO ---")
            isbn = input("ISBN del libro a eliminar: ").strip()
            if isbn:
                manager.eliminar_libro(isbn)
            else:
                print("Error: Debe ingresar un ISBN.")
            pausar()
        
        elif opcion == '3':
            # Modificar libro
            print("\n--- MODIFICAR LIBRO ---")
            isbn = input("ISBN del libro a modificar: ").strip()
            
            if isbn:
                print("Deje en blanco los campos que no desea modificar.")
                titulo = input("Nuevo título: ").strip()
                autor = input("Nuevo autor: ").strip()
                año = input("Nuevo año: ").strip()
                
                titulo = titulo if titulo else None
                autor = autor if autor else None
                año = int(año) if año else None
                
                manager.modificar_libro(isbn, titulo, autor, año)
            else:
                print("Error: Debe ingresar un ISBN.")
            pausar()
        
        elif opcion == '4':
            # Listar libros
            manager.listar_libros()
            pausar()
        
        elif opcion == '5':
            # Volver al menú principal
            break
        
        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 5.")
            pausar()


def gestionar_usuarios(manager):
    """
    Gestiona las operaciones relacionadas con usuarios.
    
    Args:
        manager (LibraryManager): Instancia del gestor de biblioteca
    """
    while True:
        limpiar_pantalla()
        mostrar_menu_usuarios()
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == '1':
            # Agregar usuario
            print("\n--- AGREGAR USUARIO ---")
            id_usuario = input("ID de usuario: ").strip()
            nombre = input("Nombre completo: ").strip()
            email = input("Email: ").strip()
            telefono = input("Teléfono: ").strip()
            
            if id_usuario and nombre and email and telefono:
                manager.agregar_usuario(id_usuario, nombre, email, telefono)
            else:
                print("Error: Todos los campos son obligatorios.")
            pausar()
        
        elif opcion == '2':
            # Eliminar usuario
            print("\n--- ELIMINAR USUARIO ---")
            id_usuario = input("ID del usuario a eliminar: ").strip()
            if id_usuario:
                manager.eliminar_usuario(id_usuario)
            else:
                print("Error: Debe ingresar un ID de usuario.")
            pausar()
        
        elif opcion == '3':
            # Modificar usuario
            print("\n--- MODIFICAR USUARIO ---")
            id_usuario = input("ID del usuario a modificar: ").strip()
            
            if id_usuario:
                print("Deje en blanco los campos que no desea modificar.")
                nombre = input("Nuevo nombre: ").strip()
                email = input("Nuevo email: ").strip()
                telefono = input("Nuevo teléfono: ").strip()
                
                nombre = nombre if nombre else None
                email = email if email else None
                telefono = telefono if telefono else None
                
                manager.modificar_usuario(id_usuario, nombre, email, telefono)
            else:
                print("Error: Debe ingresar un ID de usuario.")
            pausar()
        
        elif opcion == '4':
            # Listar usuarios
            manager.listar_usuarios()
            pausar()
        
        elif opcion == '5':
            # Volver al menú principal
            break
        
        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 5.")
            pausar()


def gestionar_prestamos(manager):
    """
    Gestiona las operaciones relacionadas con préstamos.
    
    Args:
        manager (LibraryManager): Instancia del gestor de biblioteca
    """
    while True:
        limpiar_pantalla()
        mostrar_menu_prestamos()
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == '1':
            # Registrar préstamo
            print("\n--- REGISTRAR PRÉSTAMO ---")
            id_usuario = input("ID del usuario: ").strip()
            isbn = input("ISBN del libro: ").strip()
            fecha_prestamo = input("Fecha de préstamo (DD/MM/YYYY): ").strip()
            fecha_devolucion = input("Fecha de devolución (DD/MM/YYYY): ").strip()
            
            if id_usuario and isbn and fecha_prestamo and fecha_devolucion:
                manager.registrar_prestamo(id_usuario, isbn, fecha_prestamo, fecha_devolucion)
            else:
                print("Error: Todos los campos son obligatorios.")
            pausar()
        
        elif opcion == '2':
            # Devolver libro
            print("\n--- DEVOLVER LIBRO ---")
            id_prestamo = input("ID del préstamo: ").strip()
            if id_prestamo:
                manager.devolver_prestamo(id_prestamo)
            else:
                print("Error: Debe ingresar un ID de préstamo.")
            pausar()
        
        elif opcion == '3':
            # Listar préstamos pendientes
            manager.listar_prestamos_pendientes()
            pausar()
        
        elif opcion == '4':
            # Volver al menú principal
            break
        
        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 4.")
            pausar()


def main():
    """
    Función principal del programa.
    """
    # Obtener el directorio actual del script
    directorio = os.path.dirname(os.path.abspath(__file__))
    
    # Crear instancia del gestor de biblioteca
    manager = LibraryManager(directorio)
    
    # Bucle principal del programa
    while True:
        limpiar_pantalla()
        mostrar_menu_principal()
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == '1':
            gestionar_libros(manager)
        
        elif opcion == '2':
            gestionar_usuarios(manager)
        
        elif opcion == '3':
            gestionar_prestamos(manager)
        
        elif opcion == '4':
            print("\n¡Gracias por usar el Sistema de Gestión de Biblioteca!")
            print("¡Hasta pronto!\n")
            break
        
        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 4.")
            pausar()


if __name__ == "__main__":
    main()
