"""
Ejercicio 8: Análisis de Datos Meteorológicos
- Solicita al usuario las precipitaciones registradas durante los últimos 7 días.
- Crea una Serie con los datos.
- Identifica los días sin lluvia (0 mm) y reemplázalos con "Sin precipitación".
- Calcula el total y el promedio de precipitaciones.
- Muestra los días con precipitación por encima del promedio.
"""

import pandas as pd

def main():
    print("=" * 50)
    print("ANÁLISIS DE DATOS METEOROLÓGICOS")
    print("=" * 50)
    
    # Solicitar las precipitaciones
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    precipitaciones = []
    
    print("Ingrese las precipitaciones en milímetros (mm) para cada día.\n")
    
    for dia in dias:
        while True:
            try:
                precip = float(input(f"Ingrese la precipitación del {dia} (mm): "))
                if precip >= 0:
                    precipitaciones.append(precip)
                    break
                else:
                    print("Error: La precipitación debe ser un valor positivo o cero.")
            except ValueError:
                print("Error: Ingrese un número válido.")
    
    # Crear Serie con los datos
    serie_precipitaciones = pd.Series(precipitaciones, index=dias)
    
    print("\n" + "=" * 50)
    print("PRECIPITACIONES REGISTRADAS:")
    print("=" * 50)
    print(serie_precipitaciones)
    
    # Calcular total y promedio de precipitaciones
    total_precip = serie_precipitaciones.sum()
    promedio_precip = serie_precipitaciones.mean()
    
    print("\n" + "=" * 50)
    print("ESTADÍSTICAS DE PRECIPITACIÓN:")
    print("=" * 50)
    print(f"Total de precipitaciones: {total_precip:.2f} mm")
    print(f"Promedio de precipitaciones: {promedio_precip:.2f} mm")
    
    # Identificar días sin lluvia
    dias_sin_lluvia = serie_precipitaciones[serie_precipitaciones == 0]
    
    print("\n" + "=" * 50)
    print("DÍAS SIN LLUVIA:")
    print("=" * 50)
    if len(dias_sin_lluvia) > 0:
        print(dias_sin_lluvia.index.tolist())
    else:
        print("Todos los días tuvieron precipitación.")
    
    # Reemplazar días sin lluvia con "Sin precipitación"
    serie_modificada = serie_precipitaciones.copy()
    serie_modificada[serie_modificada == 0] = "Sin precipitación"
    
    print("\n" + "=" * 50)
    print("PRECIPITACIONES CON ESTADO:")
    print("=" * 50)
    print(serie_modificada)
    
    # Días con precipitación por encima del promedio
    dias_sobre_promedio = serie_precipitaciones[serie_precipitaciones > promedio_precip]
    
    print("\n" + "=" * 50)
    print(f"DÍAS CON PRECIPITACIÓN > PROMEDIO ({promedio_precip:.2f} mm):")
    print("=" * 50)
    if len(dias_sobre_promedio) > 0:
        print(dias_sobre_promedio)
    else:
        print("No hay días con precipitación por encima del promedio.")
    
    # Clasificación de precipitación
    print("\n" + "=" * 50)
    print("CLASIFICACIÓN DE PRECIPITACIÓN:")
    print("=" * 50)
    for dia, precip in serie_precipitaciones.items():
        if precip == 0:
            clasificacion = "Sin lluvia"
        elif precip < 2:
            clasificacion = "Lluvia ligera"
        elif precip < 10:
            clasificacion = "Lluvia moderada"
        else:
            clasificacion = "Lluvia intensa"
        print(f"{dia}: {precip:.2f} mm - {clasificacion}")

if __name__ == "__main__":
    main()
