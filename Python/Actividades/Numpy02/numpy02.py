# Carlos Navarro Martinez

# Tarea - Ejercicios NumPy

import numpy as np

# ===========================================================
# Ejercicio 1: Producto Escalar
# np.dot(a, b) calcula el producto escalar (suma de productos elemento a elemento)
# También puede escribirse como: (a * b).sum() o a @ b
a = np.array([2, 3, 4])
b = np.array([5, 6, 7])
producto_escalar = np.dot(a, b)
print("Ejercicio 1 - Producto Escalar de a=[2,3,4] y b=[5,6,7]:")
print(f"  a · b = {producto_escalar}")

# ===========================================================
# Ejercicio 2: Módulo de un Vector
# np.linalg.norm(v) calcula la norma (módulo) euclidiana de un vector
# Equivale a sqrt(v[0]^2 + v[1]^2 + ...)
v = np.array([3, 4])
modulo = np.linalg.norm(v)
print("\nEjercicio 2 - Módulo del vector v=[3,4]:")
print(f"  ||v|| = {modulo}")

# ===========================================================
# Ejercicio 3: Producto de Dos Matrices
# np.dot(A, B) o el operador @ realizan la multiplicación matricial
# (no confundir con la multiplicación elemento a elemento: A * B)
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
producto_matrices = np.dot(A, B)
print("\nEjercicio 3 - Producto de matrices A y B:")
print(f"  A =\n{A}")
print(f"  B =\n{B}")
print(f"  A · B =\n{producto_matrices}")

# ===========================================================
# Ejercicio 4: Matriz Traspuesta
# .T es el atributo que devuelve la traspuesta de una matriz
# Intercambia filas por columnas
A = np.array([[1, 2, 3], [4, 5, 6]])
traspuesta = A.T
print("\nEjercicio 4 - Traspuesta de la matriz A:")
print(f"  A =\n{A}")
print(f"  A^T =\n{traspuesta}")

# ===========================================================
# Ejercicio 5: Traza de una Matriz
# np.trace(A) devuelve la suma de los elementos de la diagonal principal
# Solo aplicable a matrices cuadradas
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
traza = np.trace(A)
print("\nEjercicio 5 - Traza de la matriz A 3x3:")
print(f"  A =\n{A}")
print(f"  Traza = {traza}  (1 + 5 + 9 = {traza})")

# ===========================================================
# Ejercicio 6: Determinante de una Matriz
# np.linalg.det(A) calcula el determinante de una matriz cuadrada
# Un determinante = 0 indica que la matriz es singular (no invertible)
A = np.array([[1, 2], [3, 4]])
determinante = np.linalg.det(A)
print("\nEjercicio 6 - Determinante de la matriz A 2x2:")
print(f"  A =\n{A}")
print(f"  det(A) = {determinante:.2f}")

# ===========================================================
# Ejercicio 7: Matriz Inversa
# np.linalg.inv(A) calcula la inversa de una matriz cuadrada
# Solo existe si el determinante es distinto de 0
# Propiedad: A · A⁻¹ = I (matriz identidad)
A = np.array([[4, 7], [2, 6]])
inversa = np.linalg.inv(A)
print("\nEjercicio 7 - Inversa de la matriz A 2x2:")
print(f"  A =\n{A}")
print(f"  A⁻¹ =\n{inversa}")
# Verificación: A · A⁻¹ debe dar la identidad
print(f"  Verificación A · A⁻¹ =\n{np.round(np.dot(A, inversa))}")

# ===========================================================
# Ejercicio 8: Autovalores y Autovectores
# np.linalg.eig(A) devuelve una tupla (autovalores, autovectores)
# Los autovectores se devuelven como columnas de la matriz resultante
# Un autovector v cumple: A·v = λ·v, donde λ es el autovalor correspondiente
A = np.array([[2, 1], [1, 3]])
autovalores, autovectores = np.linalg.eig(A)
print("\nEjercicio 8 - Autovalores y Autovectores de la matriz A 2x2:")
print(f"  A =\n{A}")
print(f"  Autovalores:   {autovalores}")
print(f"  Autovectores (columnas):\n{autovectores}")

# ===========================================================
# Ejercicio 9: Solución de un Sistema de Ecuaciones
# np.linalg.solve(A, b) resuelve el sistema A·x = b
# Equivale a calcular x = A⁻¹ · b, pero de forma más eficiente y estable
#
#   Sistema:
#     2x + y  = 8
#     x  + 3y = 18
#
#   Forma matricial: A·x = b
#     A = [[2, 1], [1, 3]]
#     b = [8, 18]
A_sistema = np.array([[2, 1], [1, 3]])
b_sistema = np.array([8, 18])
solucion = np.linalg.solve(A_sistema, b_sistema)
x, y = solucion
print("\nEjercicio 9 - Solución del sistema de ecuaciones:")
print("   2x + y  = 8")
print("    x + 3y = 18")
print(f"  Solución: x = {x:.2f}, y = {y:.2f}")
# Verificación
print(f"  Verificación: 2({x:.0f}) + {y:.0f} = {2*x + y:.0f}  |  {x:.0f} + 3({y:.0f}) = {x + 3*y:.0f}")
