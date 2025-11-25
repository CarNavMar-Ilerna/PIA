#Ejercicios clases y objetos

#Clase Restaurante
class Restaurante:
    def __init__(self, nombre, tipo_cocina):
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.menu = []

    def agregar_plato(self, plato):
        self.menu.append(plato)

    def mostrar_menu(self):
        print(f"--- Menú de {self.nombre} ---")
        for plato in self.menu:
            print(f"- {plato}")

    def tomar_pedido(self, plato):
        if plato in self.menu:
            print(f"Pedido confirmado: {plato}")
        else:
            print(f"El plato '{plato}' no está disponible.")

restaurante = Restaurante("La Trattoria", "Italiana")

restaurante.agregar_plato("Pizza Margarita")
restaurante.agregar_plato("Lasaña")
restaurante.agregar_plato("Risotto de Setas")

restaurante.mostrar_menu()

restaurante.tomar_pedido("Lasaña")
restaurante.tomar_pedido("Ensalada César")