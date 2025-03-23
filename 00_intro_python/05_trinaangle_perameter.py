def main():
    print("This program calculates the perimeter of a triangle.")
    
    # User se triangle ke sides ke length lena
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))
    
    # Perimeter calculate 3 side one by one
    perimeter = side1 + side2 + side3
    
    # Out put
    print(f"The perimeter of the triangle is {perimeter}")

# Program ko run karne ke liye ye line zaroori hai
if __name__ == '__main__':
    main()
# https://colab.research.google.com/drive/1RVsio_GMvwVq6LHQykS-nBzNQNgM74gs#scrollTo=EkCtxzpF0yle&line=14&uniqifier=1