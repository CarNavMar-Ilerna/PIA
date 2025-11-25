# Sistema de Animales

class Animal:
    """Clase base para todos los animales"""
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def hacer_sonido(self):
        return "El animal hace un sonido"
    
    def mostrar_info(self):
        return f"{self.nombre} tiene {self.edad} años"


class Perro(Animal):
    """Clase derivada para perros"""
    
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza
    
    def hacer_sonido(self):
        return f"{self.nombre} dice: ¡Guau guau!"
    
    def correr(self):
        return f"{self.nombre} está corriendo muy rápido"
    
    def traer_pelota(self):
        return f"{self.nombre} trae la pelota de vuelta"


class Gato(Animal):
    """Clase derivada para gatos"""
    
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color
    
    def hacer_sonido(self):
        return f"{self.nombre} dice: ¡Miau miau!"
    
    def arañar(self):
        return f"{self.nombre} está arañando el sofá"
    
    def dormir(self):
        return f"{self.nombre} está durmiendo plácidamente"


class Pajaro(Animal):
    """Clase derivada para pájaros"""
    
    def __init__(self, nombre, edad, especie):
        super().__init__(nombre, edad)
        self.especie = especie
    
    def hacer_sonido(self):
        return f"{self.nombre} dice: ¡Pío pío!"
    
    def volar(self):
        return f"{self.nombre} está volando por el cielo"
    
    def cantar(self):
        return f"{self.nombre} canta una hermosa melodía"


# Ejemplo de uso
if __name__ == "__main__":
    print("=== SISTEMA DE ANIMALES ===\n")
    
    # Crear animales
    mi_perro = Perro("Max", 5, "Golden Retriever")
    mi_gato = Gato("Luna", 3, "Blanco")
    mi_pajaro = Pajaro("Piolín", 2, "Canario")
    
    # Probar perro
    print(mi_perro.mostrar_info())
    print(mi_perro.hacer_sonido())
    print(mi_perro.correr())
    print(mi_perro.traer_pelota())
    print()
    
    # Probar gato
    print(mi_gato.mostrar_info())
    print(mi_gato.hacer_sonido())
    print(mi_gato.arañar())
    print(mi_gato.dormir())
    print()
    
    # Probar pájaro
    print(mi_pajaro.mostrar_info())
    print(mi_pajaro.hacer_sonido())
    print(mi_pajaro.volar())
    print(mi_pajaro.cantar())
