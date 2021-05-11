# If we want to extract data from a string in Python we can use the findall() method to extract all of the substrings which match a regular expression. We don’t want to write code for each of the types of lines, splitting and slicing differently for each line. This following program uses findall() to find the lines with email addresses in them and extract one or more addresses from each of those lines.
# We are using a two-character sequence that matches a non-whitespace character (\S).

# Import the regular expressions library
import re
# String to search with findall()
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
# Look for substrings that include '@' and put them in a list
lst = re.findall('\S+@\S+', s)

print(lst)
