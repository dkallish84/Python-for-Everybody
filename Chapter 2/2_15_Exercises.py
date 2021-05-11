# Exercise 2: Write a program that asks the user for their name and greets them
user_input = input('Enter your name: ')
print('Hello', user_input)

# Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
inp = input('Enter hours: ')
hours = int(inp)
inp = input('Enter Rate: ')
rate = float(inp)
print('Pay:', (hours * rate))

# Exercise 5: Write a program which prompts the user for a Celsius tem- perature, convert the temperature to Fahrenheit, and print out the converted temperature.
# F = C * (9/5) + 32
inp = input('Enter the temperature in Celcius: ')
fahrenheit_temp = float(inp) * (9/5) + 32
print('The temperature in Fahrenheit is', fahrenheit_temp)
