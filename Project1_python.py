import random

target = random.randint(1,100)

while True:

    userChoice = input("Guess the target or Quit : ")

    if(userChoice == "Quite"):
        break

    userChoice = int(userChoice)

    if(userChoice == target):
        print("Success : Correct Guess!!")
        break

    elif(userChoice < target):
        print("Your number was too small.Guess the bigger number...")
    else:
        print("Your number was too big.Guess the smaller number...")


print("GAME OVER.....")