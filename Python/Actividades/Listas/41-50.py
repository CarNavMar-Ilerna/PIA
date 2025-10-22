#Ejercicios del 41 al 50

#41.Crea una lista con los precios de los productos
precios = [23.4, 12, 31, 47.5, 1.33]
suma = 0
k = 0
for n in precios:
    suma += n
    k += 1
promedio = suma / k
print(promedio)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#42.Crea una lista de temperaturas y convierte todas las temperaturas de Celsius a Farenheit
temp_cel = [22, 12, 20, 36, 2]
temp_far = []
cambio = 0
for n in temp_cel:
    cambio = (n * 1.8) + 32
    temp_far.append(cambio)
    cambio = 0
print(temp_far)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#43.Encuentra los numeros pares en una lista de 10 números enteros
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda n:n%2==0,numeros)))
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#44.Crea una lista de palabras yusa map() para convertirlas a mayúsculas
palabras = ["chorizo", "porra", "morcilla", "vacio"]
mayusculas = list(map(str.upper, palabras))
print(mayusculas)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#45.Simula una cola utilizando listas, añadiendo elementos con append() y removiéndolos con pop(0)
cola = []
cola.append("primero")
cola.append("segundo")
cola.pop(0)
cola.append("tercero")
cola.append("cuarto")
print(cola)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#46.Crea una lista de nombres y usa filter() para obtener solo los nombre que comienzan con una vocal
nombres = ["Pedro", "Adrian", "Olivia", "Mateo", "Ignacio"]
print(list(filter(lambda nombre: nombre[0] in "aeiouAEIOU", nombres)))
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#47.Encuentra los duplicados en una lista de números y elimina las repeticiones
numeros2 = [2, 34, 7, 2, 7, 89, 7, 34, 12]
numeros2_unic = list(set(numeros2))
print(numeros2_unic)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#48.Crea una lista de nombre y ordénalos por la longitud de cada nombre
print(sorted(nombres, key=len))
print("...............................................................................")

#-------------------------------------------------------------------------------------------

