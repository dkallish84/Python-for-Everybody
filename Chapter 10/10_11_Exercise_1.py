# Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.
# After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

emails_from = dict()
max_num = None
max_email_addr = ''

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

for key in emails_from:
    if max_num is None or max_num < emails_from[key]:
        max_email_addr, max_num = key, emails_from[key]

print(max_email_addr, max_num)
