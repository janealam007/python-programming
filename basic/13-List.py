# Python Lists

# A list is a collection which is ordered and changeable. 
# In Python lists are written with square brackets.
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

thislist = ["apple", "banana", "cherry"]
print(thislist)

# Single Item print
print(thislist[1])

# Assign a value in list index
thislist[1] = "blackcurrant"
print(thislist)

# Print all list items
for x in thislist:
  print(x)

# item existancy check 
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

# List length check
print(len(thislist))

# Using the append() method to append an item:
thislist.append("orange")
print(thislist)

# remove() method removes the specified item:
thislist.remove("apple")
print(thislist)

# pop() method removes the specified index, (or the last item if index is not specified):
thislist.pop()
print(thislist)

# del keyword removes the specified index:
del thislist[0]
print(thislist)

# clear() method empties the list:
thislist.clear()
print(thislist)

# del keyword can also delete the list completely:
del thislist

# Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)