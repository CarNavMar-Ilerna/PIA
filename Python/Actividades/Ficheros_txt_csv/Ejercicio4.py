import csv
import os


def leer_calificaciones(fichero):
    ruta_fichero = os.path.join(os.path.dirname(__file__), fichero)
    alumnos = []
    
    try:
        with open(ruta_fichero, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                alumno = {
                    'Apellidos': fila['Apellidos'],
                    'Asistencia': float(fila['Asistencia']),
                    'Parcial1': float(fila['Parcial1']),
                    'Parcial2': float(fila['Parcial2']),
                    'Ordinaria': float(fila['Ordinaria'])
                }
                alumnos.append(alumno)
        
        return alumnos
    except FileNotFoundError:
        print(f'El fichero {fichero} no existe.')
        return None


def calcular_notas_finales(lista_alumnos):
    for alumno in lista_alumnos:
        nota_teoria = (alumno['Parcial1'] + alumno['Parcial2']) / 2
        nota_practica = alumno['Ordinaria']
        
        nota_final = nota_teoria * 0.3 + nota_practica * 0.4
        
        alumno['NotaFinal'] = round(nota_final, 2)
    
    return lista_alumnos


def separar_aprobados_suspensos(lista_alumnos):
    aprobados = []
    suspensos = []
    
    for alumno in lista_alumnos:
        asistencia_ok = alumno['Asistencia'] >= 75
        
        media_parciales_practica = (alumno['Parcial1'] + alumno['Parcial2'] + alumno['Ordinaria']) / 3
        media_ok = media_parciales_practica >= 4
        
        nota_final_ok = alumno['NotaFinal'] >= 5
        
        if asistencia_ok and media_ok and nota_final_ok:
            aprobados.append(alumno)
        else:
            suspensos.append(alumno)
    
    return aprobados, suspensos


if __name__ == '__main__':
    print("=== Ejercicio 4: Calificaciones del Curso ===")
    
    fichero = input("Introduce el nombre del fichero de calificaciones (calificaciones.csv): ") or 'calificaciones.csv'
    
    print("\n1. Leer calificaciones")
    alumnos = leer_calificaciones(fichero)
    
    if alumnos:
        print(f"Datos leídos: {len(alumnos)} alumnos")
        
        print("\n2. Calcular notas finales")
        alumnos = calcular_notas_finales(alumnos)
        
        print("\nNotas finales calculadas:")
        for alumno in alumnos:
            print(f"{alumno['Apellidos']}: {alumno['NotaFinal']}")
        
        print("\n3. Separar aprobados y suspensos")
        aprobados, suspensos = separar_aprobados_suspensos(alumnos)
        
        print(f"\nAprobados: {len(aprobados)}")
        for alumno in aprobados:
            print(f"  - {alumno['Apellidos']}: {alumno['NotaFinal']}")
        
        print(f"\nSuspensos: {len(suspensos)}")
        for alumno in suspensos:
            print(f"  - {alumno['Apellidos']}: {alumno['NotaFinal']}")
