from utils import square, is_even, celsius_to_fahrenheit


number = float(input("Enter a number: "))

print("Square:", square(number))
print("Even:" if is_even(number) else "Odd:", is_even(number))
print("Fahrenheit:", celsius_to_fahrenheit(number))
