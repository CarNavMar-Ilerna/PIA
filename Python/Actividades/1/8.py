#Crearemos un set llamado frutas
frutas = {"manzana", "banana", "naranja", "uva"}
print(frutas)

#Agregamos una nueva fruta al set
frutas.add("pera")
print(frutas)

#Intentamos agregar una fruta que ya existe
frutas.add("banana")
print(frutas)

#Eliminamos la naranja del set
frutas.remove("naranja")
print(frutas)

#Imprimimos todos los elementos del set
for fruta in frutas:
    print(fruta)