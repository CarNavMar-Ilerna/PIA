#Ejercicios de matemáticas y números aleatorios

#1.Tirada de dados(con 2 dados)
import random
def tirar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2
print("Tirada de dados:", tirar_dados())
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#2.La ruleta
def girar_ruleta():
    return random.randint(0, 36)
print("Número de la ruleta:", girar_ruleta())
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#3.Baraja de cartas (repartir 5 cartas)
def repartir_cartas():
    palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    baraja = [f"{valor} de {palo}" for palo in palos for valor in valores]
    random.shuffle(baraja)
    return baraja[:5]
print("Cartas repartidas:", repartir_cartas())
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#4.Adivinar número en la ruleta
def adivinar_numero(numero_usuario):
    numero_ruleta = girar_ruleta()
    if numero_usuario == numero_ruleta:
        print("¡Felicidades! Has adivinado el número.")
    else:
        print(f"Lo siento, el número era {numero_ruleta}.")
print("Adivina el número de la ruleta (0-36):")
numero_usuario = int(input())
adivinar_numero(numero_usuario)
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#5.BlackJack simple
def jugar_blackjack():
    def valor_carta(carta):
        if carta in ['J', 'Q', 'K']:
            return 10
        elif carta == 'A':
            return 11
        else:
            return int(carta)

    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']*4
    baraja = [f"{valor} " for valor in valores]
    random.shuffle(baraja)

    mano_jugador = [baraja.pop(), baraja.pop()]
    mano_casa = [baraja.pop(), baraja.pop()]

    puntaje_jugador = sum(valor_carta(carta.split()[0]) for carta in mano_jugador)
    puntaje_casa = sum(valor_carta(carta.split()[0]) for carta in mano_casa)

    print("Mano del jugador:", mano_jugador, "Puntaje:", puntaje_jugador)
    print("Mano de la casa:", mano_casa, "Puntaje:", puntaje_casa)

    if puntaje_jugador > 21:
        print("El jugador se pasa. La casa gana.")
    elif puntaje_casa > 21 or puntaje_jugador > puntaje_casa:
        print("El jugador gana.")
    elif puntaje_jugador < puntaje_casa:
        print("La casa gana.")
    else:
        print("Empate.")
jugar_blackjack()
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#6.La quiniela
def generar_quiniela():
    resultados = []
    for _ in range(15):
        resultado = random.choices(['1', 'X', '2'], weights=[0.5, 0.25, 0.25])[0]
        resultados.append(resultado)
    return resultados
print("Resultados de la quiniela:", generar_quiniela())
print("...............................................................................")

#-------------------------------------------------------------------------------------------

#7.La primitiva
def generar_primitiva():
    numeros = random.sample(range(1, 50), 6)
    numeros.sort()
    return numeros
print("Números de la primitiva:", generar_primitiva())