print("Welcome to the unit converter")
print()

conversions_available = [(1, "feet", "meters"),
                          (2, "meters", "feet"), 
                          (3, "celsius", "fahrenheit"),
                          (4, "fahrenheit", "celsius")]

print("Conversions available:")
print()
for conversion_number, unit_from, unit_to in conversions_available:
    print(f"{conversion_number}. {unit_from} to {unit_to}")



