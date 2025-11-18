#Ejercicios con fechas

#1.Obtener la fecha y hora actual
from datetime import datetime, timedelta
fecha_hora_actual = datetime.now()
print("Fecha y hora actual:", fecha_hora_actual)
#Formatea la fecha
fecha_formateada = fecha_hora_actual.strftime("%d/%m/%Y %H:%M:%S")
print("Fecha y hora formateada:", fecha_formateada)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#2.Convierte una cadena a una fecha
cadena_fecha = "25/12/2023 15:30:00"
fecha_convertida = datetime.strptime(cadena_fecha, "%d/%m/%Y %H:%M:%S")
print("Fecha convertida desde cadena:", fecha_convertida)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#3.Calcula la diferencia entre dos fechas
fecha1 = datetime(2023, 12, 25, 15, 30, 0)
fecha2 = datetime(2024, 1, 1, 10, 0, 0)
diferencia = fecha2 - fecha1
print("Diferencia entre fechas:", diferencia)
print("Días de diferencia:", diferencia.days)
print("Segundos de diferencia:", diferencia.seconds)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#4.Suma dias a una fecha
dias_a_sumar = 10
nueva_fecha = fecha1 + timedelta(days=dias_a_sumar)
print("Fecha original:", fecha1)
print("Nueva fecha después de sumar", dias_a_sumar, "días:", nueva_fecha)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#5.Convierte una fecha a otro formato
fecha_ejemplo = datetime(2023, 12, 25, 15, 30, 0)
fecha_reformateada = fecha_ejemplo.strftime("%A, %d de %B de %Y a las %H:%M")
print("Fecha reformateada:", fecha_reformateada)