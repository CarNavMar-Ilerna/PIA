import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
excel_path = os.path.join(script_dir, 'alumnos.xlsx')
salida_path = os.path.join(script_dir, 'alumnos_mayores22.xlsx')

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
    pd.DataFrame(datos).to_excel(excel_path, index=False)

df = pd.read_excel(excel_path)
mayores = df[df['Edad'] > 22]
mayores.to_excel(salida_path, index=False)

print(f"Alumnos mayores de 22 años guardados en: {salida_path}")
print(mayores[['Nombre', 'Edad']].to_string(index=False))
