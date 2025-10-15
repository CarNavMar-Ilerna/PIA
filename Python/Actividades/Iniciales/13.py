#Creamos un diccionario llamado clase
clase = {
    "estudiante1": {
        "nombre": "Carlos",
        "edad": 19,
        "materias": ["Matemáticas", "Física"]
    },
    "estudiante2": {
        "nombre": "Marta",
        "edad": 20,
        "materias": ["Biología", "Química"]
    }
}
print(clase)

#Agregamos un nuevo estudiante al diccionario
clase["estudiante3"] = {
    "nombre": "Pedro",
    "edad": 21,
    "materias": ["Historia", "Geografía"]
}
print(clase)

#Imprimimos el nombre y edad de todos los estudiantes
for estudiante, info in clase.items():
    print(f"Nombre: {info['nombre']}, Edad: {info['edad']}")

#Cambiamos la edad de Marta a 21
clase["estudiante2"]["edad"] = 21
print(clase)

#Eliminamos las materias de Carlos
clase["estudiante1"].pop("materias")
print(clase)