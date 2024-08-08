from random import randint


def check_die(score, die_value):
    if die_value == 1:
        return 0
    else:
        return score + die_value


def display_scoreboard(player_score, computer_score):
    print()
    print("#" * 20)
    print(f"Player Score: {player_score}")
    print(f"Computer Score: {computer_score}")
    print("#" * 20)
    print()


player_score = 0
computer_score = 0

welcome_message = """
          Welcome to 'Pig', a dice game!
    
    In this game, a user and a computer opponent 
    roll a 6-sided die each round. If the value of
    the die is a 1, the player that rolled the 1 loses
    all of their points. Otherwise, the player gets the
    value of the die added to their points. The first
    player to reach 30 points wins!
"""

print(welcome_message)

username = input("What is your name? ")

while True:
    input(f"Press 'Enter' to roll the die {username}!\n")

    player_die_value = randint(1, 6)
    print(f"{username} rolls a {player_die_value}")

    computer_die_value = randint(1, 6)
    print(f"Computer rolls a {computer_die_value}")

    player_score = check_die(player_score, player_die_value)
    computer_score = check_die(computer_score, computer_die_value)

    display_scoreboard(player_score, computer_score)

    if player_score >= 30:
        print(f"{username} wins!")
        break
    elif computer_score >= 30:
        print("Computer wins!")
        break


#En español
from random import randint

def check_die(puntaje, valor_dado):
    if die_value == 1:
        return 0
    else:
        return puntuación + valor del dado


def display_scoreboard(puntuación del jugador, puntuación de la computadora):
    print()
    print("#" * 20)
    print(f"Player Score: {puntuación del jugador}")
    print(f"Computer Score: {puntuación de la computadora}")
    print("#" * 20)
    print()


puntuación_del_jugador = 0
puntuación_del_ordenador = 0

welcome_message = """
          ¡Bienvenidos a 'Pig', un juego de dados!
    
    En este juego, un usuario y un oponente de la computadora
    tiran un dado de 6 caras en cada ronda. Si el valor del dado es 1, 
    el jugador que sacó el 1 pierde todos sus puntos. De lo contrario, 
    el jugador obtiene el valor del dado agregado a sus puntos. 
    ¡El primer jugador que alcance los 30 puntos gana!
"""

print(mensaje_de_bienvenida)

nombre de usuario = input("Cuál es tu nombre? ")

while True:
    input(f"Presiona 'Enter' para lanzar el dado {nombre de usuario}!\n")

    valor_dado_jugador = randint(1, 6)
    print(f"{nombre de usuario} rolls a {valor del dado del jugador}")

    valor del dado de computadora = randint(1, 6)
    print(f"La computadora hace girar una {valor_del_troquel_de_computadora}")

    puntuación del jugador = check_die(puntuación del jugador, valor del dado del jugador)
    puntuación de la computadora = check_die(puntuación del jugador, valor del dado del jugador)

    mostrar_marcador(puntuación del jugador, puntuación de la computadora)

    if puntuación del jugador >= 30:
        print(f"{usuario} gana!")
        break
    elif puntuación de la computadora >= 30:
        print("La computadora gana!")
        break
