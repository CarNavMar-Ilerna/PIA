# Jerarquía de Figuras Geométricas

import math

class Figura:
    """Clase base para todas las figuras geométricas"""
    
    def __init__(self, color, tipo):
        self.color = color
        self.tipo = tipo
    
    def mostrar_info(self):
        return f"Figura: {self.tipo}, Color: {self.color}"
    
    def calcular_area(self):
        return 0
    
    def calcular_perimetro(self):
        return 0


class Circulo(Figura):
    """Clase derivada para círculos"""
    
    def __init__(self, color, radio):
        super().__init__(color, "Círculo")
        self.radio = radio
    
    def calcular_area(self):
        area = math.pi * (self.radio ** 2)
        return round(area, 2)
    
    def calcular_perimetro(self):
        perimetro = 2 * math.pi * self.radio
        return round(perimetro, 2)
    
    def mostrar_detalles(self):
        return f"{self.mostrar_info()}, Radio: {self.radio}"


class Cuadrado(Figura):
    """Clase derivada para cuadrados"""
    
    def __init__(self, color, lado):
        super().__init__(color, "Cuadrado")
        self.lado = lado
    
    def calcular_area(self):
        return self.lado ** 2
    
    def calcular_perimetro(self):
        return 4 * self.lado
    
    def mostrar_detalles(self):
        return f"{self.mostrar_info()}, Lado: {self.lado}"


class Triangulo(Figura):
    """Clase derivada para triángulos"""
    
    def __init__(self, color, base, altura, lado1=None, lado2=None, lado3=None):
        super().__init__(color, "Triángulo")
        self.base = base
        self.altura = altura
        # Si no se proporcionan los lados, asumimos triángulo equilátero
        self.lado1 = lado1 if lado1 else base
        self.lado2 = lado2 if lado2 else base
        self.lado3 = lado3 if lado3 else base
    
    def calcular_area(self):
        area = (self.base * self.altura) / 2
        return round(area, 2)
    
    def calcular_perimetro(self):
        perimetro = self.lado1 + self.lado2 + self.lado3
        return round(perimetro, 2)
    
    def mostrar_detalles(self):
        return f"{self.mostrar_info()}, Base: {self.base}, Altura: {self.altura}"


# Ejemplo de uso
if __name__ == "__main__":
    print("=== JERARQUÍA DE FIGURAS GEOMÉTRICAS ===\n")
    
    # Crear figuras
    circulo = Circulo("Rojo", 5)
    cuadrado = Cuadrado("Azul", 4)
    triangulo = Triangulo("Verde", 6, 4, 5, 5, 6)
    
    # Probar círculo
    print(circulo.mostrar_detalles())
    print(f"Área: {circulo.calcular_area()} unidades²")
    print(f"Perímetro: {circulo.calcular_perimetro()} unidades")
    print()
    
    # Probar cuadrado
    print(cuadrado.mostrar_detalles())
    print(f"Área: {cuadrado.calcular_area()} unidades²")
    print(f"Perímetro: {cuadrado.calcular_perimetro()} unidades")
    print()
    
    # Probar triángulo
    print(triangulo.mostrar_detalles())
    print(f"Área: {triangulo.calcular_area()} unidades²")
    print(f"Perímetro: {triangulo.calcular_perimetro()} unidades")
    print()
    
    # Demostrar polimorfismo
    print("=== POLIMORFISMO ===")
    figuras = [circulo, cuadrado, triangulo]
    
    for figura in figuras:
        print(f"{figura.tipo}: Área = {figura.calcular_area()}, Perímetro = {figura.calcular_perimetro()}")
