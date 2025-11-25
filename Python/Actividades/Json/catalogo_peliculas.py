import json
import os

ARCHIVO_JSON = "catalogo_peliculas.json"

def cargar_peliculas():
    if os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    else:
        return {"peliculas": []}

def guardar_peliculas(datos):
    with open(ARCHIVO_JSON, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)

def inicializar_peliculas():
    peliculas_iniciales = {
        "peliculas": [
            {"titulo": "El Laberinto del Fauno", "director": "Guillermo del Toro", "año": 2006, "genero": "Fantasía"},
            {"titulo": "Mar Adentro", "director": "Alejandro Amenábar", "año": 2004, "genero": "Drama"},
            {"titulo": "Todo sobre mi Madre", "director": "Pedro Almodóvar", "año": 1999, "genero": "Drama"},
            {"titulo": "El Orfanato", "director": "J.A. Bayona", "año": 2007, "genero": "Terror"},
            {"titulo": "Volver", "director": "Pedro Almodóvar", "año": 2006, "genero": "Drama"},
            {"titulo": "Los Otros", "director": "Alejandro Amenábar", "año": 2001, "genero": "Terror"},
            {"titulo": "Rec", "director": "Jaume Balagueró", "año": 2007, "genero": "Terror"},
            {"titulo": "La Piel que Habito", "director": "Pedro Almodóvar", "año": 2011, "genero": "Thriller"},
            {"titulo": "Celda 211", "director": "Daniel Monzón", "año": 2009, "genero": "Thriller"},
            {"titulo": "Ocho Apellidos Vascos", "director": "Emilio Martínez-Lázaro", "año": 2014, "genero": "Comedia"}
        ]
    }
    guardar_peliculas(peliculas_iniciales)
    print("✓ Catálogo inicializado con 10 películas")

def filtrar_por_genero(genero):
    datos = cargar_peliculas()
    peliculas_genero = [p for p in datos["peliculas"] if p["genero"].lower() == genero.lower()]
    
    if peliculas_genero:
        print(f"\n--- Películas de género '{genero}' ---")
        for pelicula in peliculas_genero:
            print(f"• '{pelicula['titulo']}' - {pelicula['director']} ({pelicula['año']})")
    else:
        print(f"No hay películas del género '{genero}'")
    
    return peliculas_genero

def listar_directores():
    datos = cargar_peliculas()
    directores = sorted(set(p["director"] for p in datos["peliculas"]))
    print("\n--- Directores únicos ---")
    for director in directores:
        peliculas_director = [p for p in datos["peliculas"] if p["director"] == director]
        print(f"• {director} ({len(peliculas_director)} película(s))")
    return directores

def agregar_pelicula(titulo, director, año, genero):
    datos = cargar_peliculas()
    nueva_pelicula = {
        "titulo": titulo,
        "director": director,
        "año": año,
        "genero": genero
    }
    datos["peliculas"].append(nueva_pelicula)
    guardar_peliculas(datos)
    print(f"✓ Película '{titulo}' agregada correctamente")

def filtrar_por_director(director):
    datos = cargar_peliculas()
    peliculas_director = [p for p in datos["peliculas"] if director.lower() in p["director"].lower()]
    
    if peliculas_director:
        print(f"\n--- Películas de '{director}' ---")
        for pelicula in peliculas_director:
            print(f"• '{pelicula['titulo']}' ({pelicula['año']}) - {pelicula['genero']}")
    else:
        print(f"No hay películas del director '{director}'")
    
    return peliculas_director

def listar_peliculas():
    datos = cargar_peliculas()
    print("\n--- CATÁLOGO DE PELÍCULAS ---")
    for i, pelicula in enumerate(datos["peliculas"], 1):
        print(f"{i}. '{pelicula['titulo']}' ({pelicula['año']})")
        print(f"   Director: {pelicula['director']} | Género: {pelicula['genero']}")
    print(f"\nTotal de películas: {len(datos['peliculas'])}\n")

def listar_generos():
    datos = cargar_peliculas()
    generos = sorted(set(p["genero"] for p in datos["peliculas"]))
    print("\n--- Géneros disponibles ---")
    for genero in generos:
        print(f"• {genero}")

def menu():
    while True:
        print("\n=== CATÁLOGO DE PELÍCULAS ===")
        print("1. Listar todas las películas")
        print("2. Filtrar por género")
        print("3. Filtrar por director")
        print("4. Listar directores únicos")
        print("5. Agregar película")
        print("6. Ver géneros")
        print("7. Inicializar con datos de ejemplo")
        print("0. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            listar_peliculas()
        elif opcion == "2":
            listar_generos()
            genero = input("\nIngrese el género: ")
            filtrar_por_genero(genero)
        elif opcion == "3":
            director = input("Ingrese el director: ")
            filtrar_por_director(director)
        elif opcion == "4":
            listar_directores()
        elif opcion == "5":
            titulo = input("Título: ")
            director = input("Director: ")
            año = int(input("Año: "))
            genero = input("Género: ")
            agregar_pelicula(titulo, director, año, genero)
        elif opcion == "6":
            listar_generos()
        elif opcion == "7":
            inicializar_peliculas()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()
