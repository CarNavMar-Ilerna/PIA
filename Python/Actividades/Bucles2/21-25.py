#Ejercicios del 21 al 25 Bucles2

#21.Suma de números pares en un rango
input_inicio = int(input("Ingrese el número de inicio del rango: "))
input_fin = int(input("Ingrese el número de fin del rango: "))
suma_pares = 0
for num in range(input_inicio, input_fin + 1):
    if num % 2 == 0:
        suma_pares += num
print(f"La suma de los números pares entre {input_inicio} y {input_fin} es: {suma_pares}")
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#22.Imprimir números divisibles por 3 y 5 (entre 1 y 100)
print("Números entre 1 y 100 divisibles por 3 y 5:")
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(num)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#23.Contar números positivos, negativos y ceros
numeros = int(input("¿Cuántos números desea ingresar? "))
positivos = 0
negativos = 0
ceros = 0
for _ in range(numeros):
    valor = float(input("Ingrese un número: "))
    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1
    else:
        ceros += 1
print(f"Números positivos: {positivos}, negativos: {negativos}, ceros: {ceros}")
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#24.Sumar solo los números positivos de una lista
lista_numeros = [2, 43, 23, 78, 12, -4, -23, 0, 56, -78, 34]
suma_positivos = 0
for numero in lista_numeros:
    if numero > 0:
        suma_positivos += numero
print(f"La suma de los números positivos en la lista es: {suma_positivos}")
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#25.Contar vocales y consonantes en una cadena
cadena = input("Ingrese una cadena de texto: ").lower()
vocales = 0
consonantes = 0
for char in cadena:
    if char.isalpha():
        if char in 'aeiou':
            vocales += 1
        else:
            consonantes += 1
print(f"Número de vocales: {vocales}, número de consonantes: {consonantes}")