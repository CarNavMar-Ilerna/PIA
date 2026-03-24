import pandas as pd
import os
import subprocess
import sys

# ─────────────────────────────────────────────────────────────────────────────
# PASO 0: Generar el Excel si no existe
# ─────────────────────────────────────────────────────────────────────────────
script_dir = os.path.dirname(os.path.abspath(__file__))
ruta_excel = os.path.join(script_dir, "vehiculos.xlsx")

if not os.path.exists(ruta_excel):
    generador = os.path.join(script_dir, "generar_excel.py")
    subprocess.run([sys.executable, generador], check=True)


# ─────────────────────────────────────────────────────────────────────────────
# 1. CARGA DE DATOS DESDE EXCEL
#    Se carga el archivo Excel en un DataFrame manteniendo el formato original.
#    Los valores nulos se rellenan con valores apropiados según el tipo de dato.
# ─────────────────────────────────────────────────────────────────────────────
def cargar_datos(ruta):
    """Carga el Excel de vehículos, aplica tipos de datos correctos y gestiona nulos."""
    df = pd.read_excel(ruta)

    # Rellenar nulos numéricos con la mediana de cada columna
    columnas_numericas = ["Kilómetros", "Emisiones", "Autonomía", "C_Maletero", "Peso", "N_Ocupantes", "Precio"]
    for col in columnas_numericas:
        if col in df.columns:
            mediana = df[col].median()
            df[col] = df[col].fillna(mediana)

    # Rellenar nulos de texto con "Desconocido"
    columnas_texto = ["Marca", "Modelo", "Color", "Motor", "Combustible", "Tamaño", "Potencia"]
    for col in columnas_texto:
        if col in df.columns:
            df[col] = df[col].fillna("Desconocido")

    # Asegurar tipos de datos correctos
    df["N_ID"] = df["N_ID"].astype(int)
    df["Anyo"] = df["Anyo"].astype(int)
    df["Kilómetros"] = df["Kilómetros"].astype(int)
    df["N_Ocupantes"] = df["N_Ocupantes"].astype(int)
    df["Peso"] = df["Peso"].astype(int)
    df["C_Maletero"] = df["C_Maletero"].astype(int)
    df["Autonomía"] = df["Autonomía"].astype(int)
    df["Emisiones"] = df["Emisiones"].round(2)
    df["Precio"] = df["Precio"].round(2)

    return df


# ─────────────────────────────────────────────────────────────────────────────
# 2. EDICIÓN Y COMPROBACIÓN DE DATOS
#    Revisión de la totalidad de registros y corrección de datos incorrectos.
# ─────────────────────────────────────────────────────────────────────────────
def revisar_datos(df):
    """Muestra información general del DataFrame: total de registros, tipos y nulos."""
    print("=" * 60)
    print("REVISIÓN DE DATOS")
    print("=" * 60)
    print(f"Total de registros cargados : {len(df)}")
    print(f"Total de columnas           : {len(df.columns)}")
    print(f"\nColumnas y tipos de datos:")
    print(df.dtypes.to_string())
    print(f"\nValores nulos por columna:")
    nulos = df.isnull().sum()
    print(nulos[nulos > 0].to_string() if nulos.sum() > 0 else "  Sin valores nulos.")
    print(f"\nPrimeros 5 registros:")
    print(df.head().to_string(index=False))
    print()


# ─────────────────────────────────────────────────────────────────────────────
# 3. ANÁLISIS ESTADÍSTICO
#    Cálculo de estadísticas descriptivas y exportación a Excel.
# ─────────────────────────────────────────────────────────────────────────────
def analisis_estadistico(df, ruta_salida):
    """Genera estadísticas descriptivas de columnas numéricas y las guarda en Excel."""
    print("=" * 60)
    print("ANÁLISIS ESTADÍSTICO")
    print("=" * 60)

    columnas_numericas = ["Precio", "Kilómetros", "Emisiones", "Autonomía", "Peso", "C_Maletero"]

    stats = df[columnas_numericas].describe().round(2)
    print(stats.to_string())
    print()

    # Estadísticas personalizadas adicionales
    print(f"Precio medio          : {df['Precio'].mean():,.2f} €")
    print(f"Precio mediano        : {df['Precio'].median():,.2f} €")
    print(f"Kilómetros promedio   : {df['Kilómetros'].mean():,.0f} km")
    print(f"Emisiones promedio    : {df['Emisiones'].mean():.2f} g/km CO₂")
    print(f"Autonomía promedio    : {df['Autonomía'].mean():.0f} km")

    # Precio por tipo de combustible
    precio_combustible = df.groupby("Combustible")["Precio"].mean().round(2).reset_index()
    precio_combustible.columns = ["Combustible", "Precio Medio (€)"]
    print(f"\nPrecio medio por tipo de combustible:")
    print(precio_combustible.to_string(index=False))

    # Exportar a Excel
    with pd.ExcelWriter(ruta_salida, engine="xlsxwriter") as writer:
        stats.to_excel(writer, sheet_name="Estadísticas Generales")
        precio_combustible.to_excel(writer, sheet_name="Precio por Combustible", index=False)

    print(f"\nEstadísticas exportadas a: {ruta_salida}\n")


# ─────────────────────────────────────────────────────────────────────────────
# 4. FILTRADO DE VEHÍCULOS
#    Permite filtrar el DataFrame por marca, modelo, año, precio y color.
# ─────────────────────────────────────────────────────────────────────────────
def filtrar_vehiculos(df, marca=None, modelo=None, anyo=None, precio_max=None, color=None):
    """
    Filtra el DataFrame según los criterios indicados.
    Todos los parámetros son opcionales.
    """
    resultado = df.copy()

    if marca:
        resultado = resultado[resultado["Marca"].str.lower() == marca.lower()]
    if modelo:
        resultado = resultado[resultado["Modelo"].str.lower() == modelo.lower()]
    if anyo:
        resultado = resultado[resultado["Anyo"] == anyo]
    if precio_max:
        resultado = resultado[resultado["Precio"] <= precio_max]
    if color:
        resultado = resultado[resultado["Color"].str.lower() == color.lower()]

    return resultado


# ─────────────────────────────────────────────────────────────────────────────
# 5. ORDENACIÓN DE DATOS
#    Ordena el DataFrame por columna y dirección indicadas.
# ─────────────────────────────────────────────────────────────────────────────
def ordenar_datos(df, columna, ascendente=True):
    """Ordena el DataFrame por la columna indicada en orden ascendente o descendente."""
    return df.sort_values(by=columna, ascending=ascendente).reset_index(drop=True)


# ─────────────────────────────────────────────────────────────────────────────
# 6. TRANSFORMACIÓN DE DATOS
#    Calcula la depreciación del vehículo según el año y los kilómetros.
# ─────────────────────────────────────────────────────────────────────────────
def calcular_depreciacion(df, anyo_actual=2025):
    """
    Calcula el valor de mercado estimado aplicando depreciación:
    - Año 1: 20% de pérdida.
    - Años 2-5: 10% anual adicional.
    - Años 6+: 5% anual adicional.
    - Deducción adicional por kilómetros: 0.001 € por km por encima de 15.000 km/año.
    """
    df = df.copy()

    def depreciacion(row):
        antiguedad = anyo_actual - row["Anyo"]
        precio = row["Precio"]

        if antiguedad <= 0:
            factor = 1.0
        elif antiguedad == 1:
            factor = 0.80
        elif antiguedad <= 5:
            factor = 0.80 * (0.90 ** (antiguedad - 1))
        else:
            factor = 0.80 * (0.90 ** 4) * (0.95 ** (antiguedad - 5))

        # Penalización por exceso de kilómetros
        km_esperados = antiguedad * 15000
        km_extra = max(0, row["Kilómetros"] - km_esperados)
        penalizacion_km = km_extra * 0.001

        valor_estimado = max(precio * factor - penalizacion_km, precio * 0.05)
        return round(valor_estimado, 2)

    df["Valor Estimado (€)"] = df.apply(depreciacion, axis=1)
    df["Depreciación (%)"] = (((df["Precio"] - df["Valor Estimado (€)"]) / df["Precio"]) * 100).round(2)

    return df


# ─────────────────────────────────────────────────────────────────────────────
# 7. EXPORTAR A CSV
#    Guarda el DataFrame con todas las transformaciones en formato CSV.
# ─────────────────────────────────────────────────────────────────────────────
def exportar_csv(df, ruta_csv):
    """Exporta el DataFrame a un archivo CSV con separador punto y coma."""
    df.to_csv(ruta_csv, index=False, sep=";", encoding="utf-8-sig")
    print(f"Datos exportados a CSV: {ruta_csv}")


# ─────────────────────────────────────────────────────────────────────────────
# EJECUCIÓN PRINCIPAL
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":

    # 1. Cargar datos
    df = cargar_datos(ruta_excel)

    # 2. Revisión y comprobación
    revisar_datos(df)

    # 3. Análisis estadístico -> exportar a Excel
    ruta_stats = os.path.join(script_dir, "estadisticas_vehiculos.xlsx")
    analisis_estadistico(df, ruta_stats)

    # 4. Ejemplos de filtrado
    print("=" * 60)
    print("FILTRADO DE VEHÍCULOS")
    print("=" * 60)

    print("\nVehículos SEAT:")
    seat = filtrar_vehiculos(df, marca="SEAT")
    print(seat[["Marca", "Modelo", "Anyo", "Color", "Precio"]].to_string(index=False))

    print("\nVehículos eléctricos con precio máximo 40.000 €:")
    electricos = filtrar_vehiculos(df, precio_max=40000)
    electricos = electricos[electricos["Combustible"] == "Eléctrico"]
    print(electricos[["Marca", "Modelo", "Combustible", "Autonomía", "Precio"]].to_string(index=False))

    print("\nVehículos de color Negro del año 2022:")
    negros_22 = filtrar_vehiculos(df, anyo=2022, color="Negro")
    print(negros_22[["Marca", "Modelo", "Anyo", "Color", "Precio"]].to_string(index=False))

    # 5. Ordenación de datos
    print("\n" + "=" * 60)
    print("ORDENACIÓN DE DATOS")
    print("=" * 60)

    print("\n5 vehículos más baratos:")
    baratos = ordenar_datos(df, "Precio", ascendente=True).head(5)
    print(baratos[["Marca", "Modelo", "Anyo", "Precio"]].to_string(index=False))

    print("\n5 vehículos con más kilómetros:")
    mas_km = ordenar_datos(df, "Kilómetros", ascendente=False).head(5)
    print(mas_km[["Marca", "Modelo", "Anyo", "Kilómetros"]].to_string(index=False))

    print("\n5 vehículos más recientes:")
    recientes = ordenar_datos(df, "Anyo", ascendente=False).head(5)
    print(recientes[["Marca", "Modelo", "Anyo", "Precio"]].to_string(index=False))

    # 6. Transformación: depreciación
    print("\n" + "=" * 60)
    print("TRANSFORMACIÓN: DEPRECIACIÓN")
    print("=" * 60)
    df_depreciado = calcular_depreciacion(df)
    print("\nValor estimado y depreciación de los primeros 10 vehículos:")
    print(df_depreciado[["Marca", "Modelo", "Anyo", "Kilómetros", "Precio",
                          "Valor Estimado (€)", "Depreciación (%)"]].head(10).to_string(index=False))

    print(f"\nDepreciación media: {df_depreciado['Depreciación (%)'].mean():.2f}%")
    print(f"Vehículo con mayor depreciación: "
          f"{df_depreciado.loc[df_depreciado['Depreciación (%)'].idxmax(), 'Marca']} "
          f"{df_depreciado.loc[df_depreciado['Depreciación (%)'].idxmax(), 'Modelo']}")

    # 7. Exportar a CSV con todas las transformaciones
    ruta_csv = os.path.join(script_dir, "vehiculos_datos.csv")
    exportar_csv(df_depreciado, ruta_csv)

    print("\n¡Proceso completado correctamente!")
