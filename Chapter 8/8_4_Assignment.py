# Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.

fname = input("Enter file name: ")
fh = open(fname)
temp_list = list()
words = list()

# Loop through the file and assign each word to the list
for line in fh:
    temp_list = line.split()
    for word in temp_list:
        if word not in words:
            words.append(word)

words.sort()

# Print the result
print(words)
