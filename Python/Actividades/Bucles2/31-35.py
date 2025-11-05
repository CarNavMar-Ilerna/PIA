#Ejercicios del 31 al 35 Bucles2

#31.Palíndromo
def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]
palabra = input("Ingresa una palabra o frase: ")
if es_palindromo(palabra):
    print(f'"{palabra}" es un palíndromo.')
else:
    print(f'"{palabra}" no es un palíndromo.')
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#32.Encontrar el números mayor en una lista
numeros = [3, 5, 2, 8, 1, 4]
mayor = numeros[0]
for numero in numeros:
    if numero > mayor:
        mayor = numero
print(f"El número mayor en la lista es: {mayor}")
print("...............................................................................")

#33.Contar números primos en un rango
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
rango_inferior = 10
rango_superior = 50
contador_primos = 0
for numero in range(rango_inferior, rango_superior + 1):
    if es_primo(numero):
        contador_primos += 1
print(f"Números primos entre {rango_inferior} y {rango_superior}: {contador_primos}")
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#34.Verificar si una lista está ordenada
def esta_ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True
lista_numeros = [1, 2, 3, 4, 5]
if esta_ordenada(lista_numeros):
    print("La lista está ordenada.")
else:
    print("La lista no está ordenada.")
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#35.Números perfectos entre 1 y 1000
def es_numero_perfecto(num):
    suma_divisores = 0
    for i in range(1, num):
        if num % i == 0:
            suma_divisores += i
    return suma_divisores == num
numeros_perfectos = []
for numero in range(1, 1001):
    if es_numero_perfecto(numero):
        numeros_perfectos.append(numero)
print(f"Números perfectos entre 1 y 1000: {numeros_perfectos}")