# Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.

count = 0

file_name = input("Enter a filename: ")
try:
    fhand = open(file_name)
except:
    print('Unable to open the specified file.')
    quit()

for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] != 'From':
        continue
    print(words[1])
    count = count + 1

print('There were', count, 'lines in the file with From as the first word')
