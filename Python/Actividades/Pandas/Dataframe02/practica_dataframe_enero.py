import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 300)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 120)

np.random.seed(42)

nombres_alumnos = [
    "Juan Pérez", "María López", "Carlos García", "Ana Fernández",
    "Luis Martínez", "Sofía Gómez", "Miguel Rodríguez", "Laura Sánchez",
    "José Torres", "Lucía Morales", "Andrés Herrera", "Carmen Ruiz",
    "Raúl Castro", "Elena Jiménez", "Javier Gil", "Isabel Romero",
    "Hugo Ortiz", "Sara Delgado", "Pablo Ramírez", "Marta Vargas"
]

notas = {
    "Alumno": nombres_alumnos,
    "Base de Datos": np.random.uniform(1, 10, 20).round(1),
    "Programación": np.random.uniform(1, 10, 20).round(1),
    "Sistemas Informáticos": np.random.uniform(1, 10, 20).round(1),
    "Lenguajes de Marcas": np.random.uniform(1, 10, 20).round(1),
    "Entornos de Desarrollo": np.random.uniform(1, 10, 20).round(1),
}

df_alumnos = pd.DataFrame(notas)

print("DataFrame original:")
print(df_alumnos.to_string(index=False))


# ─────────────────────────────────────────────────────────────────────────────
# APARTADO 01 – RENOMBRAR
# Renombrar las columnas de los módulos con sus abreviaturas oficiales.
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("APARTADO 01 – RENOMBRAR COLUMNAS")
print("=" * 70)

df_renombrado = df_alumnos.rename(columns={
    "Base de Datos": "BD",
    "Programación": "PR",
    "Sistemas Informáticos": "SI",
    "Lenguajes de Marcas": "LM",
    "Entornos de Desarrollo": "ED"
})

print(df_renombrado.to_string(index=False))


# ─────────────────────────────────────────────────────────────────────────────
# APARTADO 02 – FILTRADO
# Varias condiciones de filtrado sobre el DataFrame renombrado.
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("APARTADO 02 – FILTRADO")
print("=" * 70)

modulos = ["BD", "PR", "SI", "LM", "ED"]

print("\n--- Alumnos con algún suspenso (nota < 5) ---")
suspensos_alguna = df_renombrado[df_renombrado[modulos].lt(5).any(axis=1)]
print(suspensos_alguna.to_string(index=False))

print("\n--- Alumnos suspensos en Programación (PR < 5) ---")
suspensos_pr = df_renombrado[df_renombrado["PR"] < 5]
print(suspensos_pr[["Alumno", "PR"]].to_string(index=False))

print("\n--- Notas sobresalientes por materia (nota > 9) ---")
for mod in modulos:
    sobresalientes = df_renombrado[df_renombrado[mod] > 9][["Alumno", mod]]
    if not sobresalientes.empty:
        print(f"  {mod}: {sobresalientes['Alumno'].tolist()} -> {sobresalientes[mod].tolist()}")
    else:
        print(f"  {mod}: ningún sobresaliente")

print("\n--- Resultados de 'Marta Vargas' y 'Carmen Ruiz' ---")
alumnos_filtro = df_renombrado[df_renombrado["Alumno"].isin(["Marta Vargas", "Carmen Ruiz"])]
print(alumnos_filtro.to_string(index=False))


# ─────────────────────────────────────────────────────────────────────────────
# APARTADO 03 – PIVOTAR
# Transponer el DataFrame para obtener una columna "Asignatura".
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("APARTADO 03 – PIVOTAR (columna 'Asignatura')")
print("=" * 70)

df_pivot = df_renombrado.melt(
    id_vars="Alumno",
    value_vars=modulos,
    var_name="Asignatura",
    value_name="Nota"
)

df_pivot = df_pivot.sort_values(["Alumno", "Asignatura"]).reset_index(drop=True)
print(df_pivot.to_string(index=False))


# ─────────────────────────────────────────────────────────────────────────────
# APARTADO 04 – ORDENAR
# Ordenar el DataFrame por distintos criterios.
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("APARTADO 04 – ORDENAR")
print("=" * 70)

print("\n--- Ordenado por nombre de alumno (A-Z) ---")
orden_nombre = df_renombrado.sort_values("Alumno").reset_index(drop=True)
print(orden_nombre[["Alumno"] + modulos].to_string(index=False))

print("\n--- Ordenado por nota de Programación (PR) ascendente ---")
orden_pr_asc = df_renombrado.sort_values("PR", ascending=True).reset_index(drop=True)
print(orden_pr_asc[["Alumno", "PR"]].to_string(index=False))

print("\n--- Ordenado por nota de Base de Datos (BD) descendente ---")
orden_bd_desc = df_renombrado.sort_values("BD", ascending=False).reset_index(drop=True)
print(orden_bd_desc[["Alumno", "BD"]].to_string(index=False))


# ─────────────────────────────────────────────────────────────────────────────
# APARTADO 05 – AGRUPAR
# Agrupación para calcular promedios por alumno y por materia.
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("APARTADO 05 – AGRUPAR")
print("=" * 70)

print("\n--- Promedio de notas de cada alumno ---")
df_renombrado["Promedio"] = df_renombrado[modulos].mean(axis=1).round(2)
promedio_alumnos = df_renombrado[["Alumno", "Promedio"]].sort_values("Promedio", ascending=False).reset_index(drop=True)
print(promedio_alumnos.to_string(index=False))

print("\n--- Promedio de notas de cada materia ---")
promedio_materias = df_renombrado[modulos].mean().round(2).reset_index()
promedio_materias.columns = ["Materia", "Promedio"]
print(promedio_materias.to_string(index=False))

mejor = df_renombrado.loc[df_renombrado["Promedio"].idxmax()]
print(f"\n--- Alumno con mejor promedio global ---")
print(f"  {mejor['Alumno']} → Promedio: {mejor['Promedio']}")


# ─────────────────────────────────────────────────────────────────────────────
# APARTADO 06 – CONCATENAR
# Generar un segundo DataFrame con notas faltantes y concatenar de dos formas.
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("APARTADO 06 – CONCATENAR")
print("=" * 70)

df_incompleto = df_renombrado[["Alumno"] + modulos].copy()

np.random.seed(7)
for _ in range(15):
    fila = np.random.randint(0, len(df_incompleto))
    col = np.random.choice(modulos)
    df_incompleto.at[fila, col] = np.nan

print("\n--- DataFrame con notas faltantes (NaN) ---")
print(df_incompleto.to_string(index=False))

df_base = df_renombrado[["Alumno"] + modulos].copy()

print("\n--- Concatenación manteniendo NaN ---")
df_concat_nan = pd.concat([df_base, df_incompleto], ignore_index=True)
print(df_concat_nan.to_string(index=False))

print("\n--- Concatenación eliminando filas con NaN ---")
df_concat_limpio = df_concat_nan.dropna().reset_index(drop=True)
print(df_concat_limpio.to_string(index=False))
print(f"\nRegistros totales con NaN : {len(df_concat_nan)}")
print(f"Registros sin NaN         : {len(df_concat_limpio)}")
