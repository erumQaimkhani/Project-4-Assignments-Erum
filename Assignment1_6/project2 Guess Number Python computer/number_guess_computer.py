# project 2:  guess the number game by computer .
# Date: 24th march 2025
# 1 to 100

import random

def guess_the_number():
    """This function is used to guess the number by computer"""
    number = random.randint(1, 100)
    guesses_left = 6
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # loop for guessing
    while guesses_left > 0:
        print(f"\nYou have {guesses_left} attempts remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        # checking the guessed number
        if guess < number:
            print("Too low! Think again.")
        elif guess > number:
            print("Too high! Think again.")
        else:
            print(f"Congratulations! You've guessed the number in {6 - guesses_left + 1} attempts.")
            break
        
        guesses_left -= 1
    
    # if the user is out of guesses
    if guesses_left == 0:
        print("\nYou've run out of guesses. You lose.")
        print(f"The number was {number}")

    # Asking user if they want to play again
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        guess_the_number()
    else:
        print("Thanks for playing! meet you next time.")

# Start the game
guess_the_number()


# https://colab.research.google.com/drive/18Z2pdJNl2h8suD7QE3DeSdkd-rRxzf7N#scrollTo=CsPgEmRqsC5s&line=48&uniqifier=1
