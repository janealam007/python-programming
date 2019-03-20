# Function in Python
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# Creating a Function
# In Python a function is defined using the 'def' keyword:

def my_function():
  print("Hello from a function")

def raise_to_power(base_num, pow_numbe):
   result = 1
   for index in range(pow_numbe):
       result = result * base_num
   return result

my_function()

# Integer type cast with "int(value)"
base_num = int(input('Enter a base number: '))
pow_numbe = int(input('Enter a powe number: '))

# Function with param
print(raise_to_power(base_num,pow_numbe))




