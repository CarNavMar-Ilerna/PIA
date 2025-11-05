#Ejercicios del 11 al 15 Bucles 2

#11.Par o impar
numero = int(input("Ingrese un número entero: "))
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#12.Positivo, negativo o cero
numero = float(input("Ingrese un número: "))
if numero > 0:
    print(f"El número {numero} es positivo.")
elif numero < 0:
    print(f"El número {numero} es negativo.")
else:
    print("El número es cero.")
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#13.Comparación de dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
if num1 > num2:
    print(f"El número {num1} es mayor que {num2}.")
elif num2 > num1:
    print(f"El número {num2} es mayor que {num1}.")
else:
    print("Ambos números son iguales.")
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#14.Determinar el mayor de tres números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3
print(f"El mayor de los tres números es: {mayor}")
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#15.Año bisiesto
año = int(input("Ingrese un año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")