#Creamos una tupla llamada dias_semana
dias_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
print(dias_semana)

#Verificamos si "Sabado" está en la tupla
print("Sábado" in dias_semana)

#Usamos un loop para imprimir cada día de la semana
for dia in dias_semana:
    print(dia)

#Intentamos cambiar el primer elemento de la tupla
try:
    dias_semana[0] = "Luness"
except TypeError as e:
    print("Error:", e)
print(dias_semana)

