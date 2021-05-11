# We construct our JSON by nesting dictionaries and lists as needed. In this example, we represent a list of users where each user is a set of key-value pairs (i.e., a dictionary), so we have a list of dictionaries.

# Import the required libraries
import json

# Create a 'JSON' object to store the data
data = '''
[
    { "id" : "001",
      "x" : "2",
      "name" : "Chuck"
    },
    { "id" : "009",
      "x" : "7",
      "name" : "Brent"
    }
]'''

# Convert the JSON to a Python list
info = json.loads(data)
print('User count:', len(info))

# For each entry in the JSON object, print the attributes
for item in info:
    print('Name:', item['name'])
    print('ID:', item['id'])
    print('Attribute:', item['x'])
