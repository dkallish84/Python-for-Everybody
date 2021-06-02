# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
# To complete this assignment, you should use this API endpoint that has a static subset of the Google Data: http://py4e-data.dr-chuck.net/json?
# To call the API, you need to include a key= parameter and provide the address that you are requesting as the address= parameter that is properly URL encoded using the urllib.parse.urlencode() function
# Please run your program to find the place_id for this location: Universidad de Los Andes Colombia

# Import the required libraries
import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificates
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Store the API key and service URL
api_key = 42
service_url = 'http://py4e-data.dr-chuck.net/json?'

# Prompt the user for the location
location = input('Enter location: ')
if len(location) < 1: exit()

# Create a dictionary to store the parameters for the request
params = dict()
# Populate the location and API key values
params['address'] = location
if api_key is not False:
    params['key'] = api_key
# Encode the URL with the parameters
url = service_url + urllib.parse.urlencode(params)

print('Retrieving', url)
# Create a handle for the retrieved URL
uhand = urllib.request.urlopen(url, context=ctx)
# Decode the returned data
data = uhand.read().decode()
print('Retrieved', len(data), 'characters')

# Catch any exceptions with bad JSON data
try:
    js = json.loads(data)
except:
    js = None

# Account for a bad status
if not js or 'status' not in js or js['status'] != 'OK':
    print('Failed to retrieve data')
    print(data)
    exit()

# Pretty pring the json
# print(json.dumps(js, indent=4))
# Get the place_id value
place_id = js['results'][0]['place_id']
print('Place id', place_id)
