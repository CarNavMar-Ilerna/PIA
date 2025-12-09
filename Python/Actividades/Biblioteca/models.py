"""
Módulo de modelos de datos para el Sistema de Gestión de Biblioteca.

Este módulo contiene las clases que representan las entidades principales del sistema:
- Libro: Representa un libro en la biblioteca
- Usuario: Representa un usuario de la biblioteca
- Prestamo: Representa un préstamo de un libro a un usuario
"""

from datetime import datetime


class Libro:
    """
    Clase que representa un libro en la biblioteca.
    
    Atributos:
        isbn (str): Código ISBN único del libro
        titulo (str): Título del libro
        autor (str): Autor del libro
        año (int): Año de publicación
        disponible (bool): Indica si el libro está disponible para préstamo
    """
    
    def __init__(self, isbn, titulo, autor, año, disponible=True):
        """
        Constructor de la clase Libro.
        
        Args:
            isbn (str): Código ISBN del libro
            titulo (str): Título del libro
            autor (str): Autor del libro
            año (int): Año de publicación
            disponible (bool): Estado de disponibilidad (por defecto True)
        """
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.año = int(año)
        self.disponible = disponible if isinstance(disponible, bool) else disponible.lower() == 'true'
    
    def to_dict(self):
        """
        Convierte el objeto Libro a un diccionario para guardarlo en CSV.
        
        Returns:
            dict: Diccionario con los datos del libro
        """
        return {
            'isbn': self.isbn,
            'titulo': self.titulo,
            'autor': self.autor,
            'año': str(self.año),
            'disponible': str(self.disponible)
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Crea un objeto Libro desde un diccionario.
        
        Args:
            data (dict): Diccionario con los datos del libro
            
        Returns:
            Libro: Objeto Libro creado desde el diccionario
        """
        return cls(
            isbn=data['isbn'],
            titulo=data['titulo'],
            autor=data['autor'],
            año=int(data['año']),
            disponible=data['disponible'].lower() == 'true'
        )
    
    def __str__(self):
        """
        Representación en cadena del libro.
        
        Returns:
            str: Cadena formateada con la información del libro
        """
        estado = "Disponible" if self.disponible else "Prestado"
        return f"ISBN: {self.isbn} | Título: {self.titulo} | Autor: {self.autor} | Año: {self.año} | Estado: {estado}"


class Usuario:
    """
    Clase que representa un usuario de la biblioteca.
    
    Atributos:
        id_usuario (str): Identificador único del usuario
        nombre (str): Nombre completo del usuario
        email (str): Correo electrónico del usuario
        telefono (str): Número de teléfono del usuario
    """
    
    def __init__(self, id_usuario, nombre, email, telefono):
        """
        Constructor de la clase Usuario.
        
        Args:
            id_usuario (str): Identificador único del usuario
            nombre (str): Nombre completo del usuario
            email (str): Correo electrónico del usuario
            telefono (str): Número de teléfono del usuario
        """
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
    
    def to_dict(self):
        """
        Convierte el objeto Usuario a un diccionario para guardarlo en CSV.
        
        Returns:
            dict: Diccionario con los datos del usuario
        """
        return {
            'id_usuario': self.id_usuario,
            'nombre': self.nombre,
            'email': self.email,
            'telefono': self.telefono
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Crea un objeto Usuario desde un diccionario.
        
        Args:
            data (dict): Diccionario con los datos del usuario
            
        Returns:
            Usuario: Objeto Usuario creado desde el diccionario
        """
        return cls(
            id_usuario=data['id_usuario'],
            nombre=data['nombre'],
            email=data['email'],
            telefono=data['telefono']
        )
    
    def __str__(self):
        """
        Representación en cadena del usuario.
        
        Returns:
            str: Cadena formateada con la información del usuario
        """
        return f"ID: {self.id_usuario} | Nombre: {self.nombre} | Email: {self.email} | Teléfono: {self.telefono}"


class Prestamo:
    """
    Clase que representa un préstamo de un libro a un usuario.
    
    Atributos:
        id_prestamo (str): Identificador único del préstamo
        id_usuario (str): ID del usuario que realiza el préstamo
        isbn (str): ISBN del libro prestado
        fecha_prestamo (str): Fecha en que se realizó el préstamo (formato: DD/MM/YYYY)
        fecha_devolucion (str): Fecha de devolución del libro (formato: DD/MM/YYYY)
        estado (str): Estado del préstamo ('Activo' o 'Devuelto')
    """
    
    def __init__(self, id_prestamo, id_usuario, isbn, fecha_prestamo, fecha_devolucion, estado='Activo'):
        """
        Constructor de la clase Prestamo.
        
        Args:
            id_prestamo (str): Identificador único del préstamo
            id_usuario (str): ID del usuario que realiza el préstamo
            isbn (str): ISBN del libro prestado
            fecha_prestamo (str): Fecha del préstamo (DD/MM/YYYY)
            fecha_devolucion (str): Fecha de devolución (DD/MM/YYYY)
            estado (str): Estado del préstamo (por defecto 'Activo')
        """
        self.id_prestamo = id_prestamo
        self.id_usuario = id_usuario
        self.isbn = isbn
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.estado = estado
    
    def to_dict(self):
        """
        Convierte el objeto Prestamo a un diccionario para guardarlo en CSV.
        
        Returns:
            dict: Diccionario con los datos del préstamo
        """
        return {
            'id_prestamo': self.id_prestamo,
            'id_usuario': self.id_usuario,
            'isbn': self.isbn,
            'fecha_prestamo': self.fecha_prestamo,
            'fecha_devolucion': self.fecha_devolucion,
            'estado': self.estado
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Crea un objeto Prestamo desde un diccionario.
        
        Args:
            data (dict): Diccionario con los datos del préstamo
            
        Returns:
            Prestamo: Objeto Prestamo creado desde el diccionario
        """
        return cls(
            id_prestamo=data['id_prestamo'],
            id_usuario=data['id_usuario'],
            isbn=data['isbn'],
            fecha_prestamo=data['fecha_prestamo'],
            fecha_devolucion=data['fecha_devolucion'],
            estado=data['estado']
        )
    
    def __str__(self):
        """
        Representación en cadena del préstamo.
        
        Returns:
            str: Cadena formateada con la información del préstamo
        """
        return f"ID Préstamo: {self.id_prestamo} | Usuario: {self.id_usuario} | ISBN: {self.isbn} | Fecha Préstamo: {self.fecha_prestamo} | Fecha Devolución: {self.fecha_devolucion} | Estado: {self.estado}"
