## Problem Statement

# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

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
# An example program with constants
# """

# INCHES_IN_FOOT: int = 12  # Conversion factor. There are 12 inches for 1 foot.

# def main():
#     feet: float = float(input("Enter number of feet: "))  # Get the number of feet, make sure to cast it to a float!
#     inches: float = feet * INCHES_IN_FOOT  # Perform the conversion
#     print("That is", inches, "inches!")
    
    
# # This provided line is required at the end of a Python file
# # to call the main() function.
# if __name__ == '__main__':
#     main()
# ```
# Conversion factor (1 foot = 12 inches)
INCHES_IN_FOOT = 12  

def main():
    # User se feet input lena
    feet = float(input("Enter number of feet: "))

    # Conversion karna
    inches = feet * INCHES_IN_FOOT
    
    # Result show karna
    print(f"{feet} feet is equal to {inches} inches.")

# Program ko run karne ke liye zaroori hai
if __name__ == '__main__':
    main()
