password = input("Enter the password:")
print(" ")

if password == "STEM12B":
    asking_repeat = True
    while asking_repeat:
        while True:
            try:
                secondgrade = float(input("Enter Mid Grade:"))
                sgrade = int(secondgrade)
                break
            except ValueError:
                print("It need to be a number")
                print(" ")
        while True:
            try:
                thirdgrade = float(input("Enter Final Grade:"))
                tgrade = int(thirdgrade)
                break
            except ValueError:
                print("It need to be a number")
                print(" ")
        finalgrade = (secondgrade+thirdgrade) / 2
        if finalgrade == 99 or finalgrade == 100:
            print("Your average is "+str(finalgrade)+" equal to 1.0 College Grade")
        elif finalgrade >= 96:
            print("Your Average is "+str(finalgrade)+" equal to 1.25 College Grade")
        elif finalgrade >= 93:
            print("Your Average is "+str(finalgrade)+" equal to 1.50 College Grade")
        elif finalgrade >= 90:
            print("Your Average is "+str(finalgrade)+" equal to 1.75 College Grade")
        elif finalgrade >= 87:
            print("Your Average is "+str(finalgrade)+" equal to 2.0 College Grade")
        elif finalgrade >= 84:
            print("Your Average is "+str(finalgrade)+" equal to 2.25 College Grade")
        elif finalgrade >= 81:
            print("Your Average is "+str(finalgrade)+" equal to 2.50 College Grade")
        elif finalgrade >= 78:
            print("Your Average is "+str(finalgrade)+" equal to 2.75 College Grade")
        elif finalgrade >= 75:
            print("Your Average is "+str(finalgrade)+" equal to 3.0 College Grade")
        elif finalgrade <= 74:
            print("Your Average is "+str(finalgrade)+" equal to 5.5 College Grade")
        print(" ")
        ask = input("If you want don't want to end the program enter {y or Y} if Yes, {n or N} if No:")
        if ask == "n" or ask == "N":
            asking_repeat = False
            print(" ")
            print("Thanks for Using this program")
        else:
            asking_repeat = True
            print(" ")
else:
    print("You entered wrong Password")