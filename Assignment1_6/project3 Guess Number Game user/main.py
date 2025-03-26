# https://colab.research.google.com/drive/18Z2pdJNl2h8suD7QE3DeSdkd-rRxzf7N#scrollTo=FpyLibwd_TuK&line=1&uniqifier=1

#3 project guess the number game python  project (user)
# Made by Erum Azeemi Qaimkhani

import random
print("Welcome to the Guess the Number Game!")
print("I am thinking of a number between 1 and 100.")
#generating random number
number = random.randint(1, 100)

while True:
    #taking input from user
    guess = int(input("Enter an integer from 1 to 100: "))
    #checking the guess
    if guess < number:
        print("Your guess is too low, try again.")
    elif guess > number:
        print("Your guess is too high, try again.")
    else:
        print("Congratulations! You guessed it correctly.")
        break