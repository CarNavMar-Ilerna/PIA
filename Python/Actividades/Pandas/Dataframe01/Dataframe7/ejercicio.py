import pandas as pd

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
modulos = ['Programacion', 'Base de Datos', 'Sistemas', 'Lenguajes', 'Redes']
df['Promedio General'] = df[modulos].mean(axis=1).round(2)
df['Aprobado'] = df['Promedio General'] >= 5

grupos = df.groupby('Aprobado')['Nombre'].count().reset_index()
grupos.columns = ['Aprobado', 'Cantidad']
grupos['Aprobado'] = grupos['Aprobado'].map({True: 'Aprobado', False: 'Reprobado'})

print("Alumnos agrupados por estado:")
print(grupos.to_string(index=False))
