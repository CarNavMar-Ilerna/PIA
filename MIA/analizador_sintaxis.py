"""
Analizador de Sintaxis para Corpus en Español
Práctica 01 UD03 PLN - Modelos de Inteligencia Artificial

Este programa realiza análisis sintáctico completo de corpus en español usando NLTK.
Incluye: tokenización, POS tagging, análisis de frecuencia y estadísticas.
"""

import nltk
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter
import sys
import os
from pathlib import Path

# Descargar recursos de NLTK si es necesario
recursos_nltk = ['punkt', 'punkt_tab', 'stopwords', 'averaged_perceptron_tagger', 'maxent_ne_chunker', 'words']

print("Verificando recursos de NLTK...")
for recurso in recursos_nltk:
    try:
        nltk.data.find(f'tokenizers/{recurso}')
    except LookupError:
        try:
            nltk.data.find(f'corpora/{recurso}')
        except LookupError:
            try:
                nltk.data.find(f'taggers/{recurso}')
            except LookupError:
                try:
                    nltk.data.find(f'chunkers/{recurso}')
                except LookupError:
                    print(f"Descargando {recurso}...")
                    nltk.download(recurso, quiet=True)

from nltk.corpus import stopwords
import string


def leer_archivo(ruta_archivo):
    """Lee el contenido del archivo de texto."""
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
        
        if not contenido.strip():
            print(f"ADVERTENCIA: El archivo '{ruta_archivo}' está vacío.")
            return None
        
        return contenido
    except FileNotFoundError:
        print(f"ERROR: No se encontró el archivo '{ruta_archivo}'")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR al leer el archivo: {e}")
        sys.exit(1)


def analizar_texto(texto):
    """Realiza el análisis sintáctico del texto."""
    print("\n" + "="*70)
    print("ANÁLISIS SINTÁCTICO DEL CORPUS")
    print("="*70)
    
    # 1. TOKENIZACIÓN
    print("\nTokenizando texto...")
    oraciones = sent_tokenize(texto, language='spanish')
    palabras = word_tokenize(texto, language='spanish')
    
    # Filtrar palabras (solo alfabéticas)
    palabras_alfabeticas = [palabra.lower() for palabra in palabras if palabra.isalpha()]
    
    # 2. ESTADÍSTICAS BÁSICAS
    print("\n[ESTADISTICAS BASICAS]")
    print("-" * 70)
    print(f"Total de caracteres: {len(texto):,}")
    print(f"Total de tokens: {len(palabras):,}")
    print(f"Total de palabras (alfabéticas): {len(palabras_alfabeticas):,}")
    print(f"Total de oraciones: {len(oraciones):,}")
    if len(oraciones) > 0:
        print(f"Promedio de palabras por oración: {len(palabras_alfabeticas)/len(oraciones):.2f}")
    print(f"Vocabulario único: {len(set(palabras_alfabeticas)):,} palabras distintas")
    print(f"Riqueza léxica: {len(set(palabras_alfabeticas))/len(palabras_alfabeticas):.2%}")
    
    # 3. ANÁLISIS DE FRECUENCIA DE PALABRAS
    print("\n[PALABRAS MAS FRECUENTES]")
    print("-" * 70)
    
    freq_dist = FreqDist(palabras_alfabeticas)
    
    # Obtener stopwords en español
    try:
        stop_words = set(stopwords.words('spanish'))
    except:
        print("Descargando stopwords...")
        nltk.download('stopwords', quiet=True)
        stop_words = set(stopwords.words('spanish'))
    
    palabras_sin_stopwords = [palabra for palabra in palabras_alfabeticas if palabra not in stop_words]
    freq_dist_sin_stop = FreqDist(palabras_sin_stopwords)
    
    print("\nTop 20 palabras con stopwords:")
    for palabra, frecuencia in freq_dist.most_common(20):
        print(f"  {palabra:20} -> {frecuencia:6,} veces")
    
    print("\nTop 20 palabras sin stopwords:")
    for palabra, frecuencia in freq_dist_sin_stop.most_common(20):
        print(f"  {palabra:20} -> {frecuencia:6,} veces")
    
    # 4. ANÁLISIS DE LONGITUD DE PALABRAS
    print("\n[ANALISIS DE LONGITUD DE PALABRAS]")
    print("-" * 70)
    
    longitudes = [len(palabra) for palabra in palabras_alfabeticas]
    longitud_promedio = sum(longitudes) / len(longitudes) if longitudes else 0
    
    print(f"Longitud promedio de palabras: {longitud_promedio:.2f} caracteres")
    print(f"Palabra más corta: {min(longitudes)} caracteres")
    print(f"Palabra más larga: {max(longitudes)} caracteres")
    
    # Distribución de longitudes
    dist_longitudes = Counter(longitudes)
    print("\nDistribución de longitudes:")
    for longitud in sorted(dist_longitudes.keys())[:15]:
        frecuencia = dist_longitudes[longitud]
        porcentaje = (frecuencia / len(longitudes)) * 100
        barra = "#" * int(porcentaje)
        print(f"  {longitud:2} caracteres: {barra:30} {frecuencia:5,} ({porcentaje:5.2f}%)")
    
    # 5. ANÁLISIS DE ORACIONES
    print("\n[ANALISIS DE ORACIONES]")
    print("-" * 70)
    
    longitudes_oraciones = [len(word_tokenize(oracion, language='spanish')) for oracion in oraciones]
    if longitudes_oraciones:
        print(f"Longitud promedio de oraciones: {sum(longitudes_oraciones)/len(longitudes_oraciones):.2f} palabras")
        print(f"Oración más corta: {min(longitudes_oraciones)} palabras")
        print(f"Oración más larga: {max(longitudes_oraciones)} palabras")
    
    print("\nPrimeras 5 oraciones:")
    for i, oracion in enumerate(oraciones[:5], 1):
        oracion_resumida = oracion[:100] + "..." if len(oracion) > 100 else oracion
        print(f"  {i}. {oracion_resumida}")
    
    # 6. ANÁLISIS DE CARACTERES
    print("\n[ANALISIS DE CARACTERES]")
    print("-" * 70)
    
    puntuacion = sum(1 for char in texto if char in string.punctuation)
    espacios = sum(1 for char in texto if char.isspace())
    digitos = sum(1 for char in texto if char.isdigit())
    letras = sum(1 for char in texto if char.isalpha())
    
    print(f"Letras: {letras:,} ({letras/len(texto)*100:.2f}%)")
    print(f"Espacios: {espacios:,} ({espacios/len(texto)*100:.2f}%)")
    print(f"Puntuación: {puntuacion:,} ({puntuacion/len(texto)*100:.2f}%)")
    print(f"Dígitos: {digitos:,} ({digitos/len(texto)*100:.2f}%)")
    
    # 7. PALABRAS ÚNICAS (Hapax Legomena)
    print("\n[PALABRAS UNICAS - Hapax Legomena]")
    print("-" * 70)
    
    hapax = [palabra for palabra, frecuencia in freq_dist.items() if frecuencia == 1]
    print(f"Total de palabras que aparecen solo una vez: {len(hapax):,}")
    print(f"Porcentaje del vocabulario: {len(hapax)/len(set(palabras_alfabeticas))*100:.2f}%")
    
    if len(hapax) > 0:
        print(f"\nEjemplos de palabras únicas (primeras 20):")
        for palabra in hapax[:20]:
            print(f"  - {palabra}")
    
    # 8. BIGRAMAS MÁS FRECUENTES
    print("\n[BIGRAMAS MAS FRECUENTES - pares de palabras]")
    print("-" * 70)
    
    bigramas = list(nltk.bigrams(palabras_sin_stopwords))
    freq_bigramas = FreqDist(bigramas)
    
    print("\nTop 15 bigramas:")
    for bigrama, frecuencia in freq_bigramas.most_common(15):
        print(f"  '{bigrama[0]} {bigrama[1]}' -> {frecuencia:,} veces")
    
    # 9. TRIGRAMAS MÁS FRECUENTES
    print("\n[TRIGRAMAS MAS FRECUENTES - trios de palabras]")
    print("-" * 70)
    
    trigramas = list(nltk.trigrams(palabras_sin_stopwords))
    freq_trigramas = FreqDist(trigramas)
    
    print("\nTop 10 trigramas:")
    for trigrama, frecuencia in freq_trigramas.most_common(10):
        print(f"  '{trigrama[0]} {trigrama[1]} {trigrama[2]}' -> {frecuencia:,} veces")
    
    # 10. DISTRIBUCIÓN DE FRECUENCIAS
    print("\n[DISTRIBUCION DE FRECUENCIAS]")
    print("-" * 70)
    
    # Contar cuántas palabras aparecen N veces
    distribucion_freq = Counter(freq_dist.values())
    
    print("\nPalabras por frecuencia de aparición:")
    for freq in sorted(distribucion_freq.keys())[:10]:
        cantidad = distribucion_freq[freq]
        print(f"  {cantidad:5,} palabras aparecen {freq:3,} {'vez' if freq == 1 else 'veces'}")
    
    print("\n" + "="*70)
    print("ANÁLISIS COMPLETADO")
    print("="*70 + "\n")


def main():
    """Función principal del programa."""
    if len(sys.argv) < 2:
        print("Uso: python analizador_sintaxis.py <archivo.txt>")
        print("Ejemplo: python analizador_sintaxis.py biblia.txt")
        sys.exit(1)
    
    archivo = sys.argv[1]
    
    print("\n*** ANALIZADOR DE SINTAXIS - PLN (NLTK) ***")
    print(f"Archivo: {archivo}\n")
    
    # Leer archivo
    print(f"Leyendo archivo '{archivo}'...")
    texto = leer_archivo(archivo)
    
    if texto is None:
        print("\nNo hay contenido para analizar. El programa finalizará.")
        sys.exit(0)
    
    # Realizar análisis
    print(f"Analizando texto ({len(texto)} caracteres)...")
    analizar_texto(texto)


if __name__ == "__main__":
    main()
