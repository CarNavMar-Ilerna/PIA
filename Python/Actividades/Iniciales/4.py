#Definimos en diccionario
diccionario = {
    "nombre": "Ana",
    "edad": 22,
    "Curso": "Matematicas"
}
print(diccionario)
#Cambiamos su edad a 23
diccionario["edad"] = 23
print(diccionario)

#Agregamos una nueva clave llamada promedio

diccionario["promedio"] = 8.5
print(diccionario)

#Imprimimos el valor asociado a la clave nombre
print(diccionario["nombre"])