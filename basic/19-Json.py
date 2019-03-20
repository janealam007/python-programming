# Json In Python 
# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

# When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

# Python	JSON
# dict	Object
# list	Array
# tuple	Array
# str	String
# int	Number
# float	Number
# True	true
# False	false
# None	null

import json
# If you have a JSON string, you can parse it by using the json.loads() method.
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])



# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
# a Python object (dict):
object = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(object)

# the result is a JSON string:
print(y)