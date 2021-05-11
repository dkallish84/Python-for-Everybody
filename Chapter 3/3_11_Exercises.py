# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

hours = input('Enter hours: ')
hrs = int(hours)
rate = input('Enter rate: ')
r = float(rate)

if hrs > 40 :
    print('Pay: ', (40 * r) + ((hrs - 40) * (r * 1.5)))
else :
    print('Pay: ', (hrs * r))

# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program.

hours = input('Enter hours: ')
try :
    hrs = float(hours)
    rate = input('Enter rate: ')
    try :
        r = float(rate)
        if hrs > 40 :
            print('Pay: ', (40 * r) + ((hrs - 40) * (r * 1.5)))
        else :
            print('Pay: ', (hrs * r))
    except :
        print('Please enter a number for your rate.')
except :
    print('Please enter a number for your hours.')

# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message.

score = input('Enter score: ')
try :
    score = float(score)
    if score > 1.0 :
        print('Please enter a value between 0.0 and 1.0')
    elif score >= 0.9 :
        print('A')
    elif score >= 0.8 :
        print('B')
    elif score >= 0.7 :
        print('C')
    elif score >= 0.6 :
        print('D')
    elif score >= 0.0 :
        print('F')
    else :
        print('Please enter a value between 0.0 and 1.0')
except :
    print('Please enter a number between 0.0 and 1.0')
