"""
Ejercicio 10: Análisis de Puntuaciones de Juegos
- Solicita al usuario las puntuaciones de un jugador en 8 rondas de un juego.
- Crea una Serie con las puntuaciones y asigna números de ronda como índice.
- Calcula la puntuación máxima, mínima y la diferencia entre la más alta y la más baja.
- Muestra las rondas en las que la puntuación es superior a 80.
- Ordena las puntuaciones de menor a mayor y muestra el ranking.
"""

import pandas as pd

def main():
    print("=" * 50)
    print("ANÁLISIS DE PUNTUACIONES DE JUEGOS")
    print("=" * 50)
    
    # Solicitar las puntuaciones
    num_rondas = 8
    puntuaciones = []
    rondas = [f"Ronda {i+1}" for i in range(num_rondas)]
    
    print("Ingrese las puntuaciones del jugador en cada ronda.\n")
    
    for i in range(num_rondas):
        while True:
            try:
                puntuacion = float(input(f"Ingrese la puntuación de la ronda {i+1}: "))
                if puntuacion >= 0:
                    puntuaciones.append(puntuacion)
                    break
                else:
                    print("Error: La puntuación debe ser un valor positivo o cero.")
            except ValueError:
                print("Error: Ingrese un número válido.")
    
    # Crear Serie con las puntuaciones
    serie_puntuaciones = pd.Series(puntuaciones, index=rondas)
    
    print("\n" + "=" * 50)
    print("PUNTUACIONES REGISTRADAS:")
    print("=" * 50)
    print(serie_puntuaciones)
    
    # Calcular puntuación máxima y mínima
    punt_max = serie_puntuaciones.max()
    punt_min = serie_puntuaciones.min()
    ronda_max = serie_puntuaciones.idxmax()
    ronda_min = serie_puntuaciones.idxmin()
    diferencia = punt_max - punt_min
    
    print("\n" + "=" * 50)
    print("ESTADÍSTICAS DE PUNTUACIONES:")
    print("=" * 50)
    print(f"Puntuación máxima: {punt_max:.2f} ({ronda_max})")
    print(f"Puntuación mínima: {punt_min:.2f} ({ronda_min})")
    print(f"Diferencia: {diferencia:.2f}")
    print(f"Promedio: {serie_puntuaciones.mean():.2f}")
    print(f"Mediana: {serie_puntuaciones.median():.2f}")
    
    # Rondas con puntuación superior a 80
    rondas_altas = serie_puntuaciones[serie_puntuaciones > 80]
    
    print("\n" + "=" * 50)
    print("RONDAS CON PUNTUACIÓN > 80:")
    print("=" * 50)
    if len(rondas_altas) > 0:
        print(rondas_altas)
        print(f"\nRendimiento destacado en {len(rondas_altas)} de {num_rondas} rondas.")
    else:
        print("No hay rondas con puntuación superior a 80.")
    
    # Ordenar puntuaciones de menor a mayor
    serie_ordenada = serie_puntuaciones.sort_values(ascending=True)
    
    print("\n" + "=" * 50)
    print("PUNTUACIONES ORDENADAS (Menor a Mayor):")
    print("=" * 50)
    print(serie_ordenada)
    
    # Crear ranking (de mayor a menor)
    serie_ranking = serie_puntuaciones.sort_values(ascending=False)
    
    print("\n" + "=" * 50)
    print("RANKING DE MEJORES RONDAS:")
    print("=" * 50)
    for i, (ronda, puntuacion) in enumerate(serie_ranking.items(), 1):
        medalla = ""
        if i == 1:
            medalla = "🥇"
        elif i == 2:
            medalla = "🥈"
        elif i == 3:
            medalla = "🥉"
        print(f"{i}. {ronda}: {puntuacion:.2f} puntos {medalla}")
    
    # Análisis de tendencia
    print("\n" + "=" * 50)
    print("ANÁLISIS DE RENDIMIENTO:")
    print("=" * 50)
    
    # Comparar primera y última ronda
    primera_puntuacion = serie_puntuaciones.iloc[0]
    ultima_puntuacion = serie_puntuaciones.iloc[-1]
    mejora = ultima_puntuacion - primera_puntuacion
    
    if mejora > 0:
        print(f"✓ El jugador mejoró su rendimiento: +{mejora:.2f} puntos")
    elif mejora < 0:
        print(f"⚠ El jugador empeoró su rendimiento: {mejora:.2f} puntos")
    else:
        print("= El jugador mantuvo el mismo rendimiento")
    
    # Consistencia
    desviacion = serie_puntuaciones.std()
    if desviacion < 10:
        consistencia = "Alta consistencia"
    elif desviacion < 20:
        consistencia = "Consistencia moderada"
    else:
        consistencia = "Baja consistencia (rendimiento variable)"
    
    print(f"Desviación estándar: {desviacion:.2f} - {consistencia}")

if __name__ == "__main__":
    main()
