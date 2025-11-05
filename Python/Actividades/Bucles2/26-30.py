#Ejercicios del 26 al 30 Bucles2

#26.Imprimir los primeros N números primos
rango = int(input("Ingrese el rango hasta donde desea imprimir números primos: "))
print(f"Números primos hasta {rango}:")
for num in range(2, rango + 1):
    es_primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(num)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#27.Juego de adivinanza
import random
numero_secreto = random.randint(1, 100)
intentos = 0
while True:
    intento = int(input("Adivina el número entre 1 y 100: "))
    intentos += 1
    if intento < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    elif intento > numero_secreto:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
        break
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#28.Calculadora de promedio
numeros_promedio = int(input("¿Cuántos números deseas promediar? "))
suma = 0
for _ in range(numeros_promedio):
    numero = float(input("Ingresa un número: "))
    suma += numero
promedio = suma / numeros_promedio
print(f"El promedio es: {promedio}")
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#29.Invertir una cadena con for
cadena = input("Ingresa una cadena para invertir: ")
cadena_invertida = ""
for caracter in cadena:
    cadena_invertida = caracter + cadena_invertida
print(f"Cadena invertida: {cadena_invertida}")
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#30.Suma de dígitos con while
numero = int(input("Ingresa un número para sumar sus dígitos: "))
suma_digitos = 0
while numero > 0:
    digito = numero % 10
    suma_digitos += digito
    numero //= 10
print(f"La suma de los dígitos es: {suma_digitos}")