#Ejercicios clases y objetos

#Clase Smartphone
class Smartphone:
    def __init__(self, marca, modelo, memoria, bateria_mah):
        self.marca = marca
        self.modelo = modelo
        self.memoria = memoria
        self.bateria_mah = bateria_mah
        self.nivel_bateria = 100

    def llamar(self, contacto):
        if self.nivel_bateria >= 10:
            self.nivel_bateria -= 10
            print(f"Llamando a {contacto}...")
        else:
            print("Batería insuficiente para realizar la llamada.")

    def cargar(self, cantidad_carga):
        self.nivel_bateria += cantidad_carga
        if self.nivel_bateria > 100:
            self.nivel_bateria = 100
        print(f"Cargando... Batería al {self.nivel_bateria}%.")

    def mostrar_nivel(self):
        print(f"Nivel de batería actual: {self.nivel_bateria}%")

mi_movil = Smartphone("Samsung", "Galaxy S23", "256GB", 4500)

mi_movil.mostrar_nivel()

mi_movil.llamar("Mamá")
mi_movil.llamar("Oficina")

mi_movil.mostrar_nivel()

mi_movil.cargar(15)