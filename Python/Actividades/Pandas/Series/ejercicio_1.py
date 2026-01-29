"""
Ejercicio 1: Análisis de Ventas de una Semana
- Solicita al usuario que ingrese las ventas diarias de una semana (7 días).
- Crea una Serie con los datos proporcionados.
- Realiza el análisis: muestra el total de ventas, el promedio, y el día con las mayores ventas.
- Visualiza los días que tienen ventas por encima del promedio.
"""

import pandas as pd

def main():
    print("=" * 50)
    print("ANÁLISIS DE VENTAS DE UNA SEMANA")
    print("=" * 50)
    
    # Solicitar las ventas diarias
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    ventas = []
    
    for dia in dias:
        while True:
            try:
                venta = float(input(f"Ingrese las ventas del {dia}: $"))
                ventas.append(venta)
                break
            except ValueError:
                print("Error: Ingrese un número válido.")
    
    # Crear Serie con los datos
    serie_ventas = pd.Series(ventas, index=dias)
    
    print("\n" + "=" * 50)
    print("DATOS INGRESADOS:")
    print("=" * 50)
    print(serie_ventas)
    
    # Análisis
    total_ventas = serie_ventas.sum()
    promedio_ventas = serie_ventas.mean()
    dia_max_ventas = serie_ventas.idxmax()
    max_ventas = serie_ventas.max()
    
    print("\n" + "=" * 50)
    print("ANÁLISIS DE VENTAS:")
    print("=" * 50)
    print(f"Total de ventas: ${total_ventas:.2f}")
    print(f"Promedio de ventas: ${promedio_ventas:.2f}")
    print(f"Día con mayores ventas: {dia_max_ventas} (${max_ventas:.2f})")
    
    # Días con ventas por encima del promedio
    dias_sobre_promedio = serie_ventas[serie_ventas > promedio_ventas]
    
    print("\n" + "=" * 50)
    print("DÍAS CON VENTAS POR ENCIMA DEL PROMEDIO:")
    print("=" * 50)
    if len(dias_sobre_promedio) > 0:
        print(dias_sobre_promedio)
    else:
        print("No hay días con ventas por encima del promedio.")

if __name__ == "__main__":
    main()
