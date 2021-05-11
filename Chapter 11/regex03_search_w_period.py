# The most commonly used special character is the period or full stop, which matches any character. The regular expression F..m: would match any of the strings “From:”, “Fxxm:”, “F12m:”, or “F!@m:” since the period characters in the regular expression match any character.

# Import the regular expression library
import re

fhand = open('/Users/dkallish/Documents/Coursera/Python for Everybody Specialization/mbox-short.txt')
# Loop through the file line by line
for line in fhand:
    # Strip the whitespace newline character
    line = line.rstrip()
    # Search for lines that start with 'F', followed by # 2 characters, followed by 'm:'
    if re.search('^F..m:', line):
        print(line)
