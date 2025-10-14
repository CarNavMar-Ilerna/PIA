#Codigo para sumar los primeros 50 numeros de Fibonacci.

def fibonacci():

    # Definimos las dos primeras variables de Fibonacci
    prev = 0
    next = 1

    for i in range(0, 50):
        print(prev) # Imprimimos el valor actual de prev
        fib = prev + next
        prev = next
        next = fib

fibonacci()