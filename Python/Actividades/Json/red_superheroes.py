import json
import os

ARCHIVO_JSON = "red_superheroes.json"

def cargar_superheroes():
    if os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    else:
        return {"superheroes": []}

def guardar_superheroes(datos):
    with open(ARCHIVO_JSON, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)

def inicializar_superheroes():
    superheroes_iniciales = {
        "superheroes": [
            {"alias": "El Cid", "habilidades": ["esgrima", "estrategia"], "ciudad": "Burgos", "equipo": "Los Defensores"},
            {"alias": "La Dama de Plata", "habilidades": ["manipulación de metales"], "ciudad": "Toledo", "equipo": "Los Defensores"},
            {"alias": "El Guardián", "habilidades": ["super fuerza", "vuelo"], "ciudad": "Madrid", "equipo": "Los Vengadores"},
            {"alias": "Sombra Nocturna", "habilidades": ["invisibilidad", "sigilo"], "ciudad": "Barcelona", "equipo": "Los Vengadores"},
            {"alias": "Relámpago", "habilidades": ["super velocidad", "electricidad"], "ciudad": "Valencia", "equipo": "Los Defensores"},
            {"alias": "Fénix", "habilidades": ["regeneración", "fuego"], "ciudad": "Sevilla", "equipo": "Los Inmortales"},
            {"alias": "Titán", "habilidades": ["super fuerza", "resistencia"], "ciudad": "Madrid", "equipo": "Los Vengadores"},
            {"alias": "Mente Maestra", "habilidades": ["telepatía", "telequinesis"], "ciudad": "Bilbao", "equipo": "Los Inmortales"},
            {"alias": "Águila Dorada", "habilidades": ["vuelo", "visión telescópica"], "ciudad": "Zaragoza", "equipo": "Los Defensores"},
            {"alias": "Cristal", "habilidades": ["manipulación de cristales", "escudos"], "ciudad": "Barcelona", "equipo": "Los Inmortales"}
        ]
    }
    guardar_superheroes(superheroes_iniciales)
    print("✓ Red inicializada con 10 superhéroes")

def filtrar_por_ciudad(ciudad):
    datos = cargar_superheroes()
    heroes_ciudad = [h for h in datos["superheroes"] if h["ciudad"].lower() == ciudad.lower()]
    
    if heroes_ciudad:
        print(f"\n--- Superhéroes de {ciudad} ---")
        for heroe in heroes_ciudad:
            print(f"• {heroe['alias']} - Equipo: {heroe['equipo']}")
            print(f"  Habilidades: {', '.join(heroe['habilidades'])}")
    else:
        print(f"No hay superhéroes en {ciudad}")
    
    return heroes_ciudad

def filtrar_por_equipo(equipo):
    datos = cargar_superheroes()
    heroes_equipo = [h for h in datos["superheroes"] if h["equipo"].lower() == equipo.lower()]
    
    if heroes_equipo:
        print(f"\n--- Miembros de '{equipo}' ---")
        for heroe in heroes_equipo:
            print(f"• {heroe['alias']} ({heroe['ciudad']})")
            print(f"  Habilidades: {', '.join(heroe['habilidades'])}")
    else:
        print(f"No hay superhéroes en el equipo '{equipo}'")
    
    return heroes_equipo

def listar_habilidades_unicas():
    datos = cargar_superheroes()
    habilidades = set()
    for heroe in datos["superheroes"]:
        habilidades.update(heroe["habilidades"])
    
    print("\n--- Habilidades únicas ---")
    for habilidad in sorted(habilidades):
        print(f"• {habilidad}")
    
    return sorted(habilidades)

def agregar_superheroe(alias, habilidades, ciudad, equipo):
    datos = cargar_superheroes()
    nuevo_heroe = {
        "alias": alias,
        "habilidades": habilidades,
        "ciudad": ciudad,
        "equipo": equipo
    }
    datos["superheroes"].append(nuevo_heroe)
    guardar_superheroes(datos)
    print(f"✓ Superhéroe '{alias}' agregado correctamente")

def listar_superheroes():
    datos = cargar_superheroes()
    print("\n--- RED DE SUPERHÉROES ---")
    for i, heroe in enumerate(datos["superheroes"], 1):
        print(f"{i}. {heroe['alias']} - {heroe['equipo']}")
        print(f"   Ciudad: {heroe['ciudad']} | Habilidades: {', '.join(heroe['habilidades'])}")
    print(f"\nTotal de superhéroes: {len(datos['superheroes'])}\n")

def listar_equipos():
    datos = cargar_superheroes()
    equipos = sorted(set(h["equipo"] for h in datos["superheroes"]))
    print("\n--- Equipos disponibles ---")
    for equipo in equipos:
        miembros = len([h for h in datos["superheroes"] if h["equipo"] == equipo])
        print(f"• {equipo} ({miembros} miembro(s))")

def listar_ciudades():
    datos = cargar_superheroes()
    ciudades = sorted(set(h["ciudad"] for h in datos["superheroes"]))
    print("\n--- Ciudades ---")
    for ciudad in ciudades:
        print(f"• {ciudad}")

def menu():
    while True:
        print("\n=== RED DE SUPERHÉROES ===")
        print("1. Listar todos los superhéroes")
        print("2. Filtrar por ciudad")
        print("3. Filtrar por equipo")
        print("4. Listar habilidades únicas")
        print("5. Agregar superhéroe")
        print("6. Ver equipos")
        print("7. Ver ciudades")
        print("8. Inicializar con datos de ejemplo")
        print("0. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            listar_superheroes()
        elif opcion == "2":
            listar_ciudades()
            ciudad = input("\nIngrese la ciudad: ")
            filtrar_por_ciudad(ciudad)
        elif opcion == "3":
            listar_equipos()
            equipo = input("\nIngrese el equipo: ")
            filtrar_por_equipo(equipo)
        elif opcion == "4":
            listar_habilidades_unicas()
        elif opcion == "5":
            alias = input("Alias: ")
            habilidades_str = input("Habilidades (separadas por coma): ")
            habilidades = [h.strip() for h in habilidades_str.split(",")]
            ciudad = input("Ciudad: ")
            equipo = input("Equipo: ")
            agregar_superheroe(alias, habilidades, ciudad, equipo)
        elif opcion == "6":
            listar_equipos()
        elif opcion == "7":
            listar_ciudades()
        elif opcion == "8":
            inicializar_superheroes()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()
