# Extracting Data from JSON
# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file.
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1195814.json (Sum ends with 83)

# Import the required libraries
import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Store the count, and total number of comments
count = 0
comments_total = 0

# Ignore SSL certificates
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Prompt the user for the URL
url = input('Enter URL: ')
# Make sure the User entered something
if len(url) < 1:
    print('Please enter a full URL')
    exit()
# Open the remote file
uhand = urllib.request.urlopen(url, context=ctx)
# Convert url handle into Python readable data
data = uhand.read().decode()
# Print the number of characters
print('Retrieved', len(data), 'characters')
# Convert the data to json
js = json.loads(data)

# Loop through the comments
for item in js['comments']:
    # Calculate the count and total number of comments
    count += 1
    comments_total = comments_total + int(item['count'])

# Print the final results
print('Count:', count)
print('Sum:', comments_total)
