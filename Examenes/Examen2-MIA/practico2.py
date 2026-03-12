import math

def comprobar_alcance(longitud_1, longitud_2, x, y):
    distancia = math.sqrt(x**2 + y**2)
    alcance_maximo = longitud_1 + longitud_2
    alcance_minimo = abs(longitud_1 - longitud_2)

    if alcance_minimo <= distancia <= alcance_maximo:
        print("El punto está dentro del espacio de trabajo del robot.")
    else:
        print("El punto está fuera del espacio de trabajo del robot.")

longitud_1 = float(input("Introduce la longitud del primer eslabón: "))
longitud_2 = float(input("Introduce la longitud del segundo eslabón: "))
x = float(input("Introduce la coordenada x del punto: "))
y = float(input("Introduce la coordenada y del punto: "))

comprobar_alcance(longitud_1, longitud_2, x, y)