# Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

emails_from = dict()

fhand = open('/Users/dkallish/Documents/Coursera/Python for Everybody Specialization/mbox-short.txt')

for line in fhand:
    words = line.split()
    # Filter unwanted lines
    if len(words) == 0 or words[0] != 'From': continue
    # words[1] is known to be the email address
    # split words[1] into the address and domain
    email_domain = words[1].split('@')
    if email_domain[1] not in emails_from:
        emails_from[email_domain[1]] = 1
    else:
        emails_from[email_domain[1]] += 1

print(emails_from)
