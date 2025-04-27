'''
Rock Paper Scissor (Score,Round 1-5)
'''
import random

player_score = 0
computer_score = 0
t = True
while t:
    computer = ["R","P","S"]
    computer_choose = random.choice(computer)
    player_choose = input("Enter [R] if Rock , [P] if Paper , [S] if Scissor:")
    print(" ")
    if computer_choose == player_choose:
        print("You and Computer is Tied")
        print(" ")
    if computer_choose == "R" and player_choose == "S":
        print("Computer Choose Rock")
        print("Computer Win")
        print(" ")
        computer_score += 1
    elif computer_choose == "P" and player_choose == "R":
        print("Computer Choose Paper")
        print("Computer Win")
        print(" ")
        computer_score += 1
    elif computer_choose == "S" and player_choose == "P":
        print("Computer Choose Scissor")
        print("Computer Win")
        print(" ")
        computer_score += 1
    if computer_choose == "R" and player_choose == "P":
        print("Computer Choose Rock")
        print("Player Win")
        print(" ")
        player_score += 1
    elif computer_choose == "P" and player_choose == "S":
        print("Computer Choose Paper")
        print("Player Win")
        print(" ")
        player_score += 1
    elif computer_choose == "S" and player_choose == "R":
        print("Computer Choose Scissor")
        print("Player Win")
        print(" ")
        player_score += 1

    if player_score == 5:
        print("Player Win the Round")
        break
    elif player_score == 5:
        print("Computer Win the Round")
        break
