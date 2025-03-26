# Project 7: Hangman
# Made by: Erum Azeemi Qaimkhani

# Importing the necessary libraries
import random
from words import words
from hangman_visual import lives_visual_dict
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 10

    while len(word_letters) > 0 and lives > 0:
        # Status display
        print(f"\nYou have {lives} lives left and you have used these letters: {' '.join(sorted(used_letters))}")

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        # User input
        user_letter = input('Guess a letter: ').strip().upper()

        if len(user_letter) != 1 or user_letter not in alphabet:
            print("Invalid input. Please enter a single letter from A-Z.")
            continue

        if user_letter in used_letters:
            print(f"You've already guessed '{user_letter}'. Try again!")
            continue

        # Add the guessed letter
        used_letters.add(user_letter)

        if user_letter in word_letters:
            word_letters.remove(user_letter)
            print(f"Good job! '{user_letter}' is in the word.")
        else:
            lives -= 1
            print(f"Oops! '{user_letter}' is NOT in the word. You lost a life.")

    # Game over message
    if lives == 0:
        print(lives_visual_dict[lives])
        print(f"you died, extremly sorry'{word}'.")
    else:
        print(f"YAY! You guessed the word '{word}'!! 🎉")

    # Option to play again
    play_again = input("\nDo you want to play again? (Y/N): ").strip().upper()
    if play_again == 'Y':
        hangman()
    else:
        print("Thanks for playing!  nice meet you to next time 👋")

if __name__ == '__main__':
    hangman()

