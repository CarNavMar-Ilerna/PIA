#Ejercicios del 31 al 40 Listas

#31.Crea una lista que contenga números y cadenas
mezcla = [2, 45, "pizza", 34, "peru"]

#Accede al segundo elemento
print(mezcla[1])
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#32. Usa enumerate() para imprimir el indice y valor de cada elemento de una lista
indice = ['patata', 'manzana', 'guayaba']
indice_enum = enumerate(indice)
print(list(indice_enum))
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#33.Crea una lista de listas
listade = [["pollos", "cerdos", "ovejas"],["patatas", "zanahorias", "lechuga"]]

#Usa for para recorrer los elementos de cada lista
for interior in listade:
    for x in interior:
        print(x)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#34.Usa del para eliminar el rango de elementos de una lista de números
numeros = [2, 33, 45, 21, 83, 56]
del numeros[2:4]
print(numeros)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#35.Filtra los elementos de una lista de números para obtener solo los 5 mayores
numeros2 = [2, 33, 45, 21, 83, 56, 38, 23, 90]
numeros2.sort()
numeros2.reverse()
print(numeros2[:5])
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#36.Crea una lista de cadenas y usa split() para dividir cada cadena en palabras
lista_cadenas = [
    "Este es un ejemplo",
    "Otro texto más largo para probar",
    "Palabras",
    "Una cadena con  espacios extra"
]
for cadena in lista_cadenas:
    palabras = cadena.split()
    print(palabras)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#37.Convierte en tupla en una lista y luego añade un nuevo elemento
tupla = ("pollo", "conejo", "vaca")
tupla_lista = list(tupla)
tupla_lista.append("borrego")
print(tupla_lista)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#38.Usa set() para eliminar los elementos duplicados de una lista
mi_lista = [10, 32, 32, 38, 41, 41, 57, 10]
lista_sin_duplicados = list(set(mi_lista))
print(lista_sin_duplicados)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#39.Crea una lista de números
numeros3 =  [3, 14, 56, 2, 76, 23]

#Invierte el orden de los números sin usar reverse()
numeros_invertidos = numeros3[::-1]
print(numeros_invertidos)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#40.Divide una lista en partes iguales
numeros4 = [7, 3, 4, 9, 12, 34, 54, 67]
primera_parte = numeros4[:2]
segunda_parte = numeros4[2:4]
tercera_parte = numeros4[4:6]
cuarta_parte = numeros4[6:8]
print(primera_parte, segunda_parte, tercera_parte, cuarta_parte)