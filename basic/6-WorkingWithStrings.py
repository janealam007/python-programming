# Python String capitalize()	Converts first character to Capital Letter
# Python String center()	Pads string with specified character
# Python String casefold()	converts to casefolded strings
# Python String count()	returns occurrences of substring in string
# Python String endswith()	Checks if String Ends with the Specified Suffix
# Python String expandtabs()	Replaces Tab character With Spaces
# Python String encode()	returns encoded string of given string
# Python String find()	Returns the index of first occurrence of substring
# Python String format()	formats string into nicer output
# Python String index()	Returns Index of Substring
# Python String isalnum()	Checks Alphanumeric Character
# Python String isalpha()	Checks if All Characters are Alphabets
# Python String isdecimal()	Checks Decimal Characters
# Python String isdigit()	Checks Digit Characters
# Python String isidentifier()	Checks for Valid Identifier
# Python String islower()	Checks if all Alphabets in a String are Lowercase
# Python String isnumeric()	Checks Numeric Characters
# Python String isprintable()	Checks Printable Character
# Python String isspace()	Checks Whitespace Characters
# Python String istitle()	Checks for Titlecased String
# Python String isupper()	returns if all characters are uppercase characters
# Python String join()	Returns a Concatenated String
# Python String ljust()	returns left-justified string of given width
# Python String rjust()	returns right-justified string of given width
# Python String lower()	returns lowercased string
# Python String upper()	returns uppercased string
# Python String swapcase()	swap uppercase characters to lowercase; vice versa
# Python String lstrip()	Removes Leading Characters
# Python String rstrip()	Removes Trailing Characters
# Python String strip()	Removes Both Leading and Trailing Characters
# Python String partition()	Returns a Tuple
# Python String maketrans()	returns a translation table
# Python String rpartition()	Returns a Tuple
# Python String translate()	returns mapped charactered string
# Python String replace()	Replaces Substring Inside
# Python String rfind()	Returns the Highest Index of Substring
# Python String rindex()	Returns Highest Index of Substring
# Python String split()	Splits String from Left
# Python String rsplit()	Splits String From Right
# Python String splitlines()	Splits String at Line Boundaries
# Python String startswith()	Checks if String Starts with the Specified String
# Python String title()	Returns a Title Cased String
# Python String zfill()	Returns a Copy of The String Padded With Zeros
# Python String format_map()	Formats the String Using Dictionary
# Python any()	Checks if any Element of an Iterable is True
# Python all()	returns true when all elements in iterable is true
# Python ascii()	Returns String Containing Printable Representation
# Python bool()	Converts a Value to Boolean
# Python bytearray()	returns array of given byte size
# Python bytes()	returns immutable bytes object
# Python compile()	Returns a Python code object
# Python complex()	Creates a Complex Number
# Python enumerate()	Returns an Enumerate Object
# Python filter()	constructs iterator from elements which are true
# Python float()	returns floating point number from number, string
# Python input()	reads and returns a line of string
# Python int()	returns integer from a number or string
# Python iter()	returns iterator for an object
# Python len()	Returns Length of an Object
# Python max()	returns largest element
# Python min()	returns smallest element
# Python map()	Applies Function and Returns a List
# Python ord()	returns Unicode code point for Unicode character
# Python reversed()	returns reversed iterator of a sequence
# Python slice()	creates a slice object specified by range()
# Python sorted()	returns sorted list from a given iterable
# Python sum()	Add items of an Iterable
# Python zip()	Returns an Iterator of Tuples

astring = "Hello world!"

# Returns Length of an Object
print(len(astring))

# Returns Index of Substring
print(astring.index("o")) 

# returns occurrences of substring in string
print(astring.count("l"))

# returns uppercased string
print(astring.upper())

# returns lowercased string
print(astring.lower())

# Splits String from Left
afewwords = astring.split(" ")
print(afewwords)