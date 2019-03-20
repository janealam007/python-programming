#  A tuple is a collection which is ordered and unchangeable.
#  In Python tuples are written with round brackets.
#  Tuples are unchangeable, so you cannot remove items from it,
#  but you can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
print(thistuple)

for x in thistuple:
  print(x)

  thistuple[1] = "blackcurrant"
# The values will remain the same:
print(thistuple)