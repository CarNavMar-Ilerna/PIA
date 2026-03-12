import math

def cinemática_inversa(longitud_1, longitud_2, x, y):
    distancia = x**2 + y**2

    cos_angulo_2 = (distancia - longitud_1**2 - longitud_2**2) / (2 * longitud_1 * longitud_2)

    if cos_angulo_2 < -1 or cos_angulo_2 > 1:
        print("El punto no se puede alcanzar.")
        return

    angulo_2 = math.acos(cos_angulo_2)

    k1 = longitud_1 + longitud_2 * math.cos(angulo_2)
    k2 = longitud_2 * math.sin(angulo_2)

    angulo_1 = math.atan2(y, x) - math.atan2(k2, k1)

    print("Ángulo 1:", math.degrees(angulo_1))
    print("Ángulo 2:", math.degrees(angulo_2))

longitud_1 = float(input("Introduce la longitud del primer eslabón: "))
longitud_2 = float(input("Introduce la longitud del segundo eslabón: "))
x = float(input("Introduce la coordenada x del punto: "))
y = float(input("Introduce la coordenada y del punto: "))

cinemática_inversa(longitud_1, longitud_2, x, y)