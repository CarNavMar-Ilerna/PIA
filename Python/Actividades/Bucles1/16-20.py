#Ejercicios del 16 al 20 Bucles

#16.Tablas de multiplicar con for
for i in range(1, 11):
    print(f"Tabla de multiplicar del {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#17.Potencia de un número con for
base = 2
exponente = 8
resultado = 1
for _ in range(exponente):
    resultado *= base
print(f"{base} elevado a la {exponente} es: {resultado}")
print("...............................................................................")

#-------------------------------------------------------------------------------------------

