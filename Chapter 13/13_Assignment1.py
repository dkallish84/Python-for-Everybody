# Extracting Data from XML
# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1195813.xml (Sum ends with 31)

# Import the required libraries
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
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
tree = ET.fromstring(data)

# Make a list to store the comments
lst = tree.findall('comments/comment')
# Loop through the list
for item in lst:
    count += 1
    val = item.find('count').text
    comments_total += int(val)

# Print the final results
print('Count:', count)
print('Sum:', comments_total)
