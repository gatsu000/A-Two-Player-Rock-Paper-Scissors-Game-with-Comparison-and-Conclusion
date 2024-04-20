import random
import time

""" Defining the choices players can make."""
player_1_actions = ["rock", "paper", "scissors"]
player_2_actions = ["rock", "paper", "scissors"]

rounds = int(input("How many rounds you wanna play? : "))
score_of_the_player_1 = 0
score_of_the_player_2 = 0

"""For Loop"""
for round_num in range(1, rounds + 1):
    print("Round:", round_num)
    time.sleep(2)
    """
    One of the choices that players can make is randomly selected and a variable is defined for the random choice made by the players.
    """
    player_1_choice = random.choice(player_1_actions)
    player_2_choice = random.choice(player_2_actions)

    print("Player 1 chose:", player_1_choice)
    print("Player 2 chose:", player_2_choice)

    """ Tie Condition and Output to be Displayed in this Condition """
    tie = (player_1_choice == player_2_choice)
    if tie:
        print("Tie! Both players chose the same action.")

    """Winning situations of players and the conditions that enable them"""
    if (player_1_choice == "paper" and player_2_choice == "rock") or \
            (player_1_choice == "scissors" and player_2_choice == "paper") or \
            (player_1_choice == "rock" and player_2_choice == "scissors"):
        print("Player 1 Won!")
        score_of_the_player_1 += 1
        time.sleep(2)
    elif (player_1_choice == "paper" and player_2_choice == "scissors") or \
            (player_1_choice == "scissors" and player_2_choice == "rock") or \
            (player_1_choice == "rock" and player_2_choice == "paper"):
        print("Player 2 Won!")
        score_of_the_player_2 += 1
        time.sleep(2)
        
print("Rounds are over!")
print("Player 1 score:", score_of_the_player_1)
print("Player 2 score:", score_of_the_player_2)







