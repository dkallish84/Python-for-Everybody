# Search for lines that start with 'X' followed by any # non whitespace characters and ':' followed by a space # and any number. The number can include a decimal.
# Then print the number if it is greater than zero.

# Import the regular expressions library
import re

fhand = open('/Users/dkallish/Documents/Coursera/Python for Everybody Specialization/mbox-short.txt')

# Loop through the file line by line
for line in fhand:
    # Remove the whitespace newline character
    line = line.rstrip()
    # Adding parentheses to findall() extracts the matched value as a list
    x = re.findall('^X\S*: ([0-9.]+)', line)
    # Print the line if the length is greater than 0
    if len(x) > 0:
        print(x)
