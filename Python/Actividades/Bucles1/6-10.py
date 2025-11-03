#Ejercicios del 6 al 10 Bucles

#6.Sumar dígitos de un número con while
numero = 145278
suma = 0
while numero > 0:
    digito = numero % 10
    suma += digito
    numero //= 10
print(f"La suma de los dígitos es: {suma}")
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#7.Adivinar el número con while
import random
numero_secreto = random.randint(1, 100)
adivinado = False
while not adivinado:
    intento = int(input("Adivina el número entre 1 y 100: "))
    if intento == numero_secreto:
        adivinado = True
        print("¡Felicidades! Has adivinado el número.")
    elif intento < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    else:
        print("Demasiado alto. Intenta de nuevo.")
print("...............................................................................")
#-------------------------------------------------------------------------------------------

#8.Conversión de temperatura con for
for celsius in range(0, 101, 10):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#9.Serie de Fibonacci con for
n = 10
a, b = 0, 1
print("Serie de Fibonacci:")
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#10.Conteo de vocales con for
texto = "Me gustan las papas bravas"
vocales = "aeiouAEIOU"
contador = 0
for char in texto:
    if char in vocales:
        contador += 1
print(f"Número de vocales en el texto: {contador}")