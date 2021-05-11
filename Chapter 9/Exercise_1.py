# Exercise 1: Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.

word_dictionary = dict()
fhand = open("/Users/dkallish/Documents/Coursera/Python for Everybody Specialization/words.txt")

for line in fhand:
    temp_words = line.split()
    for word in temp_words:
        word_dictionary[word] = word
print(word_dictionary)
