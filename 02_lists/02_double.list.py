# Is code mein humne numbers ki list ko double kiya hai bina kisi function ya method ke istemal kiye.
# Ye ek simple example hai jo list ke elements ko double karta hai.
def main():
    # List ke numbers define kiye hain
    numbers = [1, 2, 3, 4]
    fruits = ['apple', 'banana', 'cherry']
    # List ko print kiya
    print(numbers[0])  # Pehla element print kiya
    print(numbers[1:-6])  # Dusra element print kiya
    print(fruits[1:-3])  # Slicing ka istemal kiya

    # Har element ko double karne ke liye loop chalayi
    for i in range(len(numbers)):
        numbers[i] *= 2  # Directly element ko double kar diya

    # Updated list ko print kiya
    print(numbers)

if __name__ == '__main__':
    main()