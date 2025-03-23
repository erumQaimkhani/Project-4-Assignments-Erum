# 02_agreement_bot.md
# https://colab.research.google.com/drive/10Gt1ieZXjIPqfQCWUskDMajYt0UQAzQJ#scrollTo=C-VcbIgYmxJD&line=1&uniqifier=1


def main():
    print("This program adds two numbers.")

    # Taking input from the user and converting to integer
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Calculating the sum
    total = num1 + num2

    # Displaying the result
    print(f"The total is {total}.")

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
