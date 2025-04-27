print("Write your name")
name = input()

print("Hello! "+name)

pas = input("Please enter the password:")
if pas == "STEM12B":
    print("Hi Welcome")
    fruits = input("Enter a fruit letter that start with A-C:")
    if fruits == ("a") or fruits == ("A"):
        print ("Fruit that start with A is: Apple")
    elif fruits == ("b") or fruits == ("B"):
         print ("Fruit that start with B is: Banana")
    elif fruits == ("c") or fruits == ("C"):
         print ("Fruit that start with C is: Camalansi")
    else:
         print("The letter isn't part of the list")
     