# Step 3: Simulate rolling dice.

from random import randint


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

    break

#Español
# Paso 3: Simular el lanzamiento de dados.

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

    valor del dado del jugador = randint(1, 6)
    print(f"{nombre de usuario} rueda un {valor del dado del jugador}")

    valor del dado de computadora = randint(1, 6)
    print(f"La computadora lanza un {computer_die_value}")

    break

