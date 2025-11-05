#Ejercicios del 6 al 10 Bucles2

#6.Factorial de un número
n = int(input("Ingrese un número entero positivo para calcular su factorial: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"El factorial de {n} es: {factorial}")
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#7.Imprimir tabla de multiplicar
num = int(input("Ingrese un número para ver su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#8.Imprimir los primeros n números pares
n = int(input("Ingrese un número entero positivo para ver los primeros n números pares: "))
print(f"Los primeros {n} números pares son:")
for i in range(1, n + 1):
    print(i * 2)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#9.Serie de Fibonnacci
n = int(input("Ingrese un número entero positivo para ver la serie de Fibonacci hasta ese número: "))
a, b = 0, 1
print("Serie de Fibonacci:")
while a <= n:
    print(a)
    a, b = b, a + b
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#10.Contar dígitos de un número
num = int(input("Ingrese un número entero positivo para contar sus dígitos: "))
contador = 0
while num > 0:
    num //= 10
    contador += 1
print(f"El número tiene {contador} dígitos.")