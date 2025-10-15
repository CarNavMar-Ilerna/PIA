#Creamos una tupla llamada puntos
puntos = (5, 10, 15, 20, 25)
print(puntos)

#Imprimimos el tercer valor de la tupla
print(puntos[2])

#Convertimos la tupla en una lista
lista_puntos = list(puntos)
print(lista_puntos)

#Agregamos un nuevo valor a la lista
lista_puntos.append(30)
print(lista_puntos)

#Convertimos la lista de nuevo en una tupla
puntos = tuple(lista_puntos)
print(puntos)