# As it turns out, we have been using objects all along in this book. Python provides us with many built-in objects. Here is some simple code where the first few lines should feel very simple and natural to you.

# Create a list, add two items, and sort them
stuff = list()
stuff.append('python')
stuff.append('Daniel')
stuff.sort()

# Print the first item in the list using differnt methods
print(stuff[0])
print(stuff.__getitem__(0))
print(list.__getitem__(stuff, 0))
