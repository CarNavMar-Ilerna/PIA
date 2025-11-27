import json
import re
import os1
from datetime import datetime


def cargar_datos(nombre_archivo):
    """
    Función para cargar y leer el contenido de un archivo JSON.
    
    Args:
        nombre_archivo (str): Nombre del archivo JSON a cargar
        
    Returns:
        list: Lista con los datos del archivo JSON
    """
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
        print(f"[OK] Archivo '{nombre_archivo}' cargado correctamente.")
        return datos
    except FileNotFoundError:
        print(f"[ERROR] El archivo '{nombre_archivo}' no existe.")
        return []
    except json.JSONDecodeError:
        print(f"[ERROR] El archivo '{nombre_archivo}' no tiene un formato JSON válido.")
        return []


# VALIDACIÓN DE ALUMNOS

def patron_email(email):
    """
    Valida que el email sea correcto usando expresiones regulares.
    
    Args:
        email (str): Email a validar
        
    Returns:
        bool: True si el email es válido, False en caso contrario
    """
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None


def patron_telefono(telefono):
    """
    Comprueba que el teléfono comienza por 9, 6 o 7 y tiene 9 cifras.
    
    Args:
        telefono (str): Número de teléfono a validar
        
    Returns:
        bool: True si el teléfono es válido, False en caso contrario
    """
    patron = r'^[967]\d{8}$'
    return re.match(patron, telefono) is not None


def patron_codigo_postal(codigo_postal):
    """
    Verifica que el código postal tenga exactamente 5 dígitos.
    
    Args:
        codigo_postal (str): Código postal a validar
        
    Returns:
        bool: True si el código postal es válido, False en caso contrario
    """
    patron = r'^\d{5}$'
    return re.match(patron, codigo_postal) is not None


def validar_alumnos(alumnos):
    """
    Valida todos los alumnos del archivo JSON.
    
    Args:
        alumnos (list): Lista de diccionarios con información de alumnos
    """
    print("\n" + "="*60)
    print("VALIDACIÓN DE ALUMNOS")
    print("="*60)
    
    for i, alumno in enumerate(alumnos, 1):
        print(f"\nAlumno {i}: {alumno.get('nombre', 'Sin nombre')}")
        print("-" * 40)
        
        # Validar email
        email = alumno.get('email', '')
        if patron_email(email):
            print(f"  [OK] Email válido: {email}")
        else:
            print(f"  [X] Email inválido: {email}")
        
        # Validar teléfono
        telefono = alumno.get('telefono', '')
        if patron_telefono(telefono):
            print(f"  [OK] Teléfono válido: {telefono}")
        else:
            print(f"  [X] Teléfono inválido: {telefono}")
        
        # Validar código postal
        codigo_postal = alumno.get('codigo_postal', '')
        if patron_codigo_postal(codigo_postal):
            print(f"  [OK] Código postal válido: {codigo_postal}")
        else:
            print(f"  [X] Código postal inválido: {codigo_postal}")
        
        print(f"  Curso: {alumno.get('curso', 'No especificado')}")


# VALIDACIÓN DE VEHÍCULOS

def patron_matricula(matricula):
    """
    Verifica que la matrícula siga el formato español: 4 números y 3 letras.
    
    Args:
        matricula (str): Matrícula a validar
        
    Returns:
        bool: True si la matrícula es válida, False en caso contrario
    """
    patron = r'^\d{4}[A-Z]{3}$'
    return re.match(patron, matricula) is not None


def patron_ano(ano):
    """
    Acepta años entre 1900 y el año actual.
    
    Args:
        ano (int): Año a validar
        
    Returns:
        bool: True si el año es válido, False en caso contrario
    """
    ano_actual = datetime.now().year
    return isinstance(ano, int) and 1900 <= ano <= ano_actual


def validar_vehiculos(vehiculos):
    """
    Valida todos los vehículos del archivo JSON.
    
    Args:
        vehiculos (list): Lista de diccionarios con información de vehículos
    """
    print("\n" + "="*60)
    print("VALIDACIÓN DE VEHÍCULOS")
    print("="*60)
    
    for i, vehiculo in enumerate(vehiculos, 1):
        print(f"\nVehículo {i}: {vehiculo.get('marca', 'Sin marca')} {vehiculo.get('modelo', 'Sin modelo')}")
        print("-" * 40)
        
        # Validar matrícula
        matricula = vehiculo.get('matricula', '')
        if patron_matricula(matricula):
            print(f"  [OK] Matrícula válida: {matricula}")
        else:
            print(f"  [X] Matrícula inválida: {matricula}")
        
        # Validar año
        ano = vehiculo.get('año', 0)
        if patron_ano(ano):
            print(f"  [OK] Año válido: {ano}")
        else:
            print(f"  [X] Año inválido: {ano}")
        
        # Validar email del propietario
        email_propietario = vehiculo.get('propietario_email', '')
        if patron_email(email_propietario):
            print(f"  [OK] Email del propietario válido: {email_propietario}")
        else:
            print(f"  [X] Email del propietario inválido: {email_propietario}")


def main():
    """
    Función principal que ejecuta todo el programa.
    """
    print("\n" + "="*60)
    print("SISTEMA DE VALIDACIÓN CON EXPRESIONES REGULARES")
    print("="*60)
    
    # Obtener el directorio donde está el script
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    
    # Construir las rutas completas a los archivos JSON
    ruta_alumnos = os.path.join(directorio_actual, 'alumnos.json')
    ruta_vehiculos = os.path.join(directorio_actual, 'vehiculos.json')
    
    # Cargar datos de alumnos
    alumnos = cargar_datos(ruta_alumnos)
    
    # Cargar datos de vehículos
    vehiculos = cargar_datos(ruta_vehiculos)
    
    # Validar alumnos
    if alumnos:
        validar_alumnos(alumnos)
    
    # Validar vehículos
    if vehiculos:
        validar_vehiculos(vehiculos)
    
    print("\n" + "="*60)
    print("VALIDACIÓN COMPLETADA")
    print("="*60 + "\n")



if __name__ == "__main__":
    main()
