import json
import os

ARCHIVO_JSON = "catalogo_libros.json"

def cargar_libros():
    if os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    else:
        return {"libros": []}

def guardar_libros(datos):
    with open(ARCHIVO_JSON, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)

def inicializar_libros():
    libros_iniciales = {
        "libros": [
            {"titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez", "genero": "Ficción", "año": 1967},
            {"titulo": "El Quijote", "autor": "Miguel de Cervantes", "genero": "Clásico", "año": 1605},
            {"titulo": "La Sombra del Viento", "autor": "Carlos Ruiz Zafón", "genero": "Misterio", "año": 2001},
            {"titulo": "Rayuela", "autor": "Julio Cortázar", "genero": "Ficción", "año": 1963},
            {"titulo": "1984", "autor": "George Orwell", "genero": "Distopía", "año": 1949},
            {"titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "genero": "Infantil", "año": 1943},
            {"titulo": "Crónica de una Muerte Anunciada", "autor": "Gabriel García Márquez", "genero": "Ficción", "año": 1981},
            {"titulo": "La Casa de los Espíritus", "autor": "Isabel Allende", "genero": "Ficción", "año": 1982},
            {"titulo": "El Amor en los Tiempos del Cólera", "autor": "Gabriel García Márquez", "genero": "Romance", "año": 1985},
            {"titulo": "Ficciones", "autor": "Jorge Luis Borges", "genero": "Ficción", "año": 1944}
        ]
    }
    guardar_libros(libros_iniciales)
    print("✓ Catálogo inicializado con 10 libros")

def filtrar_por_genero(genero):
    datos = cargar_libros()
    libros_genero = [l for l in datos["libros"] if l["genero"].lower() == genero.lower()]
    
    if libros_genero:
        print(f"\n--- Libros de género '{genero}' ---")
        for libro in libros_genero:
            print(f"• '{libro['titulo']}' por {libro['autor']} ({libro['año']})")
    else:
        print(f"No hay libros del género '{genero}'")
    
    return libros_genero

def filtrar_por_autor(autor):
    datos = cargar_libros()
    libros_autor = [l for l in datos["libros"] if autor.lower() in l["autor"].lower()]
    
    if libros_autor:
        print(f"\n--- Libros de '{autor}' ---")
        for libro in libros_autor:
            print(f"• '{libro['titulo']}' ({libro['año']}) - Género: {libro['genero']}")
    else:
        print(f"No hay libros del autor '{autor}'")
    
    return libros_autor

def listar_libros_recientes(año_desde=2000):
    datos = cargar_libros()
    recientes = [l for l in datos["libros"] if l["año"] >= año_desde]
    
    if recientes:
        print(f"\n--- Libros desde {año_desde} ---")
        for libro in sorted(recientes, key=lambda x: x["año"], reverse=True):
            print(f"• {libro['año']}: '{libro['titulo']}' por {libro['autor']}")
    else:
        print(f"No hay libros desde {año_desde}")
    
    return recientes

def agregar_libro(titulo, autor, genero, año):
    datos = cargar_libros()
    nuevo_libro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "año": año
    }
    datos["libros"].append(nuevo_libro)
    guardar_libros(datos)
    print(f"✓ Libro '{titulo}' agregado correctamente")

def listar_libros():
    datos = cargar_libros()
    print("\n--- CATÁLOGO DE LIBROS ---")
    for i, libro in enumerate(datos["libros"], 1):
        print(f"{i}. '{libro['titulo']}' - {libro['autor']}")
        print(f"   Género: {libro['genero']} | Año: {libro['año']}")
    print(f"\nTotal de libros: {len(datos['libros'])}\n")

def listar_generos():
    datos = cargar_libros()
    generos = sorted(set(l["genero"] for l in datos["libros"]))
    print("\n--- Géneros disponibles ---")
    for genero in generos:
        print(f"• {genero}")

def listar_autores():
    datos = cargar_libros()
    autores = sorted(set(l["autor"] for l in datos["libros"]))
    print("\n--- Autores en el catálogo ---")
    for autor in autores:
        print(f"• {autor}")

def menu():
    while True:
        print("\n=== CATÁLOGO DE LIBROS ===")
        print("1. Listar todos los libros")
        print("2. Filtrar por género")
        print("3. Filtrar por autor")
        print("4. Listar libros recientes")
        print("5. Agregar libro")
        print("6. Ver géneros disponibles")
        print("7. Ver autores")
        print("8. Inicializar con datos de ejemplo")
        print("0. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            listar_libros()
        elif opcion == "2":
            listar_generos()
            genero = input("\nIngrese el género: ")
            filtrar_por_genero(genero)
        elif opcion == "3":
            listar_autores()
            autor = input("\nIngrese el autor: ")
            filtrar_por_autor(autor)
        elif opcion == "4":
            año = input("Desde qué año [2000]: ") or "2000"
            listar_libros_recientes(int(año))
        elif opcion == "5":
            titulo = input("Título: ")
            autor = input("Autor: ")
            genero = input("Género: ")
            año = int(input("Año: "))
            agregar_libro(titulo, autor, genero, año)
        elif opcion == "6":
            listar_generos()
        elif opcion == "7":
            listar_autores()
        elif opcion == "8":
            inicializar_libros()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()
