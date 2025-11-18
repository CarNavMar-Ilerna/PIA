#Ejercicios clases y objetos

#Clase Cafetera
class Cafetera:
    def __init__(self, marca, capacidad_max, nivel_actual):
        self.marca = marca
        self.capacidad_max = capacidad_max
        self.nivel_actual = nivel_actual
        pass
    def servir_cafe(self, cantidad):
        if cantidad > self.nivel_actual:
            servido = self.nivel_actual
            self.nivel_actual = 0
            return f"Se sirvieron {servido} ml de café. La cafetera está vacía."
        else:
            self.nivel_actual -= cantidad
            return f"Se sirvieron {cantidad} ml de café. Nivel actual: {self.nivel_actual} ml."
    def llenar_cafetera(self):
        self.nivel_actual = self.capacidad_max
        return f"La cafetera ha sido llenada. Nivel actual: {self.nivel_actual} ml."
    def llena_o_vacia(self):
        if self.nivel_actual == self.capacidad_max:
            return "La cafetera está llena."
        elif self.nivel_actual == 0:
            return "La cafetera está vacía."
        else:
            return f"La cafetera tiene {self.nivel_actual} ml de café."
        
cafetera1 = Cafetera("Nespresso", 1000, 500)
print(cafetera1.llena_o_vacia())
print(cafetera1.servir_cafe(600))
print(cafetera1.servir_cafe(300))
print(cafetera1.llenar_cafetera())
print(cafetera1.llena_o_vacia())
print(cafetera1.servir_cafe(200))
print(cafetera1.llena_o_vacia())
print(cafetera1.servir_cafe(800))
print(cafetera1.llena_o_vacia())
print(cafetera1.llenar_cafetera())
print(cafetera1.llena_o_vacia())