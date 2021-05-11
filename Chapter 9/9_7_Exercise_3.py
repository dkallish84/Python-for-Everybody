# Exercise 3: Write a program to read through a mail log, build a his- togram using a dictionary to count how many messages have come from each email address, and print the dictionary.

emails_from = dict()
fhand = open('/Users/dkallish/Documents/Coursera/Python for Everybody Specialization/mbox-short.txt')

for line in fhand:
    words = line.split()
    # Filter unwanted lines
    if len(words) == 0 or words[0] != 'From': continue
    # words[1] is known to be the email address
    if words[1] not in emails_from:
        emails_from[words[1]] = 1
    else:
        emails_from[words[1]] += 1

print(emails_from)
