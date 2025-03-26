# Topic :project 4 - Rock, Paper, Scissors
# Description: This is a simple rock, paper, scissors game. The user will play against the computer. The user will be prompted to enter their choice of rock, paper, or scissors. The computer will randomly select one of the three options. The winner will be determined based on the rules of the game. The user will be prompted to play again or quit. The game will continue until the user decides to quit.
# Author: Erum Azeemi Qaimkhani

import random

# Game choices
choices = ['rock', 'paper', 'scissors']

def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return f"You win! {player_choice} beats {computer_choice}."
    else:
        return f"Computer wins! {computer_choice} beats {player_choice}."

def play_game():
    while True:
        # Get player choice
        player_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
        if player_choice not in choices:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue
        
        # Get computer choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        # Determine winner
        result = get_winner(player_choice, computer_choice)
        print(result)
        
        # Ask to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Good luck nice meet to you!")
            break

if __name__ == "__main__":
    play_game()
