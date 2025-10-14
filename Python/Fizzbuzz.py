#Definimos las funciones que usaremos, en este caso con un bucle dentro de la función.

def fizzbuzz():
    for i in range(1, 101):  # Iteramos del 1 al 100
        if i % 3 == 0 and i % 5 == 0:  # Si es divisible por 3 y por 5
            print("FIZZBUZZ")
        elif i % 3 == 0:  # Si es divisible solo por 3
            print("FIZZ")
        elif i % 5 == 0:  # Si es divisible solo por 5
            print("BUZZ")
        else:  # Si no es divisible ni por 3 ni por 5
            print(i)


fizzbuzz()  # Llamamos a la función para ejecutar el código