"""
Ejercicio 7: Análisis de Precio de un Producto en Tiendas
- Pide al usuario que ingrese los precios de un producto en 5 tiendas diferentes.
- Crea una Serie y nombra cada tienda como índice.
- Muestra el precio más bajo y más alto.
- Identifica las tiendas con precios por encima de la mediana.
- Rellena los precios faltantes (NaN) con el precio promedio y grafica los precios.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    print("=" * 50)
    print("ANÁLISIS DE PRECIO DE UN PRODUCTO EN TIENDAS")
    print("=" * 50)
    
    # Solicitar nombre del producto
    producto = input("Ingrese el nombre del producto a comparar: ")
    
    # Solicitar nombres de tiendas y precios
    num_tiendas = 5
    tiendas = []
    precios = []
    
    print(f"\nIngrese los precios de '{producto}' en diferentes tiendas.")
    print("Nota: Ingrese 'NaN' si el precio no está disponible.\n")
    
    for i in range(num_tiendas):
        nombre_tienda = input(f"Ingrese el nombre de la tienda {i+1}: ")
        tiendas.append(nombre_tienda)
        
        while True:
            try:
                precio_input = input(f"Ingrese el precio en '{nombre_tienda}': $")
                if precio_input.upper() == 'NAN':
                    precios.append(np.nan)
                    break
                else:
                    precio = float(precio_input)
                    if precio >= 0:
                        precios.append(precio)
                        break
                    else:
                        print("Error: El precio debe ser un valor positivo.")
            except ValueError:
                print("Error: Ingrese un número válido o 'NaN'.")
    
    # Crear Serie con los datos
    serie_precios = pd.Series(precios, index=tiendas)
    
    print("\n" + "=" * 50)
    print(f"PRECIOS DE '{producto.upper()}':")
    print("=" * 50)
    print(serie_precios)
    
    # Calcular precio más bajo y más alto
    precio_min = serie_precios.min()
    precio_max = serie_precios.max()
    tienda_min = serie_precios.idxmin()
    tienda_max = serie_precios.idxmax()
    
    print("\n" + "=" * 50)
    print("ANÁLISIS DE PRECIOS:")
    print("=" * 50)
    print(f"Precio más bajo: ${precio_min:.2f} ({tienda_min})")
    print(f"Precio más alto: ${precio_max:.2f} ({tienda_max})")
    print(f"Diferencia: ${precio_max - precio_min:.2f}")
    
    # Calcular mediana
    mediana = serie_precios.median()
    print(f"Precio mediana: ${mediana:.2f}")
    
    # Tiendas con precios por encima de la mediana
    tiendas_caras = serie_precios[serie_precios > mediana]
    
    print("\n" + "=" * 50)
    print("TIENDAS CON PRECIOS POR ENCIMA DE LA MEDIANA:")
    print("=" * 50)
    if len(tiendas_caras) > 0:
        print(tiendas_caras)
    else:
        print("No hay tiendas con precios por encima de la mediana.")
    
    # Rellenar precios faltantes con el precio promedio
    if serie_precios.isna().any():
        promedio = serie_precios.mean()
        serie_precios_completa = serie_precios.fillna(promedio)
        print("\n" + "=" * 50)
        print(f"PRECIOS CON VALORES FALTANTES RELLENADOS (${promedio:.2f}):")
        print("=" * 50)
        print(serie_precios_completa)
    else:
        serie_precios_completa = serie_precios
        print("\nNo hay precios faltantes.")
    
    # Graficar los precios
    plt.figure(figsize=(10, 6))
    colors = ['#3498db' if precio <= mediana else '#e74c3c' for precio in serie_precios_completa]
    plt.bar(serie_precios_completa.index, serie_precios_completa.values, color=colors, alpha=0.8)
    plt.axhline(y=mediana, color='green', linestyle='--', linewidth=2, 
                label=f'Mediana: ${mediana:.2f}')
    plt.title(f'Comparación de Precios de {producto}', fontsize=16, fontweight='bold')
    plt.xlabel('Tiendas', fontsize=12)
    plt.ylabel('Precio ($)', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, alpha=0.3, axis='y')
    plt.legend()
    
    # Añadir etiquetas de valor en las barras
    for i, (tienda, precio) in enumerate(serie_precios_completa.items()):
        plt.text(i, precio + (precio_max * 0.02), f'${precio:.2f}', 
                ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.show()
    
    print("\n✓ Gráfico generado exitosamente.")

if __name__ == "__main__":
    main()
