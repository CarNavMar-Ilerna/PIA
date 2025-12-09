"""
Módulo de gestión de biblioteca para el Sistema de Gestión de Biblioteca.

Este módulo contiene la clase LibraryManager que gestiona todas las operaciones
de la biblioteca: libros, usuarios y préstamos.
"""

import os
from datetime import datetime
from models import Libro, Usuario, Prestamo
from file_manager import leer_csv, escribir_csv


class LibraryManager:
    """
    Clase principal que gestiona todas las operaciones de la biblioteca.
    
    Atributos:
        libros (dict): Diccionario de libros indexados por ISBN
        usuarios (dict): Diccionario de usuarios indexados por ID
        prestamos (list): Lista de préstamos
        directorio (str): Directorio donde se guardan los archivos CSV
    """
    
    def __init__(self, directorio=''):
        """
        Constructor de la clase LibraryManager.
        
        Args:
            directorio (str): Directorio donde se guardan los archivos CSV
        """
        self.libros = {}
        self.usuarios = {}
        self.prestamos = []
        self.directorio = directorio
        
        # Definir rutas de archivos
        self.archivo_libros = os.path.join(directorio, 'libros.csv')
        self.archivo_usuarios = os.path.join(directorio, 'usuarios.csv')
        self.archivo_prestamos = os.path.join(directorio, 'prestamos.csv')
        
        # Definir campos de CSV
        self.campos_libros = ['isbn', 'titulo', 'autor', 'año', 'disponible']
        self.campos_usuarios = ['id_usuario', 'nombre', 'email', 'telefono']
        self.campos_prestamos = ['id_prestamo', 'id_usuario', 'isbn', 'fecha_prestamo', 'fecha_devolucion', 'estado']
        
        # Cargar datos existentes
        self.cargar_datos()
    
    def cargar_datos(self):
        """
        Carga todos los datos desde los archivos CSV.
        """
        # Cargar libros
        datos_libros = leer_csv(self.archivo_libros, self.campos_libros)
        for dato in datos_libros:
            libro = Libro.from_dict(dato)
            self.libros[libro.isbn] = libro
        
        # Cargar usuarios
        datos_usuarios = leer_csv(self.archivo_usuarios, self.campos_usuarios)
        for dato in datos_usuarios:
            usuario = Usuario.from_dict(dato)
            self.usuarios[usuario.id_usuario] = usuario
        
        # Cargar préstamos
        datos_prestamos = leer_csv(self.archivo_prestamos, self.campos_prestamos)
        for dato in datos_prestamos:
            prestamo = Prestamo.from_dict(dato)
            self.prestamos.append(prestamo)
    
    def guardar_datos(self):
        """
        Guarda todos los datos en los archivos CSV.
        """
        # Guardar libros
        datos_libros = [libro.to_dict() for libro in self.libros.values()]
        escribir_csv(self.archivo_libros, datos_libros, self.campos_libros)
        
        # Guardar usuarios
        datos_usuarios = [usuario.to_dict() for usuario in self.usuarios.values()]
        escribir_csv(self.archivo_usuarios, datos_usuarios, self.campos_usuarios)
        
        # Guardar préstamos
        datos_prestamos = [prestamo.to_dict() for prestamo in self.prestamos]
        escribir_csv(self.archivo_prestamos, datos_prestamos, self.campos_prestamos)
    
    # ==================== GESTIÓN DE LIBROS ====================
    
    def agregar_libro(self, isbn, titulo, autor, año):
        """
        Agrega un nuevo libro a la biblioteca.
        
        Args:
            isbn (str): ISBN del libro
            titulo (str): Título del libro
            autor (str): Autor del libro
            año (int): Año de publicación
            
        Returns:
            bool: True si se agregó correctamente, False si ya existe
        """
        if isbn in self.libros:
            print(f"Error: Ya existe un libro con ISBN {isbn}")
            return False
        
        libro = Libro(isbn, titulo, autor, año)
        self.libros[isbn] = libro
        self.guardar_datos()
        print(f"Libro '{titulo}' agregado correctamente.")
        return True
    
    def eliminar_libro(self, isbn):
        """
        Elimina un libro de la biblioteca.
        
        Args:
            isbn (str): ISBN del libro a eliminar
            
        Returns:
            bool: True si se eliminó correctamente, False si no existe
        """
        if isbn not in self.libros:
            print(f"Error: No existe un libro con ISBN {isbn}")
            return False
        
        # Verificar si el libro está prestado
        if not self.libros[isbn].disponible:
            print(f"Error: No se puede eliminar el libro porque está prestado.")
            return False
        
        titulo = self.libros[isbn].titulo
        del self.libros[isbn]
        self.guardar_datos()
        print(f"Libro '{titulo}' eliminado correctamente.")
        return True
    
    def modificar_libro(self, isbn, titulo=None, autor=None, año=None):
        """
        Modifica los datos de un libro existente.
        
        Args:
            isbn (str): ISBN del libro a modificar
            titulo (str, optional): Nuevo título
            autor (str, optional): Nuevo autor
            año (int, optional): Nuevo año
            
        Returns:
            bool: True si se modificó correctamente, False si no existe
        """
        if isbn not in self.libros:
            print(f"Error: No existe un libro con ISBN {isbn}")
            return False
        
        libro = self.libros[isbn]
        if titulo:
            libro.titulo = titulo
        if autor:
            libro.autor = autor
        if año:
            libro.año = int(año)
        
        self.guardar_datos()
        print(f"Libro con ISBN {isbn} modificado correctamente.")
        return True
    
    def listar_libros(self):
        """
        Lista todos los libros de la biblioteca.
        """
        if not self.libros:
            print("No hay libros registrados en la biblioteca.")
            return
        
        print("\n" + "="*100)
        print("LISTADO DE LIBROS")
        print("="*100)
        for libro in self.libros.values():
            print(libro)
        print("="*100 + "\n")
    
    # ==================== GESTIÓN DE USUARIOS ====================
    
    def agregar_usuario(self, id_usuario, nombre, email, telefono):
        """
        Agrega un nuevo usuario a la biblioteca.
        
        Args:
            id_usuario (str): ID del usuario
            nombre (str): Nombre del usuario
            email (str): Email del usuario
            telefono (str): Teléfono del usuario
            
        Returns:
            bool: True si se agregó correctamente, False si ya existe
        """
        if id_usuario in self.usuarios:
            print(f"Error: Ya existe un usuario con ID {id_usuario}")
            return False
        
        usuario = Usuario(id_usuario, nombre, email, telefono)
        self.usuarios[id_usuario] = usuario
        self.guardar_datos()
        print(f"Usuario '{nombre}' agregado correctamente.")
        return True
    
    def eliminar_usuario(self, id_usuario):
        """
        Elimina un usuario de la biblioteca.
        
        Args:
            id_usuario (str): ID del usuario a eliminar
            
        Returns:
            bool: True si se eliminó correctamente, False si no existe
        """
        if id_usuario not in self.usuarios:
            print(f"Error: No existe un usuario con ID {id_usuario}")
            return False
        
        # Verificar si el usuario tiene préstamos activos
        prestamos_activos = [p for p in self.prestamos if p.id_usuario == id_usuario and p.estado == 'Activo']
        if prestamos_activos:
            print(f"Error: No se puede eliminar el usuario porque tiene préstamos activos.")
            return False
        
        nombre = self.usuarios[id_usuario].nombre
        del self.usuarios[id_usuario]
        self.guardar_datos()
        print(f"Usuario '{nombre}' eliminado correctamente.")
        return True
    
    def modificar_usuario(self, id_usuario, nombre=None, email=None, telefono=None):
        """
        Modifica los datos de un usuario existente.
        
        Args:
            id_usuario (str): ID del usuario a modificar
            nombre (str, optional): Nuevo nombre
            email (str, optional): Nuevo email
            telefono (str, optional): Nuevo teléfono
            
        Returns:
            bool: True si se modificó correctamente, False si no existe
        """
        if id_usuario not in self.usuarios:
            print(f"Error: No existe un usuario con ID {id_usuario}")
            return False
        
        usuario = self.usuarios[id_usuario]
        if nombre:
            usuario.nombre = nombre
        if email:
            usuario.email = email
        if telefono:
            usuario.telefono = telefono
        
        self.guardar_datos()
        print(f"Usuario con ID {id_usuario} modificado correctamente.")
        return True
    
    def listar_usuarios(self):
        """
        Lista todos los usuarios de la biblioteca.
        """
        if not self.usuarios:
            print("No hay usuarios registrados en la biblioteca.")
            return
        
        print("\n" + "="*100)
        print("LISTADO DE USUARIOS")
        print("="*100)
        for usuario in self.usuarios.values():
            print(usuario)
        print("="*100 + "\n")
    
    # ==================== GESTIÓN DE PRÉSTAMOS ====================
    
    def registrar_prestamo(self, id_usuario, isbn, fecha_prestamo, fecha_devolucion):
        """
        Registra un nuevo préstamo de un libro a un usuario.
        
        Args:
            id_usuario (str): ID del usuario
            isbn (str): ISBN del libro
            fecha_prestamo (str): Fecha del préstamo (DD/MM/YYYY)
            fecha_devolucion (str): Fecha de devolución (DD/MM/YYYY)
            
        Returns:
            bool: True si se registró correctamente, False en caso contrario
        """
        # Validar que el usuario existe
        if id_usuario not in self.usuarios:
            print(f"Error: No existe un usuario con ID {id_usuario}")
            return False
        
        # Validar que el libro existe
        if isbn not in self.libros:
            print(f"Error: No existe un libro con ISBN {isbn}")
            return False
        
        # Validar que el libro está disponible
        if not self.libros[isbn].disponible:
            print(f"Error: El libro no está disponible para préstamo.")
            return False
        
        # Validar fechas
        try:
            fecha_p = datetime.strptime(fecha_prestamo, '%d/%m/%Y')
            fecha_d = datetime.strptime(fecha_devolucion, '%d/%m/%Y')
            
            if fecha_d <= fecha_p:
                print("Error: La fecha de devolución debe ser posterior a la fecha de préstamo.")
                return False
        except ValueError:
            print("Error: Formato de fecha inválido. Use DD/MM/YYYY")
            return False
        
        # Generar ID de préstamo
        id_prestamo = str(len(self.prestamos) + 1)
        
        # Crear préstamo
        prestamo = Prestamo(id_prestamo, id_usuario, isbn, fecha_prestamo, fecha_devolucion, 'Activo')
        self.prestamos.append(prestamo)
        
        # Marcar libro como no disponible
        self.libros[isbn].disponible = False
        
        self.guardar_datos()
        print(f"Préstamo registrado correctamente. ID: {id_prestamo}")
        return True
    
    def devolver_prestamo(self, id_prestamo):
        """
        Registra la devolución de un libro.
        
        Args:
            id_prestamo (str): ID del préstamo a devolver
            
        Returns:
            bool: True si se devolvió correctamente, False en caso contrario
        """
        # Buscar el préstamo
        prestamo = None
        for p in self.prestamos:
            if p.id_prestamo == id_prestamo:
                prestamo = p
                break
        
        if not prestamo:
            print(f"Error: No existe un préstamo con ID {id_prestamo}")
            return False
        
        if prestamo.estado == 'Devuelto':
            print(f"Error: Este préstamo ya fue devuelto.")
            return False
        
        # Marcar préstamo como devuelto
        prestamo.estado = 'Devuelto'
        
        # Marcar libro como disponible
        if prestamo.isbn in self.libros:
            self.libros[prestamo.isbn].disponible = True
        
        self.guardar_datos()
        print(f"Préstamo {id_prestamo} devuelto correctamente.")
        return True
    
    def listar_prestamos_pendientes(self):
        """
        Lista todos los préstamos pendientes (activos).
        """
        prestamos_activos = [p for p in self.prestamos if p.estado == 'Activo']
        
        if not prestamos_activos:
            print("No hay préstamos pendientes.")
            return
        
        print("\n" + "="*120)
        print("LISTADO DE PRÉSTAMOS PENDIENTES")
        print("="*120)
        
        for prestamo in prestamos_activos:
            # Obtener información adicional
            usuario = self.usuarios.get(prestamo.id_usuario)
            libro = self.libros.get(prestamo.isbn)
            
            nombre_usuario = usuario.nombre if usuario else "Desconocido"
            titulo_libro = libro.titulo if libro else "Desconocido"
            
            print(f"{prestamo} | Usuario: {nombre_usuario} | Libro: {titulo_libro}")
        
        print("="*120 + "\n")
