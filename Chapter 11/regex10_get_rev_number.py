# Search for lines that start with 'Details: rev=' # followed by numbers and '.'
# Then print the number if it is greater than zero

# Import the regular expressions library
import re

fhand = open('/Users/dkallish/Documents/Coursera/Python for Everybody Specialization/mbox-short.txt')
# Loop through the file line by line
for line in fhand:
    # Strip the whitespace newline character
    line = line.rstrip()
    # Use findall() and parentheses to extract the revision numbers
    x = re.findall('^Details:.*rev=([0-9.]+)', line)
    # If the resulting list length is greater than 0 print it
    if len(x) > 0:
        print(x)
