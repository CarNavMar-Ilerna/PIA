"""
Conversor de Texto a Voz (TXT -> MP3)
Práctica 01 UD03 PLN - Modelos de Inteligencia Artificial

Este programa convierte archivos de texto a formato de audio MP3 con preprocesamiento
y detección automática del idioma.
"""

from gtts import gTTS
import os
import sys
import re
from pathlib import Path

# Intentar importar langdetect, pero no es crítico
try:
    from langdetect import detect, LangDetectException
    LANGDETECT_DISPONIBLE = True
except ImportError:
    LANGDETECT_DISPONIBLE = False
    print("NOTA: langdetect no está instalado. Se usará español por defecto.")
    print("Para instalar: pip install langdetect\n")


def preprocesar_texto(texto):
    """
    Preprocesa el texto antes de la conversión a voz.
    
    Args:
        texto: El texto original a procesar
        
    Returns:
        El texto procesado y limpio
    """
    # Eliminar múltiples espacios en blanco
    texto = re.sub(r'\s+', ' ', texto)
    
    # Eliminar espacios al inicio y final
    texto = texto.strip()
    
    # Normalizar saltos de línea (máximo 2 consecutivos)
    texto = re.sub(r'\n{3,}', '\n\n', texto)
    
    # Eliminar caracteres de control extraños (excepto espacios y saltos de línea)
    texto = re.sub(r'[\x00-\x08\x0B-\x0C\x0E-\x1F\x7F]', '', texto)
    
    # Asegurar punto al final de párrafos para pausas naturales
    texto = re.sub(r'([^\.\!\?])\n', r'\1. ', texto)
    
    return texto


def detectar_idioma(texto):
    """
    Detecta el idioma del texto automáticamente.
    
    Args:
        texto: El texto a analizar
        
    Returns:
        Código del idioma (ej: 'es', 'en', 'fr')
    """
    if not LANGDETECT_DISPONIBLE:
        return 'es'  # Español por defecto
    
    try:
        # Usar una muestra del texto para la detección (más rápido)
        muestra = texto[:1000] if len(texto) > 1000 else texto
        idioma = detect(muestra)
        
        # Mapeo de idiomas comunes
        idiomas_dict = {
            'es': 'Español',
            'en': 'Inglés',
            'fr': 'Francés',
            'de': 'Alemán',
            'it': 'Italiano',
            'pt': 'Portugués',
            'ca': 'Catalán',
            'gl': 'Gallego',
            'eu': 'Euskera'
        }
        
        nombre_idioma = idiomas_dict.get(idioma, f'Desconocido ({idioma})')
        print(f"OK Idioma detectado: {nombre_idioma} ({idioma})")
        
        return idioma
    except LangDetectException:
        print("! No se pudo detectar el idioma. Usando español por defecto.")
        return 'es'
    except Exception as e:
        print(f"! Error al detectar idioma: {e}. Usando español por defecto.")
        return 'es'


def leer_archivo(ruta_archivo):
    """Lee el contenido del archivo de texto."""
    try:
        # Intentar con UTF-8 primero
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
        return contenido
    except UnicodeDecodeError:
        # Si falla, intentar con latin-1
        try:
            with open(ruta_archivo, 'r', encoding='latin-1') as f:
                contenido = f.read()
            print("! Archivo leído con codificación latin-1")
            return contenido
        except Exception as e:
            print(f"ERROR al leer el archivo: {e}")
            sys.exit(1)
    except FileNotFoundError:
        print(f"ERROR: No se encontró el archivo '{ruta_archivo}'")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR al leer el archivo: {e}")
        sys.exit(1)


def convertir_texto_a_voz(texto, idioma, archivo_salida):
    """
    Convierte el texto a voz y guarda el archivo MP3.
    
    Args:
        texto: El texto a convertir
        idioma: Código del idioma
        archivo_salida: Ruta del archivo MP3 de salida
    """
    try:
        print(f"\n  Convirtiendo texto a voz...")
        print(f"   Caracteres a convertir: {len(texto):,}")
        print(f"   Idioma: {idioma}")
        
        # Crear objeto gTTS
        tts = gTTS(text=texto, lang=idioma, slow=False)
        
        # Guardar como MP3
        tts.save(archivo_salida)
        
        # Verificar que se creó el archivo
        if os.path.exists(archivo_salida):
            tamaño = os.path.getsize(archivo_salida)
            tamaño_mb = tamaño / (1024 * 1024)
            print(f"\n[OK] ¡Conversión exitosa!")
            print(f"   Archivo creado: {archivo_salida}")
            print(f"   Tamaño: {tamaño_mb:.2f} MB")
        else:
            print("\n[ERROR] Error: El archivo no se creó correctamente.")
            sys.exit(1)
            
    except Exception as e:
        print(f"\n[ERROR] ERROR durante la conversión: {e}")
        print("\nPosibles soluciones:")
        print("  - Verifica tu conexión a Internet (gTTS necesita conexión)")
        print("  - Instala/actualiza gTTS: pip install --upgrade gtts")
        sys.exit(1)


def obtener_archivo_salida(archivo_entrada):
    """
    Genera el nombre del archivo de salida basado en el archivo de entrada.
    
    Args:
        archivo_entrada: Ruta del archivo de texto de entrada
        
    Returns:
        Ruta del archivo MP3 de salida
    """
    # Obtener el nombre base sin extensión
    path_entrada = Path(archivo_entrada)
    nombre_base = path_entrada.stem
    directorio = path_entrada.parent
    
    # Crear el nombre del archivo de salida
    archivo_salida = directorio / f"{nombre_base}.mp3"
    
    return str(archivo_salida)


def main():
    """Función principal del programa."""
    print("\n" + "="*70)
    print("*** CONVERSOR DE TEXTO A VOZ (TXT -> MP3) ***")
    print("="*70 + "\n")
    
    if len(sys.argv) < 2:
        print("Uso: python texto_a_voz.py <archivo.txt>")
        print("Ejemplo: python texto_a_voz.py biblia.txt")
        print("\nEl programa generará un archivo MP3 con el mismo nombre del archivo de entrada.")
        sys.exit(1)
    
    archivo_entrada = sys.argv[1]
    
    # Verificar que el archivo tiene extensión .txt
    if not archivo_entrada.lower().endswith('.txt'):
        print(f"! ADVERTENCIA: El archivo '{archivo_entrada}' no tiene extensión .txt")
        respuesta = input("¿Deseas continuar de todas formas? (s/n): ")
        if respuesta.lower() != 's':
            print("Operación cancelada.")
            sys.exit(0)
    
    print(f"Archivo de entrada: {archivo_entrada}")
    
    # Leer el archivo
    print("\nLeyendo archivo...")
    texto_original = leer_archivo(archivo_entrada)
    
    if not texto_original.strip():
        print("\n[ERROR] ERROR: El archivo está vacío. No hay contenido para convertir.")
        sys.exit(1)
    
    print(f"OK - Archivo leido correctamente ({len(texto_original):,} caracteres)")
    
    # Preprocesar el texto
    print("\nPreprocesando texto...")
    print("   - Normalizando espacios")
    print("   - Limpiando caracteres especiales")
    print("   - Organizando párrafos")
    texto_procesado = preprocesar_texto(texto_original)
    print(f"OK - Texto procesado ({len(texto_procesado):,} caracteres)")
    
    # Detectar idioma
    print("\nDetectando idioma...")
    idioma = detectar_idioma(texto_procesado)
    
    # Generar nombre del archivo de salida
    archivo_salida = obtener_archivo_salida(archivo_entrada)
    
    # Verificar si el archivo de salida ya existe
    if os.path.exists(archivo_salida):
        print(f"\n! El archivo '{archivo_salida}' ya existe.")
        respuesta = input("¿Deseas sobrescribirlo? (s/n): ")
        if respuesta.lower() != 's':
            print("Operación cancelada.")
            sys.exit(0)
    
    # Convertir texto a voz
    convertir_texto_a_voz(texto_procesado, idioma, archivo_salida)
    
    print("\n" + "="*70)
    print("*** PROCESO COMPLETADO EXITOSAMENTE ***")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
