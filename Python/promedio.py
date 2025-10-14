#Codigo para calcular el promedio de una lista de numeros.

def promedio(*nums):
    #Definimos las variables
    suma = 0
    k = 0
    #Recorremos la lista de numeros
    for n in nums:
        suma += n
        k += 1
    #Calculamos el promedio
    return suma / k

print(promedio(10,500,20,13,54))