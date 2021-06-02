# Here is a simple application that parses some XML and extracts some data elements from the XML

# Import the required library
import xml.etree.ElementTree as ET

# Create an object to hold the xml
data = '''
<person>
    <name>Chuck</name>
    <phone type="intl">+1 743 303 4456</phone>
    <email hide="yes" />
</person>'''

# Format the data
tree = ET.fromstring(data)
# Print the name and email hide attributes
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
