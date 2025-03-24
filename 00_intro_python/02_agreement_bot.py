# 02_agreement_bot.md
# https://colab.research.google.com/drive/10Gt1ieZXjIPqfQCWUskDMajYt0UQAzQJ#scrollTo=C-VcbIgYmxJD&line=1&uniqifier=1


def main():
    print("What's your favorite animal?")
    animal = input()
    print("My favorite animal is also {}!".format(animal))


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

