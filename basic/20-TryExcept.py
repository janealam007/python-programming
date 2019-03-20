# Python Try Except
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

#The try block will generate a NameError, because x is not defined:
# x = 'Mr John'
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
finally:
  print("The 'try except' is finished")