# Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

days = dict()

fhand = open("/Users/dkallish/Documents/Coursera/Python for Everybody Specialization/mbox-short.txt")
for line in fhand:
    words = line.split()
    # Filter unwanted lines
    if len(words) == 0 or words[0] != 'From': continue
    # words[2] is known to be the day of the week abbreviation
    if words[2] not in days:
        days[words[2]] = 1
    else:
        days[words[2]] += 1

print(days)
