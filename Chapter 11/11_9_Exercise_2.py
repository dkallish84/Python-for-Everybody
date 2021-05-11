# Exercise 2: Write a program to look for lines in mbox.txt and mbox-short.txt of the form:
# New Revision: 39772
# Extract the number from each of the lines using a regular expression and the findall() method. Compute the average of the numbers and print out the average as an integer.

# Import the regular expressions library
import re
count = 0
total = 0

fhand = open('/Users/dkallish/Documents/Coursera/Python for Everybody Specialization/mbox-short.txt')
# Loop through the file line by line
for line in fhand:
    # Remove the whitespace newline character
    line = line.rstrip()
    # Use finall() for the RegEx
    # x = re.findall('^New .*: ([0-9][0-9][0-9][0-9][0-9])', line)
    x = re.findall('^New .*: ([0-9]*)', line)
    # If the line length is greater than 0, add one to the count
    if len(x) > 0:
        str1 = ''.join(str(s) for s in x)
        total = total + int(str1)
        count += 1

print('The average is:', int(total/count))
