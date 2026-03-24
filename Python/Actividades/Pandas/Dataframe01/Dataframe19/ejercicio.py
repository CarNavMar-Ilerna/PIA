import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
excel1_path = os.path.join(script_dir, 'alumnos_grupo1.xlsx')
excel2_path = os.path.join(script_dir, 'alumnos_grupo2.xlsx')
salida_path = os.path.join(script_dir, 'alumnos_fusionados.xlsx')

if not os.path.exists(excel1_path):
    datos1 = {
        'Nombre': ['Ana', 'Luis', 'Marta', 'Carlos'],
        'Edad': [19, 21, 20, 18],
        'Programacion': [8.5, 6.0, 9.0, 5.5],
        'Base de Datos': [7.0, 5.5, 8.5, 6.0],
        'Sistemas': [6.5, 7.0, 7.5, 4.5],
        'Lenguajes': [9.0, 4.5, 8.0, 5.0],
        'Redes': [5.5, 8.0, 6.5, 7.0],
    }
    pd.DataFrame(datos1).to_excel(excel1_path, index=False)

if not os.path.exists(excel2_path):
    datos2 = {
        'Nombre': ['Elena', 'Pedro', 'Sara', 'Jorge'],
        'Edad': [22, 23, 19, 20],
        'Programacion': [7.5, 4.0, 8.0, 6.5],
        'Base de Datos': [9.0, 3.5, 7.5, 5.0],
        'Sistemas': [8.5, 5.0, 6.0, 7.0],
        'Lenguajes': [6.5, 6.0, 9.5, 4.0],
        'Redes': [7.0, 6.5, 5.0, 8.5],
    }
    pd.DataFrame(datos2).to_excel(excel2_path, index=False)

df1 = pd.read_excel(excel1_path)
df2 = pd.read_excel(excel2_path)
df_fusionado = pd.concat([df1, df2], ignore_index=True)
df_fusionado.to_excel(salida_path, index=False)

print(f"Datos fusionados guardados en: {salida_path}")
print(df_fusionado.to_string(index=False))
