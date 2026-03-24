# Carlos Navarro Martinez

# Tarea - Ejercicios Matplotlib

import math
import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ===========================================================
# Ejercicio 01: Gráfico de dispersión - raíces cuadradas de valores aleatorios
# random.randint genera enteros aleatorios; math.sqrt calcula la raíz cuadrada
# plt.scatter dibuja un gráfico de dispersión con puntos
print("Ejercicio 01 - Gráfico de dispersión: 20 enteros aleatorios vs su raíz cuadrada")

x_vals = [random.randint(0, 100) for _ in range(20)]
y_vals = [math.sqrt(x) for x in x_vals]

plt.figure(figsize=(8, 5))
plt.scatter(x_vals, y_vals, color='steelblue', s=80, edgecolors='navy', zorder=3)
plt.title("Ejercicio 01 - Raíz cuadrada de valores aleatorios")
plt.xlabel("Valor entero aleatorio (0-100)")
plt.ylabel("Raíz cuadrada")
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("ejercicio01.png", dpi=150)
plt.show()
print("  Gráfico guardado como ejercicio01.png\n")


# ===========================================================
# Ejercicio 02: Diagrama de líneas con evolución de ventas por años
# input() solicita datos al usuario; plt.plot() dibuja líneas
print("Ejercicio 02 - Evolución de ventas por años (entrada de usuario)")

inicio = int(input("  Año de inicio: "))
fin = int(input("  Año de fin: "))
años = list(range(inicio, fin + 1))
ventas = []
for año in años:
    v = float(input(f"  Ventas del año {año}: "))
    ventas.append(v)

plt.figure(figsize=(9, 5))
plt.plot(años, ventas, marker='o', color='darkorange', linewidth=2, markersize=7)
plt.title("Ejercicio 02 - Evolución de Ventas")
plt.xlabel("Año")
plt.ylabel("Ventas")
plt.xticks(años)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("ejercicio02.png", dpi=150)
plt.show()
print("  Gráfico guardado como ejercicio02.png\n")


# ===========================================================
# Ejercicio 03: Diagrama de barras de notas de asignaturas con color personalizado
# La función recibe un diccionario {asignatura: nota} y nombre de color
def diagrama_notas_barras(notas_dict, color):
    """Genera un diagrama de barras con las notas recibidas en el color indicado."""
    # plt.bar(x, height, color) dibuja las barras verticales
    asignaturas = list(notas_dict.keys())
    notas = list(notas_dict.values())
    plt.figure(figsize=(9, 5))
    plt.bar(asignaturas, notas, color=color, edgecolor='black', alpha=0.85)
    plt.title("Ejercicio 03 - Notas por Asignatura")
    plt.xlabel("Asignatura")
    plt.ylabel("Nota")
    plt.ylim(0, 10)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig("ejercicio03.png", dpi=150)
    plt.show()

print("Ejercicio 03 - Diagrama de barras de notas")
notas_ejemplo = {
    "Matemáticas": 8.5,
    "Lengua": 7.0,
    "Historia": 9.0,
    "Inglés": 6.5,
    "Física": 7.8,
    "Programación": 9.5
}
diagrama_notas_barras(notas_ejemplo, "mediumseagreen")
print("  Gráfico guardado como ejercicio03.png\n")


# ===========================================================
# Ejercicio 04: Diagrama de cajas (boxplot) con notas de alumnos
# La función recibe una Serie de Pandas con notas
# plt.boxplot() muestra la distribución estadística de los datos
def diagrama_cajas_notas(serie_notas):
    """Genera un boxplot con las notas de los alumnos."""
    plt.figure(figsize=(6, 6))
    plt.boxplot(serie_notas, patch_artist=True,
                boxprops=dict(facecolor='lightskyblue', color='navy'),
                medianprops=dict(color='red', linewidth=2))
    plt.title("Distribución de Notas")
    plt.ylabel("Nota")
    plt.ylim(0, 10)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig("ejercicio04.png", dpi=150)
    plt.show()

print("Ejercicio 04 - Diagrama de cajas: distribución de notas")
notas_alumnos = pd.Series([5.5, 7.0, 8.5, 6.0, 9.0, 4.5, 7.5, 6.5, 8.0, 5.0,
                            9.5, 7.0, 6.0, 8.0, 7.5, 5.5, 6.5, 9.0, 4.0, 7.0])
diagrama_cajas_notas(notas_alumnos)
print("  Gráfico guardado como ejercicio04.png\n")


# ===========================================================
# Ejercicio 05: Diagrama de sectores (pie chart) de ventas trimestrales
# La función recibe una Serie de Pandas con ventas mensuales y un título
# El gráfico se guarda como PNG con el nombre del título
def diagrama_sectores_ventas(serie_ventas, titulo):
    """Genera un pie chart con las ventas del trimestre y lo guarda como PNG."""
    # plt.pie() dibuja el diagrama de sectores; autopct muestra porcentajes
    plt.figure(figsize=(7, 7))
    plt.pie(serie_ventas.values, labels=serie_ventas.index,
            autopct='%1.1f%%', startangle=90,
            colors=['#FF9999', '#66B2FF', '#99FF99'])
    plt.title(titulo)
    nombre_fichero = titulo.replace(" ", "_") + ".png"
    plt.tight_layout()
    plt.savefig(nombre_fichero, dpi=150)
    plt.show()
    return nombre_fichero

print("Ejercicio 05 - Diagrama de sectores: ventas trimestrales")
ventas_trimestre = pd.Series(
    [1200, 1850, 1600],
    index=["Enero", "Febrero", "Marzo"]
)
fichero = diagrama_sectores_ventas(ventas_trimestre, "Ventas Trimestre 1")
print(f"  Gráfico guardado como {fichero}\n")


# ===========================================================
# Ejercicio 06: Diagrama del tipo indicado con evolución de ventas anuales
# La función recibe una Serie con ventas por año y el tipo de gráfico como cadena
def diagrama_ventas_tipo(serie_ventas, tipo):
    """
    Genera un gráfico del tipo especificado con la evolución de ventas.
    Tipos válidos: 'líneas', 'barras', 'sectores', 'áreas'
    """
    fig, ax = plt.subplots(figsize=(9, 5))
    tipo = tipo.lower().strip()

    if tipo == "líneas" or tipo == "lineas":
        # plt.plot traza una línea conectando los valores
        ax.plot(serie_ventas.index.astype(str), serie_ventas.values,
                marker='o', color='steelblue', linewidth=2)
    elif tipo == "barras":
        # plt.bar dibuja barras verticales
        ax.bar(serie_ventas.index.astype(str), serie_ventas.values,
               color='coral', edgecolor='black', alpha=0.85)
    elif tipo == "sectores":
        # Para sectores se usa una figura separada sin ax
        plt.close(fig)
        plt.figure(figsize=(7, 7))
        plt.pie(serie_ventas.values, labels=serie_ventas.index.astype(str),
                autopct='%1.1f%%', startangle=90)
        plt.title("Evolución del Número de Ventas")
        plt.tight_layout()
        plt.savefig("ejercicio06.png", dpi=150)
        plt.show()
        return
    elif tipo == "áreas" or tipo == "areas":
        # fill_between rellena el área bajo la curva
        ax.fill_between(serie_ventas.index.astype(str), serie_ventas.values,
                        alpha=0.5, color='mediumseagreen')
        ax.plot(serie_ventas.index.astype(str), serie_ventas.values,
                color='darkgreen', linewidth=2)
    else:
        print(f"  Tipo '{tipo}' no reconocido. Opciones: líneas, barras, sectores, áreas")
        plt.close(fig)
        return

    ax.set_title("Evolución del Número de Ventas")
    ax.set_xlabel("Año")
    ax.set_ylabel("Ventas")
    ax.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig("ejercicio06.png", dpi=150)
    plt.show()

print("Ejercicio 06 - Diagrama de ventas anuales por tipo")
ventas_anuales = pd.Series(
    [12000, 15000, 13500, 17000, 19500, 22000],
    index=[2019, 2020, 2021, 2022, 2023, 2024]
)
diagrama_ventas_tipo(ventas_anuales, "barras")
print("  Gráfico guardado como ejercicio06.png\n")


# ===========================================================
# Ejercicio 07: Diagrama de líneas con ingresos y gastos por meses
# La función recibe un DataFrame con columnas 'Ingresos' y 'Gastos'
# Se dibujan dos líneas con leyenda y el eje Y arranca desde 0
def diagrama_ingresos_gastos(df):
    """
    Genera un diagrama de líneas con ingresos y gastos.
    El DataFrame debe tener columnas 'Ingresos' y 'Gastos' y el mes como índice.
    """
    plt.figure(figsize=(10, 5))
    # Línea de ingresos
    plt.plot(df.index, df['Ingresos'], marker='o', color='steelblue',
             linewidth=2, label='Ingresos')
    # Línea de gastos
    plt.plot(df.index, df['Gastos'], marker='s', color='tomato',
             linewidth=2, label='Gastos')
    plt.title("Evolución de Ingresos y Gastos")
    plt.xlabel("Mes")
    plt.ylabel("Importe (€)")
    plt.ylim(0)           # El eje Y empieza en 0
    plt.legend()          # Muestra la leyenda identificando cada línea
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig("ejercicio07.png", dpi=150)
    plt.show()

print("Ejercicio 07 - Ingresos y gastos por meses")
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
         "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
datos_empresa = pd.DataFrame({
    "Ingresos": [32000, 28000, 35000, 40000, 38000, 42000,
                 45000, 30000, 38000, 41000, 43000, 50000],
    "Gastos":   [25000, 24000, 27000, 30000, 29000, 31000,
                 33000, 28000, 30000, 32000, 34000, 38000]
}, index=meses)
diagrama_ingresos_gastos(datos_empresa)
print("  Gráfico guardado como ejercicio07.png\n")


# ===========================================================
# Ejercicio 08: Cotizaciones de bancos desde CSV - serie temporal de cierres
# Se lee el CSV con pd.read_csv(); se agrupa por empresa y fecha
# Se dibuja una línea por cada banco usando groupby
def diagrama_cotizaciones_bancos(fichero_csv):
    """Lee bancos.csv y genera un diagrama de líneas con los cierres de cada banco."""
    df = pd.read_csv(fichero_csv, parse_dates=['Fecha'])
    # Ordenar por fecha para que las líneas sean continuas
    df = df.sort_values('Fecha')

    plt.figure(figsize=(11, 6))
    # Agrupar por empresa y dibujar una línea por banco
    for empresa, grupo in df.groupby('Empresa'):
        plt.plot(grupo['Fecha'], grupo['Cierre'], marker='o',
                 markersize=4, linewidth=1.8, label=empresa)

    plt.title("Ejercicio 08 - Cotizaciones de Cierre de Bancos Españoles")
    plt.xlabel("Fecha")
    plt.ylabel("Precio de Cierre (€)")
    plt.legend(title="Banco")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig("ejercicio08.png", dpi=150)
    plt.show()

print("Ejercicio 08 - Cotizaciones bancarias desde bancos.csv")
diagrama_cotizaciones_bancos("bancos.csv")
print("  Gráfico guardado como ejercicio08.png\n")


# ===========================================================
# Ejercicio 09: Análisis del Titanic con múltiples gráficos
# Se usa pd.read_csv para cargar los datos y se generan 5 diagramas distintos
print("Ejercicio 09 - Análisis del Titanic (5 diagramas)")

df_titanic = pd.read_csv("titanic.csv")

# --- 9.1 Diagrama de Sectores: fallecidos y supervivientes ---
# value_counts() cuenta los valores únicos de la columna 'Survived'
supervivencia = df_titanic['Survived'].value_counts()
etiquetas = ['Fallecidos', 'Supervivientes']

plt.figure(figsize=(6, 6))
plt.pie(supervivencia.values, labels=etiquetas, autopct='%1.1f%%',
        colors=['#FF6B6B', '#6BCB77'], startangle=90,
        wedgeprops={'edgecolor': 'white', 'linewidth': 1.5})
plt.title("Ejercicio 09.1 - Fallecidos vs Supervivientes")
plt.tight_layout()
plt.savefig("ejercicio09_1_sectores.png", dpi=150)
plt.show()
print("  9.1 Guardado como ejercicio09_1_sectores.png")

# --- 9.2 Histograma de edades ---
# plt.hist() agrupa las edades en intervalos (bins) y muestra su frecuencia
edades = df_titanic['Age'].dropna()  # Eliminar valores nulos

plt.figure(figsize=(8, 5))
plt.hist(edades, bins=15, color='steelblue', edgecolor='white', alpha=0.85)
plt.title("Ejercicio 09.2 - Distribución de Edades")
plt.xlabel("Edad")
plt.ylabel("Número de pasajeros")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("ejercicio09_2_histograma.png", dpi=150)
plt.show()
print("  9.2 Guardado como ejercicio09_2_histograma.png")

# --- 9.3 Diagrama de barras: número de personas por clase ---
# value_counts().sort_index() ordena por clase (1, 2, 3)
personas_clase = df_titanic['Pclass'].value_counts().sort_index()

plt.figure(figsize=(7, 5))
plt.bar(['1ª Clase', '2ª Clase', '3ª Clase'], personas_clase.values,
        color=['gold', 'silver', '#cd7f32'], edgecolor='black', alpha=0.85)
plt.title("Ejercicio 09.3 - Número de personas por clase")
plt.xlabel("Clase")
plt.ylabel("Número de pasajeros")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("ejercicio09_3_barras_clase.png", dpi=150)
plt.show()
print("  9.3 Guardado como ejercicio09_3_barras_clase.png")

# --- 9.4 Diagrama de barras agrupadas: fallecidos y supervivientes por clase ---
# groupby agrupa por clase y estado de supervivencia; unstack() la pivota
supervivencia_clase = df_titanic.groupby(['Pclass', 'Survived']).size().unstack()
supervivencia_clase.columns = ['Fallecidos', 'Supervivientes']
supervivencia_clase.index = ['1ª Clase', '2ª Clase', '3ª Clase']

ax = supervivencia_clase.plot(kind='bar', figsize=(9, 5), rot=0,
                               color=['#FF6B6B', '#6BCB77'],
                               edgecolor='black', alpha=0.85)
plt.title("Ejercicio 09.4 - Fallecidos y Supervivientes por Clase")
plt.xlabel("Clase")
plt.ylabel("Número de pasajeros")
plt.legend(title="Estado")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("ejercicio09_4_barras_agrupadas.png", dpi=150)
plt.show()
print("  9.4 Guardado como ejercicio09_4_barras_agrupadas.png")

# --- 9.5 Diagrama de barras acumuladas por clase ---
# stacked=True apila las barras de fallecidos y supervivientes
ax = supervivencia_clase.plot(kind='bar', figsize=(9, 5), stacked=True, rot=0,
                               color=['#FF6B6B', '#6BCB77'],
                               edgecolor='black', alpha=0.85)
plt.title("Ejercicio 09.5 - Fallecidos y Supervivientes Acumulados por Clase")
plt.xlabel("Clase")
plt.ylabel("Número de pasajeros")
plt.legend(title="Estado")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("ejercicio09_5_barras_acumuladas.png", dpi=150)
plt.show()
print("  9.5 Guardado como ejercicio09_5_barras_acumuladas.png")

print("\nEjercicio 09 completo. Todos los gráficos guardados.")
