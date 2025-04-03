# Problem Statement
# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48


import random

def guess_my_number():
    """A simple number guessing game."""
    secret_number = random.randint(0, 99)  # Random number between 0 and 99

    print("I am thinking of a number between 0 and 99...")
    guess = None  # Initialize guess variable

    while guess != secret_number:
        try:
            if guess is None:
                guess = int(input("Enter a guess: "))
            else:
                guess = int(input("Enter a new number: "))
        except ValueError:
            print("Please enter a valid number!")
            continue  # Ask again if input is not a number

        if guess < secret_number:
            print("Your guess is too low")
        elif guess > secret_number:
            print("Your guess is too high")
        else:
            print(f"Congrats! The number was: {secret_number}")
            break  # Exit the loop when guessed correctly

# Run the game
guess_my_number()
