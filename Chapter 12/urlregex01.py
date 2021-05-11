# Search for link values within URL input

# Import the urllib, regular expression, and SSL libraries
import urllib.request, urllib.parse, urllib.error
import re
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Prompt the user for a URL
url = input('Enter a url: ')
# Create a variable to store the remote connection information
html = urllib.request.urlopen(url, context=ctx).read()
# Create a list of the RegEx matching items
# Extract the URL http(s) using non-greedy RegEx
links = re.findall(b'(href="http[s]?://.*?)"', html)
# Decode and print each link that was found on the supplied page
for link in links:
    print(link.decode())
