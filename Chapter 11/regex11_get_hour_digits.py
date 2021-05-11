# Search for lines that start with 'From ' followed by a two digit number between 00 and 99 followed by ':'
# Then print the number if it is greater than zero

# Import the regular expressions library
import re

fhand = open('/Users/dkallish/Documents/Coursera/Python for Everybody Specialization/mbox-short.txt')
# Loop through the file line by line
for line in fhand:
    # Remove the whitespace newline character
    line = line.rstrip()
    # Extract the hour the message was sent and add it to a list
    x = re.findall('^From .* ([0-9][0-9]):', line)
    # If the list length is greater than 0, print it
    if len(x) > 0:
        print(x)
