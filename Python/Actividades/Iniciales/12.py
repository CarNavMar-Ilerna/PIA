#Creamos un set llamado animales
animales = {"gato", "perro", "loro", "pez"}
print(animales)

#Creamos un segundo set llamado animales_domesticos
animales_domesticos = {"gato", "perro", "conejo"}
print(animales_domesticos)

#Buscamos la intersección entre ambos sets
print(animales.intersection(animales_domesticos))

#Buscamos las diferencias entre ambos sets
print(animales.difference(animales_domesticos))
print(animales_domesticos.difference(animales))

#Unimos ambos sets
print(animales.union(animales_domesticos))