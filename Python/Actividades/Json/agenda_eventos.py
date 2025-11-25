import json
import os
from datetime import datetime

ARCHIVO_JSON = "agenda_eventos.json"

def cargar_eventos():
    if os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    else:
        return {"eventos": []}

def guardar_eventos(datos):
    with open(ARCHIVO_JSON, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)

def inicializar_eventos():
    eventos_iniciales = {
        "eventos": [
            {"titulo": "Conferencia Python", "fecha": "2024-11-15", "ubicacion": "Madrid", "organizador": "PyCon España"},
            {"titulo": "Taller de IA", "fecha": "2024-12-01", "ubicacion": "Barcelona", "organizador": "TechFest"},
            {"titulo": "Hackathon 2024", "fecha": "2024-11-20", "ubicacion": "Valencia", "organizador": "DevCommunity"},
            {"titulo": "Meetup JavaScript", "fecha": "2024-11-10", "ubicacion": "Madrid", "organizador": "JS España"},
            {"titulo": "Seminario Cloud", "fecha": "2024-12-05", "ubicacion": "Sevilla", "organizador": "CloudExperts"},
            {"titulo": "Workshop React", "fecha": "2024-11-25", "ubicacion": "Barcelona", "organizador": "Frontend Masters"},
            {"titulo": "Conferencia DevOps", "fecha": "2024-12-10", "ubicacion": "Madrid", "organizador": "DevOps Spain"},
            {"titulo": "Charla Ciberseguridad", "fecha": "2024-11-18", "ubicacion": "Bilbao", "organizador": "SecureIT"},
            {"titulo": "Feria Tecnológica", "fecha": "2024-12-15", "ubicacion": "Barcelona", "organizador": "TechExpo"},
            {"titulo": "Curso Machine Learning", "fecha": "2024-11-30", "ubicacion": "Madrid", "organizador": "AI Academy"}
        ]
    }
    guardar_eventos(eventos_iniciales)
    print("✓ Agenda inicializada con 10 eventos")

def filtrar_por_fecha(fecha):
    datos = cargar_eventos()
    eventos_fecha = [e for e in datos["eventos"] if e["fecha"] == fecha]
    
    if eventos_fecha:
        print(f"\n--- Eventos del {fecha} ---")
        for evento in eventos_fecha:
            print(f"• {evento['titulo']}")
            print(f"  Ubicación: {evento['ubicacion']} | Organizador: {evento['organizador']}")
    else:
        print(f"No hay eventos para la fecha {fecha}")
    
    return eventos_fecha

def filtrar_por_ubicacion(ubicacion):
    datos = cargar_eventos()
    eventos_ubicacion = [e for e in datos["eventos"] if ubicacion.lower() in e["ubicacion"].lower()]
    
    if eventos_ubicacion:
        print(f"\n--- Eventos en {ubicacion} ---")
        for evento in eventos_ubicacion:
            print(f"• {evento['titulo']} - {evento['fecha']}")
            print(f"  Organizador: {evento['organizador']}")
    else:
        print(f"No hay eventos en {ubicacion}")
    
    return eventos_ubicacion

def agregar_evento(titulo, fecha, ubicacion, organizador):
    datos = cargar_eventos()
    nuevo_evento = {
        "titulo": titulo,
        "fecha": fecha,
        "ubicacion": ubicacion,
        "organizador": organizador
    }
    datos["eventos"].append(nuevo_evento)
    guardar_eventos(datos)
    print(f"✓ Evento '{titulo}' agregado correctamente")

def eliminar_eventos_pasados(fecha_actual):
    datos = cargar_eventos()
    eventos_originales = len(datos["eventos"])
    datos["eventos"] = [e for e in datos["eventos"] if e["fecha"] >= fecha_actual]
    
    eliminados = eventos_originales - len(datos["eventos"])
    if eliminados > 0:
        guardar_eventos(datos)
        print(f"✓ Se eliminaron {eliminados} evento(s) pasado(s)")
    else:
        print("No hay eventos pasados para eliminar")

def listar_eventos():
    datos = cargar_eventos()
    print("\n--- AGENDA DE EVENTOS ---")
    for i, evento in enumerate(datos["eventos"], 1):
        print(f"{i}. {evento['titulo']} - {evento['fecha']}")
        print(f"   Ubicación: {evento['ubicacion']} | Organizador: {evento['organizador']}")
    print(f"\nTotal de eventos: {len(datos['eventos'])}\n")

def menu():
    while True:
        print("\n=== AGENDA DE EVENTOS ===")
        print("1. Listar todos los eventos")
        print("2. Filtrar por fecha")
        print("3. Filtrar por ubicación")
        print("4. Agregar evento")
        print("5. Eliminar eventos pasados")
        print("6. Inicializar con datos de ejemplo")
        print("0. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            listar_eventos()
        elif opcion == "2":
            fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
            filtrar_por_fecha(fecha)
        elif opcion == "3":
            ubicacion = input("Ingrese la ubicación: ")
            filtrar_por_ubicacion(ubicacion)
        elif opcion == "4":
            titulo = input("Título: ")
            fecha = input("Fecha (YYYY-MM-DD): ")
            ubicacion = input("Ubicación: ")
            organizador = input("Organizador: ")
            agregar_evento(titulo, fecha, ubicacion, organizador)
        elif opcion == "5":
            fecha = input("Fecha actual (YYYY-MM-DD): ")
            eliminar_eventos_pasados(fecha)
        elif opcion == "6":
            inicializar_eventos()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()
