# The caret character is used in regular expressions to match “the beginning” of a line. We could change our program to only match lines where “From:” was at the beginning of the line as follows:

import re

fhand = open('/Users/dkallish/Documents/Coursera/Python for Everybody Specialization/mbox-short.txt')
# Loop through the file, line by line
for line in fhand:
    # Strip the newline character whitespace
    line = line.rstrip()
    # Search for lines that begin with 'From:' using the carat character
    if re.search('^From:', line):
        print(line)
