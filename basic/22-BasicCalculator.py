# Basic arithmetic operation with two input value and a operator. 
# Here we use four operator(+, -, *, /)

num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
op = input("Enter operator: ")

if op == "+":
   print(num1+num2)
elif op == "-":
   print(num1-num2)
elif op == "*":
   print(num1*num2)
elif op == "/":
   print(num1/num2)