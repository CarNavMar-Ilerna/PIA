#Ejercicios clases y objetos

#Clase Reloj
class Reloj:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def ajustar_hora(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def avanzar_minuto(self):
        self.minuto += 1
        if self.minuto == 60:
            self.minuto = 0
            self.hora += 1
            if self.hora == 24:
                self.hora = 0

    def avanzar_segundo(self):
        self.segundo += 1
        if self.segundo == 60:
            self.segundo = 0
            self.avanzar_minuto()

    def mostrar_hora(self):
        print(f"{self.hora:02}:{self.minuto:02}:{self.segundo:02}")

mi_reloj = Reloj(23, 59, 58)

mi_reloj.mostrar_hora()

mi_reloj.avanzar_segundo()
mi_reloj.mostrar_hora()

mi_reloj.avanzar_segundo()
mi_reloj.mostrar_hora()

mi_reloj.ajustar_hora(12, 30, 0)
mi_reloj.avanzar_minuto()
mi_reloj.mostrar_hora()