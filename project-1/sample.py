import random

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Generate a list of 10 random integers representing temperatures in Celsius
tempslist = [random.randint(-5, 35) for _ in range(5)]

# Convert each Celsius temperature to Fahrenheit and print
for item in tempslist:
    fahrenheit = celsius_to_fahrenheit(item)
    print(f"{item} Celsius = {fahrenheit:.2f} Fahrenheit")

