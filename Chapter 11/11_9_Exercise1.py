# Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter a regular expression and count the number of lines that matched the regular expression:
# $ python grep.py
# Enter a regular expression: ^Author
# mbox.txt had 1798 lines that matched ^Author
# $ python grep.py
# Enter a regular expression: ^X-
# mbox.txt had 14368 lines that matched ^X-
# $ python grep.py
# Enter a regular expression: java$
# mbox.txt had 4175 lines that matched java$

# Import the regular expressions library
import re
count = 0

# Prompt the user for their 'grep' command:
user_in = input('Enter a regular expression: ')

fhand = open('/Users/dkallish/Documents/Coursera/Python for Everybody Specialization/mbox.txt')
# Loop through the file line by line
for line in fhand:
    # Remove the whitespace newline character
    line = line.rstrip()
    # Use findall() for the RegEx
    x = re.findall(user_in, line)
    # If the list length is greater than 0, increase the counter
    if len(x) > 0:
        count += 1

# Print the final result
print('mxbox.txt had', count, 'lines that matched', user_in)
