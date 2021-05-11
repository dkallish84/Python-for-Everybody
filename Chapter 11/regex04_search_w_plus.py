# This is particularly powerful when combined with the ability to indicate that a character can be repeated any number of times using the * or + characters in your regular expression. We can further narrow down the lines that we match using a repeated wild card character.
# The search string ˆFrom:.+@ will successfully match lines that start with “From:”, followed by one or more characters (.+), followed by an at-sign.

# Import the regular experessions library
import re

fhand = open('/Users/dkallish/Documents/Coursera/Python for Everybody Specialization/mbox-short.txt')
# Loop through the file line by line
for line in fhand:
    # Remove the whitespace newline character
    line = line.rstrip()
    # Search for lines that start with From and have an at sign
    if re.search('^From:.+@', line):
        print(line)
