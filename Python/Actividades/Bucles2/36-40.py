#Ejercicios del 36 al 40 Bucles2

#36.Juego del "FizzBuzz"
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#37.Generar números aleatorios hasta que sea cero
import random
numero = random.randint(1, 10)
while numero != 0:
    print(f"Número generado: {numero}")
    numero = random.randint(0, 10)
print("Se generó un cero, fin del juego.")
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#38.Determinar el segundo número más grande de una lista con bucles y condicionales
numeros = [12, 45, 23, 67, 34, 89, 90, 11]
mayor = segundo_mayor = float('-inf')
for num in numeros:
    if num > mayor:
        segundo_mayor = mayor
        mayor = num
    elif mayor > num > segundo_mayor:
        segundo_mayor = num
print(f"El segundo número más grande es: {segundo_mayor}")
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#39.Pares e impares separados
numeros = [10, 15, 22, 33, 42, 55, 60, 71]
pares = []
impares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#40.Convertir números decimalesa binarios
numero = int(input("Ingrese un número decimal: "))
binario = ""
if numero == 0:
    binario = "0"
while numero > 0:
    binario = str(numero % 2) + binario
    numero //= 2
print(f"El número en binario es: {binario}")