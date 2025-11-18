#Ejercicios clases y objetos

#Clase Persona
class Perosna:
    def __init__(self, nombre, edad, genero, altura):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.altura = altura
        pass
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y mido {self.altura} metros."
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return "mayor de edad"
        else:
            return "menor de edad"
    def edad_en_5_anios(self):
        return self.edad + 5

persona1 = Perosna("Ana", 25, "Femenino", 1.65)
persona2 = Perosna("Luis", 16, "Masculino", 1.75)

print(persona1.saludar())
print(persona2.saludar())
print(f"{persona1.nombre} es {persona1.es_mayor_de_edad()}.")
print(f"{persona2.nombre} es {persona2.es_mayor_de_edad()}.")
print(f"En 5 años, {persona1.nombre} tendrá {persona1.edad_en_5_anios()} años.")
print(f"En 5 años, {persona2.nombre} tendrá {persona2.edad_en_5_anios()} años.")     