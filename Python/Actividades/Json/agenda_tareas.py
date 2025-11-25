import json
import os
from datetime import datetime

ARCHIVO_JSON = "agenda_tareas.json"

def cargar_tareas():
    if os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    else:
        return {"tareas": []}

def guardar_tareas(datos):
    with open(ARCHIVO_JSON, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)

def inicializar_tareas():
    tareas_iniciales = {
        "tareas": [
            {"descripcion": "Estudiar Python", "vencimiento": "2024-11-01", "estado": "pendiente"},
            {"descripcion": "Revisar proyecto", "vencimiento": "2024-10-29", "estado": "completada"},
            {"descripcion": "Hacer ejercicios de JSON", "vencimiento": "2024-11-05", "estado": "pendiente"},
            {"descripcion": "Preparar presentación", "vencimiento": "2024-11-10", "estado": "en progreso"},
            {"descripcion": "Leer documentación", "vencimiento": "2024-11-03", "estado": "completada"},
            {"descripcion": "Practicar algoritmos", "vencimiento": "2024-11-08", "estado": "pendiente"},
            {"descripcion": "Revisar código", "vencimiento": "2024-11-02", "estado": "completada"},
            {"descripcion": "Escribir tests", "vencimiento": "2024-11-12", "estado": "pendiente"},
            {"descripcion": "Actualizar README", "vencimiento": "2024-11-06", "estado": "en progreso"},
            {"descripcion": "Refactorizar módulo", "vencimiento": "2024-11-15", "estado": "pendiente"}
        ]
    }
    guardar_tareas(tareas_iniciales)
    print("✓ Agenda inicializada con 10 tareas")

def agregar_tarea(descripcion, vencimiento, estado="pendiente"):
    datos = cargar_tareas()
    nueva_tarea = {
        "descripcion": descripcion,
        "vencimiento": vencimiento,
        "estado": estado
    }
    datos["tareas"].append(nueva_tarea)
    guardar_tareas(datos)
    print(f"✓ Tarea '{descripcion}' agregada correctamente")

def actualizar_estado(descripcion, nuevo_estado):
    datos = cargar_tareas()
    encontrado = False
    
    for tarea in datos["tareas"]:
        if descripcion.lower() in tarea["descripcion"].lower():
            tarea["estado"] = nuevo_estado
            encontrado = True
            print(f"✓ Estado de '{tarea['descripcion']}' actualizado a '{nuevo_estado}'")
    
    if encontrado:
        guardar_tareas(datos)
    else:
        print(f"No se encontró la tarea '{descripcion}'")

def filtrar_completadas():
    datos = cargar_tareas()
    completadas = [t for t in datos["tareas"] if t["estado"].lower() == "completada"]
    
    print("\n--- TAREAS COMPLETADAS ---")
    if completadas:
        for tarea in completadas:
            print(f"✓ {tarea['descripcion']} (Vencimiento: {tarea['vencimiento']})")
    else:
        print("No hay tareas completadas")
    
    return completadas

def filtrar_pendientes():
    datos = cargar_tareas()
    pendientes = [t for t in datos["tareas"] if t["estado"].lower() != "completada"]
    
    print("\n--- TAREAS PENDIENTES ---")
    if pendientes:
        for tarea in pendientes:
            print(f"• {tarea['descripcion']} - Estado: {tarea['estado']} (Vencimiento: {tarea['vencimiento']})")
    else:
        print("No hay tareas pendientes")
    
    return pendientes

def listar_tareas():
    datos = cargar_tareas()
    print("\n--- AGENDA DE TAREAS ---")
    for i, tarea in enumerate(datos["tareas"], 1):
        icono = "✓" if tarea["estado"] == "completada" else "•"
        print(f"{i}. {icono} {tarea['descripcion']}")
        print(f"   Estado: {tarea['estado']} | Vencimiento: {tarea['vencimiento']}")
    print(f"\nTotal de tareas: {len(datos['tareas'])}\n")

def menu():
    while True:
        print("\n=== AGENDA DE TAREAS ===")
        print("1. Listar todas las tareas")
        print("2. Agregar nueva tarea")
        print("3. Actualizar estado de tarea")
        print("4. Filtrar tareas completadas")
        print("5. Filtrar tareas pendientes")
        print("6. Inicializar con datos de ejemplo")
        print("0. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            listar_tareas()
        elif opcion == "2":
            descripcion = input("Descripción: ")
            vencimiento = input("Fecha de vencimiento (YYYY-MM-DD): ")
            estado = input("Estado (pendiente/en progreso/completada) [pendiente]: ") or "pendiente"
            agregar_tarea(descripcion, vencimiento, estado)
        elif opcion == "3":
            descripcion = input("Descripción de la tarea: ")
            estado = input("Nuevo estado (pendiente/en progreso/completada): ")
            actualizar_estado(descripcion, estado)
        elif opcion == "4":
            filtrar_completadas()
        elif opcion == "5":
            filtrar_pendientes()
        elif opcion == "6":
            inicializar_tareas()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()
