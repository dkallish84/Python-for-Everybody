# Exercise 3: Create a function named count, that accepts string and the letter as arguments, in order to count the number of times a character is repeated in a given string.

def count(the_string, letter):
    count = 0
    for char in the_string:
        if char == letter:
            count = count + 1
    return count

str = input('Enter a string of characters: ')
letter = input('Enter the letter you want to count: ')

letter_count = count(str, letter)
print('Count of', letter, 'is', letter_count)
