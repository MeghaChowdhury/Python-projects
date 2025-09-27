import random

dice = (1,2,3,4,5,6)

while True:
    player = input("roll the dice? (y/n): ").upper()

    if player == "Y":
        print((random.choice(dice), random.choice(dice)))
    elif player == "N":
        print("Thanks for playing!")
        break
    else:
        print("Invalid input!")
