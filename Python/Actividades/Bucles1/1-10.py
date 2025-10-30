#Ejercicios del 1 al 10 Bucles

#1.Numeros pares con for
for numero in range(1, 100):
    if numero % 2 == 0:
        print(numero)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#2.Factorial con while
num = 5
factorial = 1
while num > 0:
    factorial = factorial * num
    num = num - 1
print(factorial)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#3.Numeros primos con for
primo = False
numero = 14
for i in range(2, numero):
    if numero % i == 0:
        primo = True
        break
if primo:
    print(f"El número {numero} es primo")
else:
    print(f"El número {numero} no es primo")
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#4.Buscar en lista con else en un for
numeros = [3, 5, 7, 9, 11]
buscar = 9
for n in numeros:
    if n == buscar:
        print(f"El número {buscar} fue encontrado en la lista.")
        break
else:
    print(f"El número {buscar} no fue encontrado en la lista.")
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#5.Palíndromo con while
texto = "radar"
izquierda = 0
derecha = len(texto) - 1
es_palindromo = True
while izquierda < derecha:
    if texto[izquierda] != texto[derecha]:
        es_palindromo = False
        break
    izquierda += 1
    derecha -= 1
if es_palindromo:
    print(f'"{texto}" es un palíndromo.')
else:
    print(f'"{texto}" no es un palíndromo.')
print("...............................................................................")

#-------------------------------------------------------------------------------------------

