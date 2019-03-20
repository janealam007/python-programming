# Taking input in Python
# Developers often have a need to interact with users, either to get data 
# or to provide some sort of result. Most programs today use a dialog box 
# as a way of asking the user to provide some type of input. 
# While Python provides us with two inbuilt functions to read the input 
# from the keyboard.

# raw_input ( prompt )
# input ( prompt )

# raw_input ( ) : This function works in older version (like Python 2.x). 
# This function takes exactly what is typed from the keyboard, convert it 
# to string and then return it to the variable in which we want to store. 
# For example –

# Python program showing  
# a use of input() 

name = input("Enter your name: ") 
number1 = input("Enter First Number: ")
number2 =input("Enter Second Number: ")
total = float(number1) + float(number2)

print(name)
print(total)