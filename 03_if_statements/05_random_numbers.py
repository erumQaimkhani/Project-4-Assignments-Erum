# Problem Statement
# Print 10 random numbers in the range 1 to 100.

# Here is an example run:

# 45 79 61 47 52 10 16 83 19 12

# Each time you run your program you should get different numbers

# 81 76 70 1 27 63 96 100 32 92

# Recall that the python random library has a function randint which returns an integer in the range set by the parameters (inclusive). For example this call would produce a random integer between 1 and 6, which could include 1 and could include 6:

# value = random.randint(1, 6)
import random

N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

def main():
    """Random numbers generate karna aur unka analysis karna."""
    numbers = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]
    
    print("\n🎲 Generated Random Numbers:", numbers)
    
    # Chhota se bada sort karna
    sorted_numbers = sorted(numbers)
    print("\n🔢 Sorted Numbers:", sorted_numbers)

    # Sabse bada aur chhota number
    print("\n📉 Smallest Number:", min(numbers))
    print("📈 Largest Number:", max(numbers))

    # Total aur Average
    total = sum(numbers)
    average = total / N_NUMBERS
    print("\n➕ Total:", total)
    print("📊 Average:", round(average, 2))

if __name__ == '__main__':
    main()
