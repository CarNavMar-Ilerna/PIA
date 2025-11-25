# Sistema de Transporte

class Vehiculo:
    """Clase base para todos los vehículos"""
    
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def mostrar_info(self):
        return f"{self.marca} {self.modelo} ({self.año})"


class Coche(Vehiculo):
    """Clase derivada para coches"""
    
    def __init__(self, marca, modelo, año, num_puertas=4):
        super().__init__(marca, modelo, año)
        self.num_puertas = num_puertas
        self.velocidad = 0
    
    def acelerar(self, incremento=10):
        self.velocidad += incremento
        return f"El coche acelera. Velocidad actual: {self.velocidad} km/h"
    
    def frenar(self, decremento=10):
        self.velocidad = max(0, self.velocidad - decremento)
        return f"El coche frena. Velocidad actual: {self.velocidad} km/h"
    
    def tocar_claxon(self):
        return "¡BEEP BEEP!"


class Motocicleta(Vehiculo):
    """Clase derivada para motocicletas"""
    
    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self.cilindrada = cilindrada
        self.velocidad = 0
    
    def acelerar(self, incremento=15):
        self.velocidad += incremento
        return f"La motocicleta acelera. Velocidad actual: {self.velocidad} km/h"
    
    def frenar(self, decremento=15):
        self.velocidad = max(0, self.velocidad - decremento)
        return f"La motocicleta frena. Velocidad actual: {self.velocidad} km/h"
    
    def tocar_claxon(self):
        return "¡BEEP!"
    
    def hacer_caballito(self):
        return "¡La motocicleta hace un caballito!"


class Bicicleta(Vehiculo):
    """Clase derivada para bicicletas"""
    
    def __init__(self, marca, modelo, año, tipo="montaña"):
        super().__init__(marca, modelo, año)
        self.tipo = tipo
        self.velocidad = 0
    
    def pedalear(self, intensidad="normal"):
        if intensidad == "suave":
            incremento = 5
        elif intensidad == "normal":
            incremento = 10
        else:  # intenso
            incremento = 15
        
        self.velocidad += incremento
        return f"Pedaleando {intensidad}. Velocidad actual: {self.velocidad} km/h"
    
    def frenar(self, decremento=8):
        self.velocidad = max(0, self.velocidad - decremento)
        return f"La bicicleta frena. Velocidad actual: {self.velocidad} km/h"
    
    def tocar_timbre(self):
        return "¡RING RING!"


# Ejemplo de uso
if __name__ == "__main__":
    print("=== SISTEMA DE TRANSPORTE ===\n")
    
    # Crear vehículos
    mi_coche = Coche("Toyota", "Corolla", 2023)
    mi_moto = Motocicleta("Honda", "CBR", 2022, 600)
    mi_bici = Bicicleta("Trek", "Mountain X", 2024, "montaña")
    
    # Probar coche
    print(f"Coche: {mi_coche.mostrar_info()}")
    print(mi_coche.acelerar(30))
    print(mi_coche.acelerar(20))
    print(mi_coche.tocar_claxon())
    print(mi_coche.frenar(25))
    print()
    
    # Probar motocicleta
    print(f"Motocicleta: {mi_moto.mostrar_info()}")
    print(mi_moto.acelerar(40))
    print(mi_moto.hacer_caballito())
    print(mi_moto.tocar_claxon())
    print(mi_moto.frenar(20))
    print()
    
    # Probar bicicleta
    print(f"Bicicleta: {mi_bici.mostrar_info()}")
    print(mi_bici.pedalear("suave"))
    print(mi_bici.pedalear("intenso"))
    print(mi_bici.tocar_timbre())
    print(mi_bici.frenar(10))
