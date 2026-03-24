# Carlos Navarro Martinez

# Tarea - Ejercicios NumPy

import numpy as np

# ===========================================================
# Ejercicio 1: Crear un vector con valores dentro del rango 10-49
# np.arange(inicio, fin) genera valores desde inicio hasta fin-1
vector_rango = np.arange(10, 50)
print("Ejercicio 1 - Vector con valores del 10 al 49:")
print(vector_rango)

# ===========================================================
# Ejercicio 2: Invertir vector
# [::-1] invierte el array usando slicing
vector_invertido = vector_rango[::-1]
print("\nEjercicio 2 - Vector invertido:")
print(vector_invertido)

# ===========================================================
# Ejercicio 3: Crear un array de 10 ceros
# np.zeros(n) crea un array de n elementos inicializados a 0
array_ceros = np.zeros(10)
print("\nEjercicio 3 - Array de 10 ceros:")
print(array_ceros)

# ===========================================================
# Ejercicio 4: Crear un array de 10 unos
# np.ones(n) crea un array de n elementos inicializados a 1
array_unos = np.ones(10)
print("\nEjercicio 4 - Array de 10 unos:")
print(array_unos)

# ===========================================================
# Ejercicio 5: Crear matriz 3x3 con valores del 0 a 8
# np.arange genera los valores y reshape cambia la forma al tamaño indicado
matriz_3x3 = np.arange(9).reshape(3, 3)
print("\nEjercicio 5 - Matriz 3x3 con valores del 0 al 8:")
print(matriz_3x3)

# ===========================================================
# Ejercicio 6: Crear un array de 10 cincos
# np.full(n, valor) crea un array de n elementos con el valor indicado
array_cincos = np.full(10, 5)
print("\nEjercicio 6 - Array de 10 cincos:")
print(array_cincos)

# ===========================================================
# Ejercicio 7: Transformar el array anterior a dimensión [2,5] y [5,2]
# reshape(filas, columnas) cambia las dimensiones del array
array_2x5 = array_cincos.reshape(2, 5)
array_5x2 = array_cincos.reshape(5, 2)
print("\nEjercicio 7 - Array de cincos en dimensión [2,5]:")
print(array_2x5)
print("Array de cincos en dimensión [5,2]:")
print(array_5x2)

# ===========================================================
# Ejercicio 8: Encontrar los índices (no el valor) que no son cero
# np.nonzero() devuelve una tupla con los índices de los elementos no nulos
array_ej8 = np.array([1, 2, 4, 2, 4, 0, 1, 0, 0, 0, 12, 4, 5, 6, 7, 0])
indices_no_cero = np.nonzero(array_ej8)
print("\nEjercicio 8 - Índices de elementos no nulos en [1,2,4,2,4,0,1,0,0,0,12,4,5,6,7,0]:")
print(indices_no_cero[0])

# ===========================================================
# Ejercicio 9: Crear una matriz identidad 6x6
# np.eye(n) crea una matriz identidad de nxn (diagonal de 1s, resto 0s)
identidad_6x6 = np.eye(6)
print("\nEjercicio 9 - Matriz identidad 6x6:")
print(identidad_6x6)

# ===========================================================
# Ejercicio 10: Crear vector con 100 valores aleatorios de formato entero
# np.random.randint(min, max, n) genera n enteros aleatorios entre min y max
vector_aleatorio = np.random.randint(0, 100, 100)
print("\nEjercicio 10 - Vector con 100 valores aleatorios enteros:")
print(vector_aleatorio)

# ===========================================================
# Ejercicio 11: Crear un array con valores al azar de forma 3x3x3
# np.random.random(shape) genera valores aleatorios flotantes entre 0 y 1
array_3d = np.random.random((3, 3, 3))
print("\nEjercicio 11 - Array aleatorio de forma 3x3x3:")
print(array_3d)

# ===========================================================
# Ejercicio 12: Encontrar los valores mínimos y máximos del array anterior
# .min() y .max() devuelven el menor y el mayor valor del array, respectivamente
valor_min = array_3d.min()
valor_max = array_3d.max()
print("\nEjercicio 12 - Valor mínimo y máximo del array 3x3x3:")
print(f"  Mínimo: {valor_min}")
print(f"  Máximo: {valor_max}")

# ===========================================================
# Ejercicio 13: Indicar los índices (posición) de los valores mínimo y máximo
# np.unravel_index convierte el índice plano al índice multidimensional
# np.argmin() y np.argmax() devuelven el índice del mínimo/máximo en forma plana
idx_min = np.unravel_index(np.argmin(array_3d), array_3d.shape)
idx_max = np.unravel_index(np.argmax(array_3d), array_3d.shape)
print("\nEjercicio 13 - Índices del mínimo y máximo del array 3x3x3:")
print(f"  Índice del mínimo: {idx_min}")
print(f"  Índice del máximo: {idx_max}")

# ===========================================================
# Ejercicio 14: Generar una matriz 10x10 con bordes 1 e interior ceros
# np.ones crea la matriz de unos, luego se asignan ceros al interior con slicing [1:-1, 1:-1]
matriz_borde = np.ones((10, 10), dtype=int)
matriz_borde[1:-1, 1:-1] = 0
print("\nEjercicio 14 - Matriz 10x10 con bordes 1 e interior 0:")
print(matriz_borde)

# ===========================================================
# Ejercicio 15: Crear array de tamaño 5x5 con los valores [0,1,2,3,4]
# np.tile repite el array base el número de veces indicado para llenar las filas
fila_base = np.array([0, 1, 2, 3, 4])
matriz_5x5_vals = np.tile(fila_base, (5, 1))
print("\nEjercicio 15 - Array 5x5 con valores [0,1,2,3,4] en cada fila:")
print(matriz_5x5_vals)

# ===========================================================
# Ejercicio 16: Crear dos arrays aleatorios 3x3 y verificar igualdad
# np.array_equal comprueba si dos arrays son exactamente iguales (elemento a elemento)
# == genera una matriz booleana comparando elemento a elemento
array_a = np.random.randint(0, 10, (3, 3))
array_b = np.random.randint(0, 10, (3, 3))
son_iguales = np.array_equal(array_a, array_b)
matriz_booleana = (array_a == array_b)
print("\nEjercicio 16 - Comparación de dos arrays aleatorios 3x3:")
print(f"  Array A:\n{array_a}")
print(f"  Array B:\n{array_b}")
print(f"  ¿Son exactamente iguales? {son_iguales}")
print(f"  Matriz booleana (coincidencias elemento a elemento):\n{matriz_booleana}")

# ===========================================================
# Ejercicio 17: Generar array 5x5 con enteros aleatorios entre 1 y 100
# np.random.randint(1, 101) genera enteros desde 1 hasta 100 (inclusive)
matriz_5x5_rand = np.random.randint(1, 101, (5, 5))
print("\nEjercicio 17 - Matriz 5x5 con enteros aleatorios entre 1 y 100:")
print(matriz_5x5_rand)

# ===========================================================
# Ejercicio 18: Obtener la suma total de la matriz 5x5 anterior
# .sum() sin argumentos suma todos los elementos del array
suma_total = matriz_5x5_rand.sum()
print("\nEjercicio 18 - Suma total de la matriz 5x5:")
print(suma_total)

# ===========================================================
# Ejercicio 19: Obtener un array con la suma de cada columna
# .sum(axis=0) suma a lo largo del eje 0 (por columnas)
suma_columnas = matriz_5x5_rand.sum(axis=0)
print("\nEjercicio 19 - Suma de cada columna de la matriz 5x5:")
print(suma_columnas)

# ===========================================================
# Ejercicio 20: Extraer fila inicial, fila intermedia (fila 3) y última fila
# Se usa indexación directa: [0] primera fila, [2] tercera fila, [-1] última fila
fila_inicial = matriz_5x5_rand[0]
fila_intermedia = matriz_5x5_rand[2]
fila_ultima = matriz_5x5_rand[-1]
print("\nEjercicio 20 - Filas extraídas de la matriz 5x5:")
print(f"  Fila inicial (fila 1):     {fila_inicial}")
print(f"  Fila intermedia (fila 3):  {fila_intermedia}")
print(f"  Última fila (fila 5):      {fila_ultima}")
