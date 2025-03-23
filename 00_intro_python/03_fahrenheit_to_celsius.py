

def main():
    print("This program converts Fahrenheit to Celsius.")
    
    # User se Fahrenheit input lena (float ke saath)
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    # Fahrenheit ko Celsius mein convert 
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0
    
    # out put
    print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C")


if __name__ == '__main__':
    main()
# https://colab.research.google.com/drive/1heGyAQlCho21aIU3UvfzzkXsqX_C5xSB#scrollTo=v7LWfeXxom5S&line=26&uniqifier=1