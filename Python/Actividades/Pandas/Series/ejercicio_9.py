"""
Ejercicio 9: Registro de Visitas a una Página Web
- Pide al usuario que ingrese el número de visitas diarias a una página web durante 10 días.
- Crea una Serie con los datos.
- Calcula el total y el promedio de visitas diarias.
- Muestra los días con más visitas que el promedio y reemplaza los valores de visitas < 50 con "Baja visita".
- Grafica el número de visitas diarias.
"""

import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("=" * 50)
    print("REGISTRO DE VISITAS A UNA PÁGINA WEB")
    print("=" * 50)
    
    # Solicitar las visitas diarias
    num_dias = 10
    visitas = []
    dias = [f"Día {i+1}" for i in range(num_dias)]
    
    print("Ingrese el número de visitas diarias.\n")
    
    for i in range(num_dias):
        while True:
            try:
                visita = int(input(f"Ingrese las visitas del día {i+1}: "))
                if visita >= 0:
                    visitas.append(visita)
                    break
                else:
                    print("Error: El número de visitas debe ser un valor positivo o cero.")
            except ValueError:
                print("Error: Ingrese un número entero válido.")
    
    # Crear Serie con los datos
    serie_visitas = pd.Series(visitas, index=dias)
    
    print("\n" + "=" * 50)
    print("VISITAS DIARIAS REGISTRADAS:")
    print("=" * 50)
    print(serie_visitas)
    
    # Calcular total y promedio de visitas
    total_visitas = serie_visitas.sum()
    promedio_visitas = serie_visitas.mean()
    
    print("\n" + "=" * 50)
    print("ESTADÍSTICAS DE VISITAS:")
    print("=" * 50)
    print(f"Total de visitas: {total_visitas}")
    print(f"Promedio de visitas diarias: {promedio_visitas:.2f}")
    print(f"Visitas máximas: {serie_visitas.max()}")
    print(f"Visitas mínimas: {serie_visitas.min()}")
    
    # Días con más visitas que el promedio
    dias_sobre_promedio = serie_visitas[serie_visitas > promedio_visitas]
    
    print("\n" + "=" * 50)
    print(f"DÍAS CON VISITAS > PROMEDIO ({promedio_visitas:.2f}):")
    print("=" * 50)
    if len(dias_sobre_promedio) > 0:
        print(dias_sobre_promedio)
    else:
        print("No hay días con visitas por encima del promedio.")
    
    # Reemplazar visitas < 50 con "Baja visita"
    serie_modificada = serie_visitas.copy()
    serie_modificada[serie_modificada < 50] = "Baja visita"
    
    print("\n" + "=" * 50)
    print("VISITAS CON CLASIFICACIÓN (<50):")
    print("=" * 50)
    print(serie_modificada)
    
    # Clasificación de visitas
    print("\n" + "=" * 50)
    print("CLASIFICACIÓN DE TRÁFICO:")
    print("=" * 50)
    for dia, visita in serie_visitas.items():
        if visita < 50:
            categoria = "Baja visita"
        elif visita < 100:
            categoria = "Visitas moderadas"
        elif visita < 200:
            categoria = "Buen tráfico"
        else:
            categoria = "Alto tráfico"
        print(f"{dia}: {visita} visitas - {categoria}")
    
    # Graficar las visitas diarias
    plt.figure(figsize=(12, 6))
    
    # Colores según el umbral de 50 visitas
    colors = ['#e74c3c' if v < 50 else '#2ecc71' for v in serie_visitas]
    
    plt.bar(serie_visitas.index, serie_visitas.values, color=colors, alpha=0.8)
    plt.axhline(y=promedio_visitas, color='blue', linestyle='--', linewidth=2, 
                label=f'Promedio: {promedio_visitas:.2f}')
    plt.axhline(y=50, color='orange', linestyle=':', linewidth=2, 
                label='Umbral: 50 visitas')
    
    plt.title('Visitas Diarias a la Página Web', fontsize=16, fontweight='bold')
    plt.xlabel('Día', fontsize=12)
    plt.ylabel('Número de Visitas', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, alpha=0.3, axis='y')
    plt.legend()
    
    # Añadir etiquetas de valor en las barras
    for i, v in enumerate(serie_visitas.values):
        plt.text(i, v + (serie_visitas.max() * 0.02), str(v), 
                ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.show()
    
    print("\n✓ Gráfico generado exitosamente.")

if __name__ == "__main__":
    main()
