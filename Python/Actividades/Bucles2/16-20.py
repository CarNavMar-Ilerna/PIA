#Ejercicios del 16 al 20 Bucles2

#16.Calcular la clasificación dando un puntuaje usando condicionales
puntuacion = int(input("Ingrese su puntuación (0-100): "))
if puntuacion >= 90:
    clasificacion = 'A'
elif puntuacion >= 80:
    clasificacion = 'B'
elif puntuacion >= 70:
    clasificacion = 'C'
elif puntuacion >= 60:
    clasificacion = 'D'
else:
    clasificacion = 'F'
print(f"Su clasificación es: {clasificacion}")
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#17.Verificar si un carácter es una vocal
caracter = input("Ingrese un carácter: ").lower()
if caracter in 'aeiou':
    print(f"El carácter '{caracter}' es una vocal.")
else:
    print(f"El carácter '{caracter}' no es una vocal.")
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#18.Verificar si un número esta dentro de una rango
numero = int(input("Ingrese un número: "))
rango_inicio = 10
rango_fin = 50
if rango_inicio <= numero <= rango_fin:
    print(f"El número {numero} está dentro del rango de {rango_inicio} a {rango_fin}.")
else:
    print(f"El número {numero} está fuera del rango de {rango_inicio} a {rango_fin}.")
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#19.Calculadora simple con condicionales
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (+, -, *, /): ")
if operacion == '+':
    resultado = num1 + num2
elif operacion == '-':
    resultado = num1 - num2
elif operacion == '*':
    resultado = num1 * num2
elif operacion == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error: División por cero"
else:
    resultado = "Operación no válida"
print(f"El resultado es: {resultado}")
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#20.Número primo
numero = int(input("Ingrese un número para verificar si es primo: "))
if numero > 1:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            print(f"El número {numero} no es primo.")
            break
    else:
        print(f"El número {numero} es primo.")