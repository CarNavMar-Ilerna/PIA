#Ejercicios clases y objetos

#Clase Estudiante
class Estudiante:
    def __init__(self, nombre, curso):
        self.nombre = nombre
        self.curso = curso
        self.notas = []
        self.promedio = 0.0

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def calcular_promedio(self):
        if len(self.notas) > 0:
            self.promedio = sum(self.notas) / len(self.notas)
        else:
            self.promedio = 0.0
        return self.promedio

    def verificar_aprobacion(self):
        self.calcular_promedio()
        if self.promedio >= 5:
            print(f"El estudiante {self.nombre} ha aprobado con {self.promedio:.2f}.")
        else:
            print(f"El estudiante {self.nombre} ha reprobado con {self.promedio:.2f}.")

estudiante1 = Estudiante("Juan Pérez", "Matemáticas 101")

estudiante1.agregar_nota(4.5)
estudiante1.agregar_nota(6.0)
estudiante1.agregar_nota(7.5)

print(f"Notas actuales: {estudiante1.notas}")

estudiante1.calcular_promedio()
print(f"Promedio actual: {estudiante1.promedio:.2f}")

estudiante1.verificar_aprobacion()