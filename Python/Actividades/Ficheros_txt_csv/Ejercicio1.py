import os


def escribir_tabla(n):
    nombre_archivo = os.path.join(os.path.dirname(__file__), f'tabla-{n}.txt')
    with open(nombre_archivo, 'w') as archivo:
        for i in range(1, 11):
            archivo.write(f'{n} x {i} = {n * i}\n')


def leer_tabla(n):
    nombre_archivo = os.path.join(os.path.dirname(__file__), f'tabla-{n}.txt')
    try:
        with open(nombre_archivo, 'r') as archivo:
            print(archivo.read())
    except FileNotFoundError:
        print(f'El fichero tabla-{n}.txt no existe.')


def leer_linea_tabla(n, m):
    nombre_archivo = os.path.join(os.path.dirname(__file__), f'tabla-{n}.txt')
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            if 1 <= m <= len(lineas):
                print(lineas[m - 1].strip())
            else:
                print(f'La línea {m} no existe en el fichero.')
    except FileNotFoundError:
        print(f'El fichero tabla-{n}.txt no existe.')


if __name__ == '__main__':
    print("=== Ejercicio 1a: Escribir tabla ===")
    n = int(input("Introduce un número entre 1 y 10: "))
    escribir_tabla(n)
    print(f"Tabla del {n} guardada en tabla-{n}.txt\n")
    
    print("=== Ejercicio 1b: Leer tabla ===")
    n = int(input("Introduce un número entre 1 y 10: "))
    leer_tabla(n)
    
    print("\n=== Ejercicio 1c: Leer línea específica ===")
    n = int(input("Introduce un número entre 1 y 10: "))
    m = int(input("Introduce el número de línea a leer: "))
    leer_linea_tabla(n, m)
