#Ejercicios del 11 al 15 Bucles

#11.Contador descendente con while
numero = 10
while numero >= 0:
    print(numero)
    numero -= 1
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#12.Mínimo común múltiplo (MCM) con while
def mcm(a, b):
    mayor = max(a, b)
    while True:
        if mayor % a == 0 and mayor % b == 0:
            return mayor
        mayor += 1
print(f"El MCM de 4 y 5 es: {mcm(4, 5)}")
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#13.Palabras que empiezan con vocal con for
palabras = ["cocos", "avion", "elefante", "perro", "iguana", "gato"]
vocales = "aeiouAEIOU"
for palabra in palabras:
    if palabra[0] in vocales:
        print(palabra)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#14.Buscar máximo en una lista con for
numeros = [12, 45, 2, 67, 34, 89, 23]
maximo = numeros[0]
for numero in numeros:
    if numero > maximo:
        maximo = numero
print(f"El número máximo en la lista es: {maximo}")
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#15.Suma de números en un rango con for
inicio = 1
fin = 100
suma = 0
for numero in range(inicio, fin + 1):
    suma += numero
print(f"La suma de los números del {inicio} al {fin} es: {suma}")