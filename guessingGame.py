import random

userInp = int(input("enter your choice from 1 to 10 :-"))
randomNumber = random.randint(1,10)

if(userInp == randomNumber):
    print("Congrats you guessed the right one ")
else:print("Upps you guessed the wrong the correct guess would be :-",randomNumber)
