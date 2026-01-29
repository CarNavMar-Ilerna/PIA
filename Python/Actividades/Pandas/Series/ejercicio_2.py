"""
Ejercicio 2: Calificaciones de Estudiantes
- Pide al usuario que ingrese las calificaciones de 10 estudiantes.
- Crea una Serie con las calificaciones y asigna nombres de estudiantes como índice.
- Calcula el promedio, la mediana y la desviación estándar de las calificaciones.
- Reemplaza las calificaciones que están por debajo de 50 con "Reprobado".
- Muestra los estudiantes con calificaciones aprobatorias.
"""

import pandas as pd
import numpy as np

def main():
    print("=" * 50)
    print("CALIFICACIONES DE ESTUDIANTES")
    print("=" * 50)
    
    # Solicitar nombres y calificaciones
    num_estudiantes = 10
    nombres = []
    calificaciones = []
    
    for i in range(num_estudiantes):
        nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
        nombres.append(nombre)
        
        while True:
            try:
                calificacion = float(input(f"Ingrese la calificación de {nombre} (0-100): "))
                if 0 <= calificacion <= 100:
                    calificaciones.append(calificacion)
                    break
                else:
                    print("Error: La calificación debe estar entre 0 y 100.")
            except ValueError:
                print("Error: Ingrese un número válido.")
    
    # Crear Serie con las calificaciones
    serie_calificaciones = pd.Series(calificaciones, index=nombres)
    
    print("\n" + "=" * 50)
    print("CALIFICACIONES INGRESADAS:")
    print("=" * 50)
    print(serie_calificaciones)
    
    # Calcular estadísticas
    promedio = serie_calificaciones.mean()
    mediana = serie_calificaciones.median()
    desviacion = serie_calificaciones.std()
    
    print("\n" + "=" * 50)
    print("ESTADÍSTICAS:")
    print("=" * 50)
    print(f"Promedio: {promedio:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Desviación estándar: {desviacion:.2f}")
    
    # Crear una copia para mostrar con "Reprobado"
    serie_modificada = serie_calificaciones.copy()
    serie_modificada[serie_modificada < 50] = "Reprobado"
    
    print("\n" + "=" * 50)
    print("CALIFICACIONES CON ESTADO:")
    print("=" * 50)
    print(serie_modificada)
    
    # Estudiantes con calificaciones aprobatorias (≥ 50)
    aprobados = serie_calificaciones[serie_calificaciones >= 50]
    
    print("\n" + "=" * 50)
    print("ESTUDIANTES APROBADOS:")
    print("=" * 50)
    if len(aprobados) > 0:
        print(aprobados)
        print(f"\nTotal de aprobados: {len(aprobados)} de {num_estudiantes}")
    else:
        print("No hay estudiantes aprobados.")

if __name__ == "__main__":
    main()
