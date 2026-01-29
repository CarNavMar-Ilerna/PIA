"""
Ejercicio 3: Análisis de Temperaturas Semanales
- Solicita al usuario las temperaturas registradas en una semana (7 días).
- Crea una Serie con los datos y calcula la temperatura máxima y mínima.
- Identifica los días que tienen temperaturas por encima de 25°C.
- Rellena posibles valores faltantes (NaN) con la temperatura promedio.
- Grafica las temperaturas de la semana.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    print("=" * 50)
    print("ANÁLISIS DE TEMPERATURAS SEMANALES")
    print("=" * 50)
    
    # Solicitar las temperaturas
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    temperaturas = []
    
    print("Nota: Ingrese 'NaN' si no hay dato disponible para un día.")
    
    for dia in dias:
        while True:
            try:
                temp_input = input(f"Ingrese la temperatura del {dia} (°C): ")
                if temp_input.upper() == 'NAN':
                    temperaturas.append(np.nan)
                    break
                else:
                    temp = float(temp_input)
                    temperaturas.append(temp)
                    break
            except ValueError:
                print("Error: Ingrese un número válido o 'NaN'.")
    
    # Crear Serie con los datos
    serie_temperaturas = pd.Series(temperaturas, index=dias)
    
    print("\n" + "=" * 50)
    print("TEMPERATURAS INGRESADAS:")
    print("=" * 50)
    print(serie_temperaturas)
    
    # Calcular temperatura máxima y mínima
    temp_max = serie_temperaturas.max()
    temp_min = serie_temperaturas.min()
    
    print("\n" + "=" * 50)
    print("ANÁLISIS DE TEMPERATURAS:")
    print("=" * 50)
    print(f"Temperatura máxima: {temp_max:.2f}°C")
    print(f"Temperatura mínima: {temp_min:.2f}°C")
    
    # Días con temperaturas por encima de 25°C
    dias_calurosos = serie_temperaturas[serie_temperaturas > 25]
    
    print("\n" + "=" * 50)
    print("DÍAS CON TEMPERATURA > 25°C:")
    print("=" * 50)
    if len(dias_calurosos) > 0:
        print(dias_calurosos)
    else:
        print("No hay días con temperatura superior a 25°C.")
    
    # Rellenar valores faltantes con la temperatura promedio
    if serie_temperaturas.isna().any():
        promedio = serie_temperaturas.mean()
        serie_temperaturas_completa = serie_temperaturas.fillna(promedio)
        print("\n" + "=" * 50)
        print(f"VALORES FALTANTES RELLENADOS CON PROMEDIO ({promedio:.2f}°C):")
        print("=" * 50)
        print(serie_temperaturas_completa)
    else:
        serie_temperaturas_completa = serie_temperaturas
        print("\nNo hay valores faltantes.")
    
    # Graficar las temperaturas
    plt.figure(figsize=(10, 6))
    plt.plot(serie_temperaturas_completa.index, serie_temperaturas_completa.values, 
             marker='o', linewidth=2, markersize=8, color='#ff6b35')
    plt.axhline(y=25, color='red', linestyle='--', label='Umbral 25°C')
    plt.title('Temperaturas de la Semana', fontsize=16, fontweight='bold')
    plt.xlabel('Día de la Semana', fontsize=12)
    plt.ylabel('Temperatura (°C)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
