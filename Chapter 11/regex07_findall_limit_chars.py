# Read all the lines in a file and print out anything that looks like an email address, filtering characters that are not a-zA-Z0-9 before and after the @ symbol.
# NOTE that we switched from + to * to indicate zero or more non-blank characters since [a-zA-Z0-9] is already one non-blank character.

# Import the regular expressions library
import re

fhand = open('/Users/dkallish/Documents/Coursera/Python for Everybody Specialization/mbox-short.txt')
# Loop through the file line by line
for line in fhand:
    # Remove the whitespace newline character
    line = line.rstrip()
    # Create a list of substrings that are email addresses using re.findall()
    # Ensure the characters before and after the @ are non-special
    lst = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    # Print only the lines were an email address was found
    if len(lst) > 0:
        print(lst)
