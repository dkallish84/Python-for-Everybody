# Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters “done”. Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.

user_numbers = list()

while True:
    user_input = input('Enter a number, enter done to exit: ')
    if user_input == 'done':
        break
    else:
        try:
            user_input = int(user_input)
            user_numbers.append(user_input)
        except:
            print('Please enter a number or done.')

print("Maximum:", max(user_numbers))
print("Minimum:", min(user_numbers))
