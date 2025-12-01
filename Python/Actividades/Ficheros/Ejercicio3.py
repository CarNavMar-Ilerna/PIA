import csv


def leer_cotizaciones(fichero):
    cotizaciones = {
        'Nombre': [],
        'Final': [],
        'Máximo': [],
        'Mínimo': [],
        'Volumen': [],
        'Efectivo': []
    }
    
    try:
        with open(fichero, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo, delimiter=';')
            for fila in lector:
                cotizaciones['Nombre'].append(fila['Nombre'])
                cotizaciones['Final'].append(float(fila['Final'].replace(',', '.')))
                cotizaciones['Máximo'].append(float(fila['Máximo'].replace(',', '.')))
                cotizaciones['Mínimo'].append(float(fila['Mínimo'].replace(',', '.')))
                cotizaciones['Volumen'].append(float(fila['Volumen'].replace('.', '').replace(',', '.')))
                cotizaciones['Efectivo'].append(float(fila['Efectivo'].replace('.', '').replace(',', '.')))
        
        return cotizaciones
    except FileNotFoundError:
        print(f'El fichero {fichero} no existe.')
        return None


def crear_estadisticas(diccionario):
    if diccionario is None:
        return
    
    estadisticas = {}
    
    for columna in ['Final', 'Máximo', 'Mínimo', 'Volumen', 'Efectivo']:
        valores = diccionario[columna]
        estadisticas[columna] = {
            'Mínimo': min(valores),
            'Máximo': max(valores),
            'Media': sum(valores) / len(valores)
        }
    
    with open('estadisticas.csv', 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(['Columna', 'Mínimo', 'Máximo', 'Media'])
        
        for columna, stats in estadisticas.items():
            escritor.writerow([
                columna,
                stats['Mínimo'],
                stats['Máximo'],
                stats['Media']
            ])
    
    print('Estadísticas guardadas en estadisticas.csv')


if __name__ == '__main__':
    print("=== Ejercicio 3: Cotizaciones IBEX35 ===")
    
    fichero = input("Introduce el nombre del fichero de cotizaciones (cotizacion.csv): ") or 'cotizacion.csv'
    
    print("\n1. Leer cotizaciones")
    cotizaciones = leer_cotizaciones(fichero)
    
    if cotizaciones:
        print(f"\nDatos leídos: {len(cotizaciones['Nombre'])} empresas")
        print(f"Columnas: {', '.join(cotizaciones.keys())}")
        
        print("\n2. Crear estadísticas")
        crear_estadisticas(cotizaciones)
