import random

choices = ['r', 'p', 's']
emoji_map = {'r': '🪨', 'p': '📃', 's': '✂️'}

def get_user_choice():
    while True:
        guess = input("Rock, Paper or Scissors? (r/p/s): ")
        if guess in choices:
            return guess
        else:
            print('Invalid choice')

def print_choices(guess, comp_choice):
    print(f"You chose {emoji_map[guess]}")
    print(f"Computer chose {emoji_map[comp_choice]}")

def determine_winner(guess, comp_choice):
    if guess == comp_choice:
        print("It's a tie!")
    elif (
        (guess == 'r' and comp_choice == 's') or
        (guess == 'p' and comp_choice == 'r') or
        (guess == 's' and comp_choice == 'p')
    ):
        print("You win!")
    else:
        print("You lose!")

def play_game():
    while True:
        guess = get_user_choice()
        comp_choice = random.choice(choices)
        print_choices(guess, comp_choice)
        determine_winner(guess, comp_choice)
        frage = input("Continue? (y/n): ").lower()
        if frage == 'n':
            break

play_game()
