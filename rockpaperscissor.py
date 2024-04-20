import random
import time

""" Oyuncuların yapabilecekleri seçimler tanımlanıyor."""
player_1_actions = ["rock", "paper", "scissors"]
player_2_actions = ["rock", "paper", "scissors"]

rounds = int(input("How many rounds you wanna play? : "))
score_of_the_player_1 = 0
score_of_the_player_2 = 0

"""For Döngüsü """
for round_num in range(1, rounds + 1):
    print("Round:", round_num)
    time.sleep(2)
    """
    Oyuncuların yapabilecekleri seçimler arasından rastgele olarak biri seçiliyor ve oyuncuların 
    yaptığı rastgele seçime değişken tanımlanıyor.
    """
    player_1_choice = random.choice(player_1_actions)
    player_2_choice = random.choice(player_2_actions)

    print("Player 1 chose:", player_1_choice)
    print("Player 2 chose:", player_2_choice)

    """ - Tie Beraberlik Koşulu ve Bu Durumda Ekrana Verilecek Output """
    tie = (player_1_choice == player_2_choice)
    if tie:
        print("Tie! Both players chose the same action.")

    """Oyuncuların kazanma durumları ve bunları sağlayan koşullar"""
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







