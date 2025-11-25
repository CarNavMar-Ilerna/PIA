#Ejercicios clases y objetos

#Clase Pelota
class Pelota:
    def __init__(self, tipo_deporte, tamano, presion_aire):
        self.tipo_deporte = tipo_deporte
        self.tamano = tamano
        self.presion_aire = presion_aire

    def inflar(self, cantidad):
        self.presion_aire += cantidad

    def desinflar(self, cantidad):
        self.presion_aire -= cantidad
        if self.presion_aire < 0:
            self.presion_aire = 0

    def mostrar_estado_presion(self):
        if self.presion_aire < 8:
            estado = "baja"
        elif self.presion_aire > 12:
            estado = "alta"
        else:
            estado = "normal"
        
        print(f"Presión: {self.presion_aire} psi ({estado}).")

mi_pelota = Pelota("Fútbol", "Número 5", 5)

mi_pelota.mostrar_estado_presion()

mi_pelota.inflar(5)
mi_pelota.mostrar_estado_presion()

mi_pelota.inflar(5)
mi_pelota.mostrar_estado_presion()

mi_pelota.desinflar(3)
mi_pelota.mostrar_estado_presion()