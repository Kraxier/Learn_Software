
import random

user = input("Pick Rock[1],Paper[2],Scissor[3]:")
computer = random.randint(1,3)

#Rock 1 
#Paper 2
# Scissor 3

if computer == 1 and user == "1":
    print("You and Computer are Tied")
if computer == 2 and user == "2":
    print("You and Computer are Tied")
if computer == 3 and user == "3":
    print("You and Computer are Tied")

if computer == 3 and user == "1":
    print("You win")
elif computer == 2 and user == "3":
    print("You win")
elif computer == 1 and user == "2":
    print("You win")

if computer == 3 and user == "2":
    print("Computer Win")
elif computer == 2 and user == "1":
    print("Computer Win")
elif computer == 1 and user == "3":
    print("Computer Win")

