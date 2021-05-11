# In order to avoid running out of memory, we retrieve the data in blocks (or buffers) and then write each block to your disk before retrieving the next block.

# Import the required urllib library methods
import urllib.request, urllib.parse, urllib.error

# Create a variable to store the remote connection information
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
# Create a file and a variable to store the file size
fhand = open('cover3.jpg', 'wb')
size = 0
# Use a loop to control the buffer
while True:
    # Limit the read size to 10,000 as a buffer
    info = img.read(10000)
    # When the length of the buffer is 0, end the loop
    if len(info) < 1: break
    # Keep a tally of the size of the file
    size = size + len(info)
    # Write the buffer to the file
    fhand.write(info)

# Print the number of characters copied and close the connection to the local file
print(size, 'characters copied.')
fhand.close()
