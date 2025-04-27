import random

''''
Lucky Nine
'''
    
Player = random.randint(1,9)
Player_2 = random.randint(1,9)
Banker = random.randint(1,9)
Banker_v2 = random.randint(1,9)
player_card = Player + Player_2
banker_card = Banker + Banker_v2
if player_card >= 10:
    player_card -= 10
if banker_card >= 10:
    banker_card -= 10
bet = input("Pick Player[P] or Banker[B]:")


print(player_card)
print(banker_card)

if player_card<banker_card:
    print("Banker Win")
if player_card>banker_card:
    print("Player Win")