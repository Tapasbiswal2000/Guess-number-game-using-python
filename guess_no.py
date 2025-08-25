#importing random module for generate random numbers.
import random

random_no = random.randint(1,1000)

while True:
    try:        
        userChoice = input("Guess a number and for quit press Q  : ")
        if(userChoice == "Q"):
            break
        userChoice = int(userChoice)
        if(userChoice == random_no):
            print("YOU SUCCESSfully did it")
            break

        elif(userChoice > random_no):
            print("You are going too big , Guess smaller.")

        else:
            print("You are going too small , Guess bigger.")
    except ValueError:
        print("invalid choice.")

print("----GAME OVER----")