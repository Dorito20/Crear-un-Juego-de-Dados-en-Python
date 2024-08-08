# Step 4: Create a function to update the scores of each player

from random import randint


def update_score(score, die_value):
    if die_value == 1:
        return 0
    else:
        return score + die_value


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

    player_score = update_score(player_score, player_die_value)
    computer_score = update_score(computer_score, computer_die_value)

    print(f"{player_score=}")
    print(f"{computer_score=}")

    break


#Español
# Step 4: Create a function to update the scores of each player

from random import randint


def update_score(score, die_value):
    if die_value == 1:
        return 0
    else:
        return score + die_value


puntuación_del_jugador = 0
puntuación_del_ordenador = 0

mensaje_de_llegada = """
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

    valor del dado del jugador = randint(1, 6)
    print(f"{username} lanza un {player_die_value}")

    valor del dado de computadora = randint(1, 6)
    print(f"La computadora lanza un {computer_die_value}")

    puntuación del jugador = update_score(puntuación del jugador, valor del dado del jugador)
    puntuación de la computadora = update_score(puntuación de la computadora, valor del dado de la computadora)

    print(f"{puntuación del jugador=}")
    print(f"{puntuación de la computadora=}")

    break