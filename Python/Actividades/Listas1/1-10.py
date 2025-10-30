#Ejercicios del 1 al 10 Listas

#1.Crea una lista con los 5 primeros números enteros
numeros = [1, 2, 3, 4, 5]

#Accedemos al 3er numero de la lista
print(numeros[2])
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#2.Crea una lista vacía
numeros2 = []

#Añadimos los números del 1 al 10 uno por uno con append()
for x in range (1 , 11):
    numeros2.append(x)
print(numeros2)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#3.Crea una lista con nombres de 5 países.
paises = ["Canada", "Perú", "Colombia", "Rusia", "China"]
print(paises)

#Cambiamos el 2º país
paises[1] = "Argentina"
print(paises)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#4.Crea una lista con 4 colores
colores = ["Verde", "Marrón", "Azul", "Violeta"]
print(colores)

#Usamos insert() para añadir un nuevo color en la posición 2
colores.insert(1, "Amarillo")
print(colores)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#5.Eliminamos el primer elemento de una lista usando pop() sin argumentos
frutas = ["Manzana", "Pera", "Melón", "Tomate", "Cereza"]
frutas.reverse()
frutas.pop()
frutas.reverse()
print(frutas)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#6.Eliminamos una lista de 4 números usando remove() para borrar un número en especifico
numeros3 = [23, 45, 72, 8]
print(numeros3)
numeros3.remove(72)
print(numeros3)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#7.Crea una lista con 6 números y la ponemos del reves
numeros4 = [3, 45, 12, 52, 78, 90]
print(numeros4)
numeros4.reverse()
print(numeros4)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#8.Usamos sort() para ordenar una lista de 6 números en orden ascendente
numeros4.sort()
print(numeros4)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#9.Crea una lista de nombre y mira cuantas veces aparece un nombre en específico
nombres = ["Pedro", "Mateo", "Juan", "Pepe", "Mateo", "Oscar", "Mateo"]
print(nombres.count("Mateo"))
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#10.Usamos el operador "in" para verificar si un elemento existe en una lista animales
animales = ["Tortuga", "Gato", "Perro", "Salamandra", "Cocodrilo"]
print("Cocodrilo" in animales)
print("Camello" in animales)