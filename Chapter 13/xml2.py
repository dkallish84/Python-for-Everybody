# Often the XML has multiple nodes and we need to write a loop to process all of the nodes. In the following program, we loop through all of the user nodes

# Import the required libraries
import xml.etree.ElementTree as ET

# Create an object to store the data
input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

# Convert the object into xml
stuff = ET.fromstring(input)
# Get a list of the users
lst = stuff.findall('users/user')
print('User count:', len(lst))

# Print each attribute from the list
for item in lst:
    print('Name:', item.find('name').text)
    print('ID:', item.find('id').text)
    print('Attribute:', item.get('x'))
