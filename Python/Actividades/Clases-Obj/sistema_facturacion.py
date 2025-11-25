# Sistema de Facturación

from datetime import datetime, timedelta

class Producto:
    """Clase base para todos los productos"""
    
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def calcular_costo_total(self):
        return self.precio * self.cantidad
    
    def mostrar_info(self):
        return f"{self.nombre} - Precio: ${self.precio} - Cantidad: {self.cantidad}"


class Electrodomestico(Producto):
    """Clase derivada para electrodomésticos"""
    
    def __init__(self, nombre, precio, cantidad, consumo_energetico):
        super().__init__(nombre, precio, cantidad)
        self.consumo_energetico = consumo_energetico  # en kWh
    
    def calcular_costo_total(self):
        costo_base = super().calcular_costo_total()
        # Descuento del 5% si compra más de 3 unidades
        if self.cantidad > 3:
            descuento = costo_base * 0.05
            return round(costo_base - descuento, 2)
        return costo_base
    
    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base} - Consumo: {self.consumo_energetico} kWh"
    
    def calcular_costo_anual_energia(self, precio_kwh=0.15):
        """Calcula el costo anual aproximado de energía"""
        # Asumiendo uso diario promedio de 2 horas
        costo_anual = self.consumo_energetico * 2 * 365 * precio_kwh
        return round(costo_anual, 2)


class Ropa(Producto):
    """Clase derivada para ropa"""
    
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla
    
    def calcular_costo_total(self):
        costo_base = super().calcular_costo_total()
        # Descuento del 15% si compra más de 5 prendas
        if self.cantidad > 5:
            descuento = costo_base * 0.15
            return round(costo_base - descuento, 2)
        # Descuento del 10% si compra más de 2 prendas
        elif self.cantidad > 2:
            descuento = costo_base * 0.10
            return round(costo_base - descuento, 2)
        return costo_base
    
    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base} - Talla: {self.talla}"


class Alimento(Producto):
    """Clase derivada para alimentos"""
    
    def __init__(self, nombre, precio, cantidad, fecha_vencimiento):
        super().__init__(nombre, precio, cantidad)
        self.fecha_vencimiento = fecha_vencimiento  # formato: datetime
    
    def calcular_costo_total(self):
        costo_base = super().calcular_costo_total()
        dias_para_vencer = (self.fecha_vencimiento - datetime.now()).days
        
        # Descuento según días para vencer
        if dias_para_vencer <= 3:
            descuento = costo_base * 0.30  # 30% de descuento
        elif dias_para_vencer <= 7:
            descuento = costo_base * 0.15  # 15% de descuento
        elif dias_para_vencer <= 14:
            descuento = costo_base * 0.05  # 5% de descuento
        else:
            descuento = 0
        
        return round(costo_base - descuento, 2)
    
    def mostrar_info(self):
        info_base = super().mostrar_info()
        fecha_str = self.fecha_vencimiento.strftime("%d/%m/%Y")
        return f"{info_base} - Vence: {fecha_str}"
    
    def dias_hasta_vencimiento(self):
        dias = (self.fecha_vencimiento - datetime.now()).days
        return max(0, dias)
    
    def esta_vencido(self):
        return datetime.now() > self.fecha_vencimiento


# Ejemplo de uso
if __name__ == "__main__":
    print("=== SISTEMA DE FACTURACIÓN ===\n")
    
    # Crear productos
    nevera = Electrodomestico("Nevera Samsung", 800, 2, 150)
    lavadora = Electrodomestico("Lavadora LG", 600, 4, 200)
    
    camisa = Ropa("Camisa Polo", 25, 3, "M")
    pantalon = Ropa("Pantalón Jeans", 40, 6, "L")
    
    leche = Alimento("Leche Entera", 2.5, 10, datetime.now() + timedelta(days=5))
    pan = Alimento("Pan Integral", 1.5, 5, datetime.now() + timedelta(days=2))
    yogurt = Alimento("Yogurt Natural", 3.0, 8, datetime.now() + timedelta(days=20))
    
    # Probar electrodomésticos
    print("--- ELECTRODOMÉSTICOS ---")
    print(nevera.mostrar_info())
    print(f"Costo total: ${nevera.calcular_costo_total()}")
    print(f"Costo anual energía: ${nevera.calcular_costo_anual_energia()}")
    print()
    
    print(lavadora.mostrar_info())
    print(f"Costo total: ${lavadora.calcular_costo_total()} (con descuento por cantidad)")
    print(f"Costo anual energía: ${lavadora.calcular_costo_anual_energia()}")
    print()
    
    # Probar ropa
    print("--- ROPA ---")
    print(camisa.mostrar_info())
    print(f"Costo total: ${camisa.calcular_costo_total()} (con descuento 10%)")
    print()
    
    print(pantalon.mostrar_info())
    print(f"Costo total: ${pantalon.calcular_costo_total()} (con descuento 15%)")
    print()
    
    # Probar alimentos
    print("--- ALIMENTOS ---")
    print(leche.mostrar_info())
    print(f"Días hasta vencimiento: {leche.dias_hasta_vencimiento()}")
    print(f"Costo total: ${leche.calcular_costo_total()} (con descuento por vencimiento)")
    print()
    
    print(pan.mostrar_info())
    print(f"Días hasta vencimiento: {pan.dias_hasta_vencimiento()}")
    print(f"Costo total: ${pan.calcular_costo_total()} (con descuento por vencimiento)")
    print()
    
    print(yogurt.mostrar_info())
    print(f"Días hasta vencimiento: {yogurt.dias_hasta_vencimiento()}")
    print(f"Costo total: ${yogurt.calcular_costo_total()}")
    print()
    
    # Resumen de factura
    print("=== RESUMEN DE FACTURA ===")
    productos = [nevera, lavadora, camisa, pantalon, leche, pan, yogurt]
    total_general = sum(p.calcular_costo_total() for p in productos)
    print(f"Total a pagar: ${round(total_general, 2)}")
