# Exercise 4: Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dic- tionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.

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
        max_num = emails_from[key]
        max_email_addr = key

print(max_email_addr, max_num)
