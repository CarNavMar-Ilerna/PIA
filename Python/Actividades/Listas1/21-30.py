#Ejercicios del 21 al 30 Listas

#21.Crea una lista de números 
numeros1 = [2, 4, 10, 23, 41]

#Usa el sum() para obtener toda la suma de los elementos
print(sum(numeros1))
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#22.Crea una lista de booleanos
booleanos = [True, False, True, False]

#Usa all() para verificar si todos los elementos son true
print(all(booleanos))
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#23.Usa any() para verificar si almenos uno de los elementos es True
print(any(booleanos))
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#24.Convierte una lista de cadenas en una cadena unica separada por comas usando join()
cadenas = ["A", "mi", "no", "me", "apetece"]
print(",".join(cadenas))
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#25.Usa list() para convertir una cadena en una lista de caracteres
cadena = "La papaya esta muy buena"
print(list(cadena))
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#26.Crea una lista con 10 números
numeros2 = [2, 4, 10, 45, 67, 89, 12, 42, 35, 90]

#Usa slicing para obtener una sublista con los numeros de indice 2 al 6
numeros_slicing = numeros2[2:6]
print(numeros_slicing)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#27.Elimina el último elemento de una lista de ciudades usando pop() con indice negativo
ciudades = ["Sevilla", "Lisboa", "Berlín", "Milan", "Atenas"]
ciudades.pop(-1)
print(ciudades)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#28.Usa max() para encontrar el valor más grande en una lista de números
print(max(numeros2))
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#29.Usa min() para encontrar el valor más pequeño en una lista de números
print(min(numeros2))
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#30.Crea una lista de números al azar
numeros3 = [34, 1, 67, 89, 9, 34, 23]

#Usa sorted() para ordenar la lista sin modificar la original
print(sorted(numeros3))