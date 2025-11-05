#Ejercicios del 1 al 5 Bucles2

#1.Imprimir numeros del 1 al 10 con for
for i in range(1, 11):
    print(i)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#2.Números pares del 1 al 100 con for
for i in range(2, 101, 2):
    print(i)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#3.Imprimir un patrón de estrellas
filas = 5
for i in range(1, filas + 1):
    print('*' * i)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#4.Imprimir un patrón invettido de estrellas
filas = 5
for i in range(filas, 0, -1):
    print('*' * i)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#5.suma de los primeros n números (n es ingresado por el usuario)
n = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(1, n + 1):
    suma += i 
print(f"La suma de los primeros {n} números es: {suma}")