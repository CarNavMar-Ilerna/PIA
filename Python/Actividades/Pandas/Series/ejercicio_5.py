"""
Ejercicio 5: Inventario de Productos
- Pide al usuario que ingrese la cantidad de 8 productos diferentes en stock.
- Crea una Serie y asigna nombres de productos como índice.
- Muestra los productos con menos de 10 unidades.
- Rellena cualquier valor faltante (NaN) con 0.
- Muestra los productos ordenados por la cantidad en stock.
"""

import pandas as pd
import numpy as np

def main():
    print("=" * 50)
    print("INVENTARIO DE PRODUCTOS")
    print("=" * 50)
    
    # Solicitar nombres de productos y cantidades
    num_productos = 8
    productos = []
    cantidades = []
    
    print("Nota: Ingrese 'NaN' si no hay dato disponible para un producto.\n")
    
    for i in range(num_productos):
        nombre_producto = input(f"Ingrese el nombre del producto {i+1}: ")
        productos.append(nombre_producto)
        
        while True:
            try:
                cantidad_input = input(f"Ingrese la cantidad en stock de '{nombre_producto}': ")
                if cantidad_input.upper() == 'NAN':
                    cantidades.append(np.nan)
                    break
                else:
                    cantidad = int(cantidad_input)
                    if cantidad >= 0:
                        cantidades.append(cantidad)
                        break
                    else:
                        print("Error: La cantidad debe ser un valor positivo.")
            except ValueError:
                print("Error: Ingrese un número entero válido o 'NaN'.")
    
    # Crear Serie con los datos
    serie_inventario = pd.Series(cantidades, index=productos)
    
    print("\n" + "=" * 50)
    print("INVENTARIO ACTUAL:")
    print("=" * 50)
    print(serie_inventario)
    
    # Productos con menos de 10 unidades
    productos_bajos = serie_inventario[serie_inventario < 10]
    
    print("\n" + "=" * 50)
    print("PRODUCTOS CON MENOS DE 10 UNIDADES:")
    print("=" * 50)
    if len(productos_bajos) > 0:
        print(productos_bajos)
        print(f"\nALERTA: {len(productos_bajos)} productos requieren reabastecimiento.")
    else:
        print("Todos los productos tienen stock suficiente.")
    
    # Rellenar valores faltantes con 0
    if serie_inventario.isna().any():
        serie_inventario_completo = serie_inventario.fillna(0)
        print("\n" + "=" * 50)
        print("INVENTARIO CON VALORES FALTANTES RELLENADOS (0):")
        print("=" * 50)
        print(serie_inventario_completo)
    else:
        serie_inventario_completo = serie_inventario
        print("\nNo hay valores faltantes en el inventario.")
    
    # Productos ordenados por cantidad en stock
    serie_ordenada = serie_inventario_completo.sort_values(ascending=False)
    
    print("\n" + "=" * 50)
    print("PRODUCTOS ORDENADOS POR CANTIDAD (Mayor a Menor):")
    print("=" * 50)
    print(serie_ordenada)
    
    # Estadísticas del inventario
    print("\n" + "=" * 50)
    print("ESTADÍSTICAS DEL INVENTARIO:")
    print("=" * 50)
    print(f"Total de unidades en stock: {serie_inventario_completo.sum():.0f}")
    print(f"Promedio de unidades por producto: {serie_inventario_completo.mean():.2f}")

if __name__ == "__main__":
    main()
