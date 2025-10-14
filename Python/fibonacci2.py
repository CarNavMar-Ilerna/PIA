#Codigo para hacer la serie de Fibonacci hasta el numero x.

def fibonacci(n):
    
    # Definimos las dos primeras variables de Fibonacci
    prev = 0
    next = 1

    for i in range(n):
        print(prev)  # Imprimimos el valor actual de prev
        fib = prev + next
        prev = next
        next = fib

fibonacci(5)