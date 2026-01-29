from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

def obtener_frecuencias(texto):
    """
    Cuenta la frecuencia de palabras en el texto
    
    Args:
        texto (str): Texto ya limpio
        
    Returns:
        Counter: Objeto Counter con frecuencias de palabras
    """
    # Tokenizar por espacios (el texto ya está limpio)
    palabras = texto.split()
    
    # Contar frecuencias
    frecuencias = Counter(palabras)
    
    return frecuencias

def generar_nube_palabras(frecuencias, archivo_salida='nube_palabras.png'):
    """
    Genera y guarda una nube de palabras
    
    Args:
        frecuencias (Counter): Frecuencias de palabras
        archivo_salida (str): Nombre del archivo de salida
    """
    # Configurar la nube de palabras
    wordcloud = WordCloud(
        width=1600,
        height=900,
        background_color='white',
        colormap='viridis',
        max_words=100,
        relative_scaling=0.5,
        min_font_size=10
    ).generate_from_frequencies(frecuencias)
    
    # Crear la figura
    plt.figure(figsize=(16, 9), facecolor='white')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Nube de Palabras - Adan y Eva en el Paraiso', 
              fontsize=20, fontweight='bold', pad=20)
    plt.tight_layout(pad=0)
    
    # Guardar la imagen
    plt.savefig(archivo_salida, dpi=300, bbox_inches='tight')
    print(f"\nOK Nube de palabras guardada como: {archivo_salida}")
    
    # Cerrar la figura para evitar que se muestre
    plt.close()

def main():
    """
    Función principal del programa
    """
    print("="*60)
    print("ANALISIS DE FRECUENCIA DE PALABRAS")
    print("Texto: Adan y Eva en el Paraiso")
    print("="*60)
    
    # Ruta del directorio actual del script
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    archivo_entrada = os.path.join(directorio_actual, 'AdanYEva.txt')
    archivo_salida_imagen = os.path.join(directorio_actual, 'nube_palabras_AdanYEva.png')
    archivo_salida_stats = os.path.join(directorio_actual, 'estadisticas_frecuencias.txt')
    
    try:
        # Leer el archivo (ya limpio)
        print(f"\n[1] Leyendo archivo: {archivo_entrada}...")
        with open(archivo_entrada, 'r', encoding='utf-8') as f:
            texto_limpio = f.read()
        print(f"    OK Archivo leido correctamente ({len(texto_limpio)} caracteres)")
        
        # Obtener frecuencias
        print("\n[2] Contando frecuencias de palabras...")
        frecuencias = obtener_frecuencias(texto_limpio)
        print(f"    OK Se encontraron {len(frecuencias)} palabras unicas")
        print(f"    OK Total de palabras: {sum(frecuencias.values())}")
        
        # Mostrar las 20 palabras más frecuentes
        print("\n[3] Top 20 palabras mas frecuentes:")
        print("    " + "-"*50)
        for i, (palabra, freq) in enumerate(frecuencias.most_common(20), 1):
            print(f"    {i:2d}. {palabra:20s} - {freq:4d} veces")
        print("    " + "-"*50)
        
        # Generar y guardar la nube de palabras
        print("\n[4] Generando nube de palabras...")
        generar_nube_palabras(frecuencias, archivo_salida_imagen)
        
        # Guardar estadísticas en archivo de texto
        print("\n[5] Guardando estadisticas en archivo...")
        with open(archivo_salida_stats, 'w', encoding='utf-8') as f:
            f.write("ANALISIS DE FRECUENCIA DE PALABRAS\n")
            f.write("Texto: Adan y Eva en el Paraiso\n")
            f.write("="*60 + "\n\n")
            f.write(f"Total de palabras unicas: {len(frecuencias)}\n")
            f.write(f"Total de palabras en el texto: {sum(frecuencias.values())}\n\n")
            f.write("Top 50 palabras mas frecuentes:\n")
            f.write("-"*60 + "\n")
            for i, (palabra, freq) in enumerate(frecuencias.most_common(50), 1):
                f.write(f"{i:2d}. {palabra:20s} - {freq:4d} veces\n")
        print("    OK Estadisticas guardadas en: estadisticas_frecuencias.txt")
        
        print("\n" + "="*60)
        print("ANALISIS COMPLETADO EXITOSAMENTE")
        print("="*60)
        
    except FileNotFoundError:
        print(f"\nERROR: No se encontro el archivo '{archivo_entrada}'")
        print("  Asegurate de que el archivo este en el mismo directorio que el script.")
    except Exception as e:
        print(f"\nERROR inesperado: {str(e)}")

if __name__ == "__main__":
    main()
