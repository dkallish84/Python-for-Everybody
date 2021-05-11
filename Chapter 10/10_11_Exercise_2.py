# Exercise 2: This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

hr_count = dict()

fhand = open('/Users/dkallish/Documents/Coursera/Python for Everybody Specialization/mbox-short.txt')

for line in fhand:
    words = line.split()
    # Filter unwanted lines
    if len(words) == 0 or words[0] != 'From': continue
    hrs = words[5].split(':')

    # Put the hour in the list and count it
    if hrs[0] not in hr_count:
        hr_count[hrs[0]] = 1
    else:
        hr_count[hrs[0]] += 1

# Use .items() to create tuples from the dictionary
hr_tuples = list(hr_count.items())
# Sort the list of tuples
hr_tuples.sort()
# Print the list using key value pairs
for k, v in hr_tuples:
    print(k, v)
