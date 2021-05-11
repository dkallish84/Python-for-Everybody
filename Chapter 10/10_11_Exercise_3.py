# Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z.

import string

# Create empty dictionary and list to store values later
chars_dict = dict()
char_list = list()

# Prompt for the filename
fname = input('Enter file name: ')
# Try/except to catch bad files
try:
    fhand = open(fname)
except:
    print('Unable to open file', fname)
    exit()

# Iterate through the file
for line in fhand:
    # Clean up punctuation, numbers, make lowercase, split into words
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.lower()
    line = line.split()
    # Iterate through each line
    for words in line:
        # Add the words to a list
        word = list(words)
        # Iterate through each word and get the letters
        for char in word:
            chars_dict[char] = chars_dict.get(char, 0) + 1

# Use tuples to create a list of the count and values
for char, count in chars_dict.items():
    char_list.append((count, char))
# Sort the list of characters in descending order
char_list.sort(reverse=True)

# Print each key, value pair
for k, v in char_list:
    print(v, k)
