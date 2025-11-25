import json
import os

ARCHIVO_JSON = "informacion_alumnos.json"

def cargar_alumnos():
    if os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    else:
        return {"alumnos": []}

def guardar_alumnos(datos):
    with open(ARCHIVO_JSON, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)

def inicializar_alumnos():
    alumnos_iniciales = {
        "alumnos": [
            {"nombre": "Carlos", "edad": 20, "calificacion": 85, "ciudad": "Madrid"},
            {"nombre": "Lucía", "edad": 22, "calificacion": 90, "ciudad": "Barcelona"},
            {"nombre": "Miguel", "edad": 19, "calificacion": 45, "ciudad": "Valencia"},
            {"nombre": "Ana", "edad": 21, "calificacion": 75, "ciudad": "Sevilla"},
            {"nombre": "Pedro", "edad": 23, "calificacion": 60, "ciudad": "Madrid"},
            {"nombre": "Laura", "edad": 20, "calificacion": 95, "ciudad": "Barcelona"},
            {"nombre": "Javier", "edad": 22, "calificacion": 55, "ciudad": "Bilbao"},
            {"nombre": "Elena", "edad": 21, "calificacion": 80, "ciudad": "Valencia"},
            {"nombre": "David", "edad": 24, "calificacion": 70, "ciudad": "Madrid"},
            {"nombre": "Sara", "edad": 19, "calificacion": 88, "ciudad": "Sevilla"}
        ]
    }
    guardar_alumnos(alumnos_iniciales)
    print("✓ Registro inicializado con 10 alumnos")

def filtrar_aprobados(nota_minima=60):
    datos = cargar_alumnos()
    aprobados = [a for a in datos["alumnos"] if a["calificacion"] >= nota_minima]
    
    print(f"\n--- ALUMNOS APROBADOS (nota >= {nota_minima}) ---")
    if aprobados:
        for alumno in aprobados:
            print(f"• {alumno['nombre']} - Calificación: {alumno['calificacion']} - Ciudad: {alumno['ciudad']}")
        print(f"\nTotal aprobados: {len(aprobados)}")
    else:
        print("No hay alumnos aprobados")
    
    return aprobados

def calcular_edad_promedio():
    datos = cargar_alumnos()
    if datos["alumnos"]:
        promedio = sum(a["edad"] for a in datos["alumnos"]) / len(datos["alumnos"])
        print(f"\n📊 Edad promedio: {promedio:.2f} años")
        return promedio
    else:
        print("No hay alumnos registrados")
        return 0

def calcular_calificacion_promedio():
    datos = cargar_alumnos()
    if datos["alumnos"]:
        promedio = sum(a["calificacion"] for a in datos["alumnos"]) / len(datos["alumnos"])
        print(f"\n📊 Calificación promedio: {promedio:.2f}")
        return promedio
    else:
        print("No hay alumnos registrados")
        return 0

def agregar_alumno(nombre, edad, calificacion, ciudad):
    datos = cargar_alumnos()
    nuevo_alumno = {
        "nombre": nombre,
        "edad": edad,
        "calificacion": calificacion,
        "ciudad": ciudad
    }
    datos["alumnos"].append(nuevo_alumno)
    guardar_alumnos(datos)
    print(f"✓ Alumno {nombre} agregado correctamente")

def eliminar_alumno(nombre):
    datos = cargar_alumnos()
    alumnos_originales = len(datos["alumnos"])
    datos["alumnos"] = [a for a in datos["alumnos"] if nombre.lower() not in a["nombre"].lower()]
    
    if len(datos["alumnos"]) < alumnos_originales:
        guardar_alumnos(datos)
        print(f"✓ Alumno(s) con nombre '{nombre}' eliminado(s)")
    else:
        print(f"No se encontró el alumno '{nombre}'")

def filtrar_por_ciudad(ciudad):
    datos = cargar_alumnos()
    alumnos_ciudad = [a for a in datos["alumnos"] if a["ciudad"].lower() == ciudad.lower()]
    
    if alumnos_ciudad:
        print(f"\n--- Alumnos de {ciudad} ---")
        for alumno in alumnos_ciudad:
            print(f"• {alumno['nombre']} - Edad: {alumno['edad']} - Calificación: {alumno['calificacion']}")
    else:
        print(f"No hay alumnos de {ciudad}")
    
    return alumnos_ciudad

def listar_alumnos():
    datos = cargar_alumnos()
    print("\n--- INFORMACIÓN DE ALUMNOS ---")
    for i, alumno in enumerate(datos["alumnos"], 1):
        estado = "✓ Aprobado" if alumno["calificacion"] >= 60 else "✗ Suspenso"
        print(f"{i}. {alumno['nombre']} ({alumno['edad']} años)")
        print(f"   Calificación: {alumno['calificacion']} {estado} | Ciudad: {alumno['ciudad']}")
    print(f"\nTotal de alumnos: {len(datos['alumnos'])}\n")

def menu():
    while True:
        print("\n=== INFORMACIÓN DE ALUMNOS ===")
        print("1. Listar todos los alumnos")
        print("2. Filtrar alumnos aprobados")
        print("3. Calcular edad promedio")
        print("4. Calcular calificación promedio")
        print("5. Agregar alumno")
        print("6. Eliminar alumno")
        print("7. Filtrar por ciudad")
        print("8. Inicializar con datos de ejemplo")
        print("0. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            listar_alumnos()
        elif opcion == "2":
            nota = input("Nota mínima para aprobar [60]: ") or "60"
            filtrar_aprobados(int(nota))
        elif opcion == "3":
            calcular_edad_promedio()
        elif opcion == "4":
            calcular_calificacion_promedio()
        elif opcion == "5":
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            calificacion = int(input("Calificación: "))
            ciudad = input("Ciudad: ")
            agregar_alumno(nombre, edad, calificacion, ciudad)
        elif opcion == "6":
            nombre = input("Nombre del alumno a eliminar: ")
            eliminar_alumno(nombre)
        elif opcion == "7":
            ciudad = input("Ciudad: ")
            filtrar_por_ciudad(ciudad)
        elif opcion == "8":
            inicializar_alumnos()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()
