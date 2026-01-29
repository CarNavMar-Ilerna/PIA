#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para limpiar el texto AdanYEva.txt
Elimina puntuación, convierte a minúsculas, y elimina stopwords
"""

import re
import nltk
import os

# Descargar recursos necesarios de NLTK
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def limpiar_texto_completo(archivo_entrada, archivo_salida=None):
    """
    Limpia el texto completo eliminando puntuación y stopwords
    
    Args:
        archivo_entrada (str): Ruta del archivo a limpiar
        archivo_salida (str): Ruta del archivo de salida (si None, sobrescribe el original)
    """
    print("="*60)
    print("LIMPIEZA DE TEXTO")
    print("="*60)
    
    # Leer el archivo original
    print(f"\n[1] Leyendo archivo: {archivo_entrada}...")
    with open(archivo_entrada, 'r', encoding='utf-8') as f:
        texto_original = f.read()
    print(f"    OK Archivo leído ({len(texto_original)} caracteres)")
    
    # Convertir a minúsculas
    print("\n[2] Convirtiendo a minúsculas...")
    texto = texto_original.lower()
    
    # Eliminar signos de puntuación y caracteres especiales
    print("[3] Eliminando puntuación y caracteres especiales...")
    texto = re.sub(r'[^\w\s]', ' ', texto)
    texto = re.sub(r'\d+', '', texto)
    texto = re.sub(r'\s+', ' ', texto)
    
    # Obtener stopwords
    print("[4] Eliminando stopwords...")
    stop_words = set(stopwords.words('spanish'))
    
    # Agregar stopwords adicionales
    stop_words_adicionales = {
        'así', 'cuán', 'tal', 'mas', 'oh', 'ahí', 'aquí',
        'allí', 'allá', 'pues', 'bien', 'aún', 'aquella',
        'aquellas', 'aquel', 'aquellos', 'sí', 'r', 'n'
    }
    stop_words.update(stop_words_adicionales)
    
    # Tokenizar
    palabras = word_tokenize(texto, language='spanish')
    
    # Filtrar stopwords y palabras muy cortas
    palabras_filtradas = [
        palabra for palabra in palabras 
        if palabra not in stop_words and len(palabra) > 2
    ]
    
    # Reconstruir el texto
    texto_limpio = ' '.join(palabras_filtradas)
    
    # Determinar archivo de salida
    if archivo_salida is None:
        archivo_salida = archivo_entrada
    
    # Guardar el texto limpio
    print(f"\n[5] Guardando texto limpio en: {archivo_salida}...")
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        f.write(texto_limpio)
    
    print(f"    OK Archivo guardado")
    print(f"\n    Estadísticas:")
    print(f"    - Texto original: {len(texto_original)} caracteres")
    print(f"    - Texto limpio:   {len(texto_limpio)} caracteres")
    print(f"    - Palabras totales (original): {len(texto_original.split())}")
    print(f"    - Palabras filtradas (limpio): {len(palabras_filtradas)}")
    
    print("\n" + "="*60)
    print("LIMPIEZA COMPLETADA EXITOSAMENTE")
    print("="*60)

if __name__ == "__main__":
    # Ruta del directorio actual del script
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    archivo_objetivo = os.path.join(directorio_actual, 'AdanYEva.txt')
    
    # Limpiar el archivo AdanYEva.txt y sobrescribir el original
    limpiar_texto_completo(archivo_objetivo)
