# Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

count = 0
total = 0

while True:
    user_input = input('Enter a number, enter done to exit: ')
    if user_input == 'done':
        break
    else:
        try:
            user_input = int(user_input)
            count = count + 1
            total = total + user_input
        except:
            print('Please enter a number or done.')

print(total, count, total/count)

# Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

total2 = 0
count2 = 0
min_num = None
max_num = None

while True:
    user_input2 = input('Enter a number, enter done to exit: ')
    if user_input2 == 'done':
        break
    else:
        try:
            user_input2 = int(user_input2)
            count2 = count2 + 1
            total2 = total2 + user_input2
            if min_num is None or min_num > user_input2:
                min_num = user_input2
            if max_num is None or max_num < user_input2:
                max_num = user_input2
        except:
            print('Please enter a number or done.')

print(total2, count2, min_num, max_num)
