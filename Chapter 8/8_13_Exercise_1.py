# Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

def chop(str):
    del str[0]
    del str[len(str) - 1]

def middle(str):
    return str[1:len(str) - 1]

string_list = ['first', 'second', 'third', 'last']
print("Pre-chop:", string_list)
chop(string_list)
print("Post-chop:", string_list)

string_list2 = ['first', 'second', 'third', 'last']
print("Pre-middle:", string_list2)
string_list3 = middle(string_list2)
print("Post-middle:", string_list3)
