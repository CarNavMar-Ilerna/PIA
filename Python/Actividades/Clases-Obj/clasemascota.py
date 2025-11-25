#Ejercicios clases y objetos

#Clase Mascota
class Mascota:
    def __init__(self, nombre, tipo_animal, edad):
        self.nombre = nombre
        self.tipo_animal = tipo_animal
        self.edad = edad
        self.energia = 50

    def alimentar(self, cantidad):
        self.energia += cantidad
        if self.energia > 100:
            self.energia = 100

    def jugar(self, cantidad):
        self.energia -= cantidad
        if self.energia < 0:
            self.energia = 0

    def mostrar_energia(self):
        if self.energia <= 20:
            estado = "cansada"
        elif self.energia >= 80:
            estado = "llena de energía"
        else:
            estado = "normal"
        
        print(f"Estado de {self.nombre}: {self.energia}% de energía ({estado}).")

mi_mascota = Mascota("Firulais", "Perro", 3)

mi_mascota.mostrar_energia()

mi_mascota.jugar(40)
mi_mascota.mostrar_energia()

mi_mascota.alimentar(80)
mi_mascota.mostrar_energia()