import re
total = 0

fhand = open('regex_sum_1195809.txt')
# Loop through the file line by line
for line in fhand:
    # Remove the whitespace newline character
    line = line.rstrip()
    # Use findall() to get the numbers as a list
    lst = re.findall('([0-9]+)', line)
    if len(lst) > 0:
        # Handle lines with more than one list entry
        if len(lst) > 1:
            # Loop through the list and add it to the total
            for i in lst:
                total += int(i)
        else:
            # Convert to string then to int and add to the total
            str1 = ''.join(str(i) for i in lst)
            total += int(str1)
print('The total is:', total)
