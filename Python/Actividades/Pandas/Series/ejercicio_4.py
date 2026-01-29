"""
Ejercicio 4: Registro de Horas de Trabajo
- Solicita al usuario que ingrese las horas trabajadas por un empleado durante 5 días laborales.
- Crea una Serie con los datos.
- Calcula el total de horas trabajadas, y muestra los días en los que el empleado trabajó más de 8 horas.
- Reemplaza las horas menores a 6 con "Medio tiempo".
- Muestra una lista de días y su clasificación de horas (Normal, Medio tiempo, Extra).
"""

import pandas as pd

def main():
    print("=" * 50)
    print("REGISTRO DE HORAS DE TRABAJO")
    print("=" * 50)
    
    # Solicitar las horas trabajadas
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
    horas = []
    
    for dia in dias:
        while True:
            try:
                hora = float(input(f"Ingrese las horas trabajadas el {dia}: "))
                if hora >= 0:
                    horas.append(hora)
                    break
                else:
                    print("Error: Las horas deben ser un valor positivo.")
            except ValueError:
                print("Error: Ingrese un número válido.")
    
    # Crear Serie con los datos
    serie_horas = pd.Series(horas, index=dias)
    
    print("\n" + "=" * 50)
    print("HORAS TRABAJADAS:")
    print("=" * 50)
    print(serie_horas)
    
    # Calcular total de horas trabajadas
    total_horas = serie_horas.sum()
    
    print("\n" + "=" * 50)
    print("ANÁLISIS DE HORAS:")
    print("=" * 50)
    print(f"Total de horas trabajadas: {total_horas:.2f} horas")
    
    # Días con más de 8 horas
    dias_extra = serie_horas[serie_horas > 8]
    
    print("\n" + "=" * 50)
    print("DÍAS CON MÁS DE 8 HORAS:")
    print("=" * 50)
    if len(dias_extra) > 0:
        print(dias_extra)
    else:
        print("No hay días con más de 8 horas trabajadas.")
    
    # Crear clasificación de horas
    clasificacion = []
    for hora in serie_horas:
        if hora < 6:
            clasificacion.append("Medio tiempo")
        elif hora <= 8:
            clasificacion.append("Normal")
        else:
            clasificacion.append("Extra")
    
    serie_clasificacion = pd.Series(clasificacion, index=dias)
    
    print("\n" + "=" * 50)
    print("CLASIFICACIÓN DE HORAS:")
    print("=" * 50)
    print(serie_clasificacion)
    
    # Crear serie modificada con "Medio tiempo" para horas < 6
    serie_modificada = serie_horas.copy()
    serie_modificada[serie_modificada < 6] = "Medio tiempo"
    
    print("\n" + "=" * 50)
    print("HORAS CON REEMPLAZO (< 6 horas):")
    print("=" * 50)
    print(serie_modificada)
    
    # Resumen por clasificación
    print("\n" + "=" * 50)
    print("RESUMEN POR CLASIFICACIÓN:")
    print("=" * 50)
    conteo = serie_clasificacion.value_counts()
    print(conteo)

if __name__ == "__main__":
    main()
