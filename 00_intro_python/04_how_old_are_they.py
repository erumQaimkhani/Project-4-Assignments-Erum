
def main():
    anton : int = 21  # Anton's age is given as 21 years old
    beth : int = 6 + anton  # Beth is 6 years older than Anton, so add 6 to Anton's age to get Beth's
    chen : int = 20 + beth  # Chen is 20 years older than Beth, so add 20 to Beth's age to get Chen's
    drew  : int= chen + anton  # Drew is as old as Chen's age plus Anton's age, so add them together
    ethan : int = chen  # Ethan is the same age as Chen, so set Ethan's age equal to Chen's
    kiran: int =5 + anton # Kiran is 5 years older than Anton, so add 5 to Anton's age to get Kiran's
   # Print out all of the ages!
    print("Anton is " + str(anton))
    print("Beth is " + str(beth))
    print("Chen is " + str(chen))
    print("Drew is " + str(drew))
    print("Ethan is " + str(ethan))
    print("Kiran is " + str(anton))


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
    # https://colab.research.google.com/drive/1ewzM9wk2Yrh2svZFR2oHcBLpTCRGD6hA#scrollTo=GSd4A2FZsCJ1&line=22&uniqifier=1