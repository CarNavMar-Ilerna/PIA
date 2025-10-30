#Ejercicios del 11 al 20 Listas

#11.Combinamos dos listas de números usando el operador +
numeros1 = [10, 22, 33]
print(numeros1)
numeros2= [14, 1, 78]
print(numeros2)
numeros3= numeros1 + numeros2
print(numeros3)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#12.Creamos una lista de cadenas
cadenas = ["Hola", ", ", "me ", "gusta ", "la ", "fidegua "]
print(cadenas[0]+cadenas[1]+cadenas[2]+cadenas[3]+cadenas[4]+cadenas[5])
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#13.Crea una lista de números e imprime su longitud usando len()
print(len(numeros1))
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#14.Crea una lista de letras
letras = ["a", "z", "q", "m", "u"]

#Con index() obtenemos el índice de una letra en específico 
print(letras.index("q"))
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#15.Usa extend() para añadir múltiples elementos de una lista a otra
lista1 = ["huevos", "mermelada", "helados"]
lista2 = ["trapo", "lejia", "enjuague"]
lista1.extend(lista2)
print(lista1)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#16.Accede a los últimos 3 elementos de una lista usando slicing
print(cadenas[-3:])
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#17.Usa copy() para crear una copia de una lista colores
colores = ["verde", "rojo", "morado", "violeta"]
colores_copia = colores.copy()
print(colores_copia)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#18.Crea una lista de listas
lista_listas = [["cocacola", "fanta", "nestea"],["hamburguesas", "perritos", "pizzas"]]

#Accede a un elemento de una lista
print(lista_listas[1][2])
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#19.Usa clear() para eliminar todos los elementos de una lista
colores.clear()
print(colores)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#20.Multiplica una lista de 3 elementos por 4
numeros4 = [2, 5, 65]
multiplicados = numeros4 * 4
print(multiplicados)