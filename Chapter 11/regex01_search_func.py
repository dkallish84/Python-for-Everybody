# The simplest use of the regular expression library is the search() function. The following program demonstrates a trivial use of the search function:

# Search for lines that contain 'From'
import re

fhand = open('/Users/dkallish/Documents/Coursera/Python for Everybody Specialization/mbox-short.txt')
# Loop through the file, line by line
for line in fhand:
    # Remove the newline character whitespace
    line = line.rstrip()

    # Use RegEx search() to locate lines with 'From'
    if re.search('From:', line):
        print(line)
