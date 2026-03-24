import pandas as pd
import matplotlib.pyplot as plt

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

plt.figure(figsize=(8, 6))
plt.scatter(df['Programacion'], df['Base de Datos'], color='steelblue', s=100, edgecolors='black')

for i, row in df.iterrows():
    plt.annotate(row['Nombre'], (row['Programacion'], row['Base de Datos']), textcoords="offset points", xytext=(5, 5))

plt.xlabel('Nota en Programación')
plt.ylabel('Nota en Base de Datos')
plt.title('Relación entre notas de Programación y Base de Datos')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('dispersion_prog_bd.png')
plt.show()
print("Gráfico guardado como 'dispersion_prog_bd.png'")
