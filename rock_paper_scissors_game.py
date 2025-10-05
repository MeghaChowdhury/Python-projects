import random

choices = ['r', 'p', 's']
emoji_map = {'r': '🪨', 'p': '📃', 's': '✂️'}

while True:
    guess = input("Rock, Paper or Scissors? (r/p/s): ")
    if guess not in choices:
        print("Invalid choice")
        continue

    comp_choice = random.choice(choices)

    print(f"You chose {emoji_map[guess]}")
    print(f"Computer chose {emoji_map[comp_choice]}")

    if guess == comp_choice:
        print("It's a tie!")
    elif (
         (guess == 'r' and comp_choice == 's') or
         (guess == 'p' and comp_choice == 'r') or
         (guess == 's' and comp_choice == 'p')):
        print("You win!")
    else:
        print("You lose!")

    frage = input("Continue? (y/n): ").lower()
    if frage == 'n':
        break
