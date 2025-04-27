'''
Hangman
'''
import random

Capital_word = ""
list_word = []
list_clue = []
num = 0
Finish = True 
def Give_Random_Words ():
    words = ["Rock","Space","Lion","King","Toy","Story","Gun","Mask","Spy","Earth",
    "Asteroid","Comb","Spider","Insect",
    "Mug","Cup","Mouse"]
    word = random.choice(words)
    capital_word = word.upper()
    return capital_word

Capital_word = Give_Random_Words()
#print(Capital_word)

for x in Capital_word:
    list_word.append(x)
#print(list_word)

for x in Capital_word:
    list_clue.append("_")
    num += 1 
#print(list_clue)

def give_clue(list_w,list_c,number):
    if number < 5:
        for x in range (1):
            letter = random.choice(list_w)
            index_clue = list_w.index(letter)
            list_c.pop(index_clue)
            list_c.insert(index_clue,letter)
    elif number < 10:
        for x in range (3):
            letter = random.choice(list_w)
            index_clue = list_w.index(letter)
            list_c.pop(index_clue)
            list_c.insert(index_clue,letter)
    elif number < 15:
        for x in range (5):
            letter = random.choice(list_w)
            index_clue = list_w.index(letter)
            list_c.pop(index_clue)
            list_c.insert(index_clue,letter)
    elif number < 18:
        for x in range (7):
            letter = random.choice(list_w)
            index_clue = list_w.index(letter)
            list_c.pop(index_clue)
            list_c.insert(index_clue,letter)
    return list_c

list_clue = give_clue(list_word,list_clue,num)
print(list_clue)

while Finish:
    letter = input("Enter an Letter:")
    
    if letter in list_word:
        p =(list_word.index(letter))
        list_clue.pop(p)
        list_clue.insert(p,letter)
        print(list_clue)
    if list_word == list_clue:
        Finish = False
        print("Congrats You completed it")