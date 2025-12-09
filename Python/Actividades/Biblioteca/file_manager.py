"""
Módulo de gestión de archivos CSV para el Sistema de Gestión de Biblioteca.

Este módulo proporciona funciones para leer y escribir datos en archivos CSV,
así como para crear archivos con encabezados si no existen.
"""

import csv
import os


def crear_archivo_si_no_existe(archivo, campos):
    """
    Crea un archivo CSV con encabezados si no existe.
    
    Args:
        archivo (str): Ruta del archivo CSV
        campos (list): Lista de nombres de campos para los encabezados
    """
    if not os.path.exists(archivo):
        with open(archivo, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()


def leer_csv(archivo, campos):
    """
    Lee un archivo CSV y devuelve una lista de diccionarios.
    
    Args:
        archivo (str): Ruta del archivo CSV
        campos (list): Lista de nombres de campos esperados
        
    Returns:
        list: Lista de diccionarios con los datos del archivo
    """
    # Crear el archivo si no existe
    crear_archivo_si_no_existe(archivo, campos)
    
    datos = []
    try:
        with open(archivo, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                datos.append(row)
    except FileNotFoundError:
        # Si el archivo no existe, devolver lista vacía
        return []
    except Exception as e:
        print(f"Error al leer el archivo {archivo}: {e}")
        return []
    
    return datos


def escribir_csv(archivo, datos, campos):
    """
    Escribe una lista de diccionarios en un archivo CSV.
    
    Args:
        archivo (str): Ruta del archivo CSV
        datos (list): Lista de diccionarios con los datos a escribir
        campos (list): Lista de nombres de campos para los encabezados
    """
    try:
        with open(archivo, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            writer.writerows(datos)
    except Exception as e:
        print(f"Error al escribir el archivo {archivo}: {e}")
