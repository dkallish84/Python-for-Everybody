# Search for lines that start with 'X' followed by any non
# whitespace characters and ':' followed by a space and any number.
# The number can include a decimal.

# Import the regular expressions library
import re

fhand = open('/Users/dkallish/Documents/Coursera/Python for Everybody Specialization/mbox-short.txt')
# Loop through the file line by line
for line in fhand:
    # Remove the whitespace newline character
    line = line.rstrip()
    # Search for the specified lines
    if re.search('^X\S*: [0-9.]+', line):
        print(line)
