# zuri task: create a rock paper scissors game
import random
plays = ["rock", "paper", "scissors"]
round = 3
player_points = 0
computer_points = 0


def validate(computer, player):

    tie = False
    global computer_points, player_points, round
    round = round - 1
    print("", name, "("+player+")", "\n CPU ", "("+computer+")")
    if computer != player:
        if computer == 'rock':
            if player == 'scissors':
                print(" COMPUTER WINS!!! ")
                computer_points += 1
            else:
                print("", name, " WINS!!! ")
                player_points += 1
        elif computer == "paper":
            if player == "rock":
                print(" COMPUTER WINS!!! ")
                computer_points += 1
            else:
                print("", name, " WINS!!! ")
                player_points += 1
        else:
            if player == "paper":
                print(" COMPUTER WINS!!! ")
                computer_points += 1
            else:
                print("", name, " WINS!!! ")
                player_points += 1

    else:
        print(" TIE!!!")
        tie = True

    print(" SCORES", "\n Computer:", computer_points,
          "\n " + name, player_points)

    return tie


name = input("Enter player name: ")

while(round > 0):
    print("\nRock-R Paper-P Scissors-S")

    player_input = input("Enter: ")
    if player_input == "R":
        player_choice = "rock"
    elif player_input == "P":
        player_choice = "paper"
    elif player_input == "S":
        player_choice = "scissors"
    else:
        print("\nchoose something appropriate")
        continue
    computer_choice = random.choice(plays)
    if validate(computer_choice, player_choice):
        print("A TIE HAS OCCURED")
        continue
