"""
Ejercicio 6: Evaluación de Encuesta de Satisfacción
- Solicita al usuario que ingrese las calificaciones de satisfacción (de 1 a 5) de 12 clientes.
- Crea una Serie con las calificaciones.
- Calcula la frecuencia de cada calificación y el porcentaje de clientes satisfechos (calificación ≥ 4).
- Reemplaza cualquier calificación de 1 con "Insatisfecho".
- Muestra un resumen de las calificaciones en forma de gráfico de barras.
"""

import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("=" * 50)
    print("EVALUACIÓN DE ENCUESTA DE SATISFACCIÓN")
    print("=" * 50)
    
    # Solicitar calificaciones de satisfacción
    num_clientes = 12
    calificaciones = []
    
    print("Escala de satisfacción: 1 (Muy insatisfecho) a 5 (Muy satisfecho)\n")
    
    for i in range(num_clientes):
        while True:
            try:
                calificacion = int(input(f"Ingrese la calificación del cliente {i+1} (1-5): "))
                if 1 <= calificacion <= 5:
                    calificaciones.append(calificacion)
                    break
                else:
                    print("Error: La calificación debe estar entre 1 y 5.")
            except ValueError:
                print("Error: Ingrese un número entero válido.")
    
    # Crear Serie con las calificaciones
    serie_calificaciones = pd.Series(calificaciones, index=[f"Cliente {i+1}" for i in range(num_clientes)])
    
    print("\n" + "=" * 50)
    print("CALIFICACIONES INGRESADAS:")
    print("=" * 50)
    print(serie_calificaciones)
    
    # Calcular frecuencia de cada calificación
    frecuencia = serie_calificaciones.value_counts().sort_index()
    
    print("\n" + "=" * 50)
    print("FRECUENCIA DE CALIFICACIONES:")
    print("=" * 50)
    for cal, freq in frecuencia.items():
        print(f"Calificación {cal}: {freq} clientes")
    
    # Calcular porcentaje de clientes satisfechos (≥ 4)
    clientes_satisfechos = serie_calificaciones[serie_calificaciones >= 4]
    porcentaje_satisfechos = (len(clientes_satisfechos) / num_clientes) * 100
    
    print("\n" + "=" * 50)
    print("ANÁLISIS DE SATISFACCIÓN:")
    print("=" * 50)
    print(f"Clientes satisfechos (≥ 4): {len(clientes_satisfechos)} de {num_clientes}")
    print(f"Porcentaje de satisfacción: {porcentaje_satisfechos:.2f}%")
    
    # Reemplazar calificaciones de 1 con "Insatisfecho"
    serie_modificada = serie_calificaciones.copy()
    serie_modificada[serie_modificada == 1] = "Insatisfecho"
    
    print("\n" + "=" * 50)
    print("CALIFICACIONES CON ESTADO:")
    print("=" * 50)
    print(serie_modificada)
    
    # Crear gráfico de barras
    plt.figure(figsize=(10, 6))
    frecuencia.plot(kind='bar', color=['#e74c3c', '#e67e22', '#f39c12', '#27ae60', '#2ecc71'])
    plt.title('Distribución de Calificaciones de Satisfacción', fontsize=16, fontweight='bold')
    plt.xlabel('Calificación', fontsize=12)
    plt.ylabel('Número de Clientes', fontsize=12)
    plt.xticks(rotation=0)
    plt.grid(True, alpha=0.3, axis='y')
    
    # Añadir etiquetas de valor en las barras
    for i, v in enumerate(frecuencia.values):
        plt.text(i, v + 0.1, str(v), ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.show()
    
    print("\n✓ Gráfico de barras generado exitosamente.")

if __name__ == "__main__":
    main()
