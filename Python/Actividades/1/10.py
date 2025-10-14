#Creamos una lista llamada numeros
numeros = [12, 45, 78, 23, 56, 89, 23, 56]
print(numeros)

#Contamos cuantas veces aparece el número 23 en la lista
print(numeros.count(23))

#Buscamos el indice del primer número 56 en la lista
print(numeros.index(56))

#Eliminamos el ultimo número de la lista
numeros.pop()
print(numeros)

#Usamos el metodo extend para agregar nuevos valores al final
numeros.extend([100, 200, 300])
print(numeros)

#Hacemos una copia de la lista llamada numeros_copia
numeros_copia = numeros.copy()
print(numeros_copia)

#Vaciamos la lista original
numeros.clear()
print(numeros)