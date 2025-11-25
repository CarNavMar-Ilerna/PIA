import json
import os

ARCHIVO_JSON = "concesionario_coches.json"

def cargar_coches():
    if os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    else:
        return {"coches": []}

def guardar_coches(datos):
    with open(ARCHIVO_JSON, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)

def inicializar_coches():
    coches_iniciales = {
        "coches": [
            {"marca": "Toyota", "modelo": "Corolla", "precio": 20000, "año": 2023},
            {"marca": "Ford", "modelo": "Focus", "precio": 18000, "año": 2022},
            {"marca": "Honda", "modelo": "Civic", "precio": 22000, "año": 2023},
            {"marca": "Volkswagen", "modelo": "Golf", "precio": 25000, "año": 2024},
            {"marca": "BMW", "modelo": "Serie 3", "precio": 40000, "año": 2023},
            {"marca": "Mercedes", "modelo": "Clase A", "precio": 35000, "año": 2022},
            {"marca": "Audi", "modelo": "A4", "precio": 38000, "año": 2023},
            {"marca": "Seat", "modelo": "León", "precio": 21000, "año": 2024},
            {"marca": "Renault", "modelo": "Megane", "precio": 19000, "año": 2022},
            {"marca": "Peugeot", "modelo": "308", "precio": 23000, "año": 2023}
        ]
    }
    guardar_coches(coches_iniciales)
    print("✓ Concesionario inicializado con 10 vehículos")

def filtrar_por_marca(marca):
    datos = cargar_coches()
    coches_marca = [c for c in datos["coches"] if c["marca"].lower() == marca.lower()]
    
    if coches_marca:
        print(f"\n--- Coches de marca {marca} ---")
        for coche in coches_marca:
            print(f"• {coche['modelo']} ({coche['año']}) - ${coche['precio']:,}")
    else:
        print(f"No hay coches de la marca {marca}")
    
    return coches_marca

def calcular_precio_promedio():
    datos = cargar_coches()
    if datos["coches"]:
        promedio = sum(c["precio"] for c in datos["coches"]) / len(datos["coches"])
        print(f"\n💰 Precio promedio de los coches: ${promedio:,.2f}")
        return promedio
    else:
        print("No hay coches registrados")
        return 0

def actualizar_precio(marca, modelo, nuevo_precio):
    datos = cargar_coches()
    encontrado = False
    
    for coche in datos["coches"]:
        if coche["marca"].lower() == marca.lower() and coche["modelo"].lower() == modelo.lower():
            coche["precio"] = nuevo_precio
            encontrado = True
            print(f"✓ Precio de {coche['marca']} {coche['modelo']} actualizado a ${nuevo_precio:,}")
    
    if encontrado:
        guardar_coches(datos)
    else:
        print(f"No se encontró el coche {marca} {modelo}")

def filtrar_por_año(año):
    datos = cargar_coches()
    coches_año = [c for c in datos["coches"] if c["año"] == año]
    
    if coches_año:
        print(f"\n--- Coches del año {año} ---")
        for coche in coches_año:
            print(f"• {coche['marca']} {coche['modelo']} - ${coche['precio']:,}")
    else:
        print(f"No hay coches del año {año}")
    
    return coches_año

def agregar_coche(marca, modelo, precio, año):
    datos = cargar_coches()
    nuevo_coche = {
        "marca": marca,
        "modelo": modelo,
        "precio": precio,
        "año": año
    }
    datos["coches"].append(nuevo_coche)
    guardar_coches(datos)
    print(f"✓ Coche {marca} {modelo} agregado correctamente")

def listar_coches():
    datos = cargar_coches()
    print("\n--- CONCESIONARIO DE COCHES ---")
    for i, coche in enumerate(datos["coches"], 1):
        print(f"{i}. {coche['marca']} {coche['modelo']} ({coche['año']})")
        print(f"   Precio: ${coche['precio']:,}")
    print(f"\nTotal de coches: {len(datos['coches'])}\n")

def listar_marcas():
    datos = cargar_coches()
    marcas = sorted(set(c["marca"] for c in datos["coches"]))
    print("\n--- Marcas disponibles ---")
    for marca in marcas:
        print(f"• {marca}")

def menu():
    while True:
        print("\n=== CONCESIONARIO DE COCHES ===")
        print("1. Listar todos los coches")
        print("2. Filtrar por marca")
        print("3. Filtrar por año")
        print("4. Calcular precio promedio")
        print("5. Actualizar precio")
        print("6. Agregar coche")
        print("7. Ver marcas disponibles")
        print("8. Inicializar con datos de ejemplo")
        print("0. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            listar_coches()
        elif opcion == "2":
            listar_marcas()
            marca = input("\nIngrese la marca: ")
            filtrar_por_marca(marca)
        elif opcion == "3":
            año = int(input("Ingrese el año: "))
            filtrar_por_año(año)
        elif opcion == "4":
            calcular_precio_promedio()
        elif opcion == "5":
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            precio = float(input("Nuevo precio: "))
            actualizar_precio(marca, modelo, precio)
        elif opcion == "6":
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            precio = float(input("Precio: "))
            año = int(input("Año: "))
            agregar_coche(marca, modelo, precio, año)
        elif opcion == "7":
            listar_marcas()
        elif opcion == "8":
            inicializar_coches()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()
