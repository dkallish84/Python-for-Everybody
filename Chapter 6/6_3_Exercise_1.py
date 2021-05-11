# Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.

word = 'Delta'
count = -1
length = (len(word) * -1) - 1

while count > length:
    print(word[count])
    count = count - 1
