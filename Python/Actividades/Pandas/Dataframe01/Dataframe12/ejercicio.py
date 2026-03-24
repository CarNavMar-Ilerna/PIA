import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
excel_path = os.path.join(script_dir, 'alumnos.xlsx')
csv_path = os.path.join(script_dir, 'alumnos_copia.csv')

if not os.path.exists(excel_path):
    datos = {
        'Nombre': ['Ana', 'Luis', 'Marta', 'Carlos', 'Elena', 'Pedro', 'Sara', 'Jorge'],
        'Edad': [19, 21, 20, 18, 22, 23, 19, 20],
        'Programacion': [8.5, 6.0, 9.0, 5.5, 7.5, 4.0, 8.0, 6.5],
        'Base de Datos': [7.0, 5.5, 8.5, 6.0, 9.0, 3.5, 7.5, 5.0],
        'Sistemas': [6.5, 7.0, 7.5, 4.5, 8.5, 5.0, 6.0, 7.0],
        'Lenguajes': [9.0, 4.5, 8.0, 5.0, 6.5, 6.0, 9.5, 4.0],
        'Redes': [5.5, 8.0, 6.5, 7.0, 7.0, 6.5, 5.0, 8.5],
    }
    df = pd.DataFrame(datos)
    df.to_excel(excel_path, index=False)

df = pd.read_excel(excel_path)
df.to_csv(csv_path, index=False)
print(f"Archivo Excel guardado como CSV en: {csv_path}")
