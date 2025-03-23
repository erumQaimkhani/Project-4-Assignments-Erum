## Problem Statement

# Simulate rolling two dice, and prints results of each roll as well as the total.

# ## Starter Code

# ```bash
# def main():
#     print("Delete this line and write your code here! :)")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()
# ```

# ## Solution

# ```bash
# """
# Simulate rolling two dice, and prints results of each
# roll as well as the total.
# """
# # Import the random library which lets us simulate random things like dice!
# import random

# # Number of sides on each die to roll
# NUM_SIDES: int = 6

# def main():
#     # Setting a seed is useful for debugging (uncomment the line below to do so!)
#     # random.seed(1)
    
#     # Roll die
#     die1: int = random.randint(1, NUM_SIDES)
#     die2: int = random.randint(1, NUM_SIDES)
    
#     # Get their total
#     total: int = die1 + die2
    
#     # Print out the results
#     print("Dice have", NUM_SIDES, "sides each.")
#     print("First die:", die1)
#     print("Second die:", die2)
#     print("Total of two dice:", total)


# # This provided line is required at the end of a Python file
# # to call the main() function.
# if __name__ == '__main__':
#     main()

# ```
# Random module import karna taaki hum dice roll simulate kar sakein
import random

# Ek constant define kar rahe hain: har dice mein kitne sides hain
NUM_SIDES = 6

def main():
    # Dice roll karna: har die ke liye random number between 1 and 6
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    
    # Dono dice ke numbers ka sum calculate karna
    total = die1 + die2
    
    # Results ko print karna
    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)

# Yeh line ensure karti hai ki main() function run ho
if __name__ == '__main__':
    main()
