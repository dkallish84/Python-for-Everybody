# Read all the lines in a file and print out anything that looks like an email address

# Import the regular expressions library
import re

fhand = open('/Users/dkallish/Documents/Coursera/Python for Everybody Specialization/mbox-short.txt')
# Loop through the file line by line
for line in fhand:
    # Remove the whitespace newline character
    line = line.rstrip()
    # Create a list of substrings that are email addresses using re.findall()
    x = re.findall('\S+@\S+', line)
    # Print only the lines where we found an email address
    if len(x) > 0:
        print(x)
