#Creamos el diccionario llamado capitales
capitales = {
    "España": "Madrid",
    "Francia": "París",
    "Italia": "Roma"
}
print(capitales)

#Agregamos una nueva clave-valor al diccionario
capitales["Alemania"] = "Berlín"
print(capitales)

#Cambiamos la capital de Francia a "Lyon"
capitales["Francia"] = "Lyon"
print(capitales)

#Eliminamos la entrada asociada a Italia
del capitales["Italia"]
print(capitales)

#Imprimimos todas las claves del diccionario
for pais in capitales.keys():
    print(pais)

#Imprimimos todos los valores del diccionario
for ciudad in capitales.values():
    print(ciudad)

#Imprimimos el diccionario completo
print(capitales)