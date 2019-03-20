# File Open
# File handling is an important part of any web application.
# Python has several functions for creating, reading, updating, and deleting files.

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

import os

f = open("demofile.txt", "r")

for employee in f.readlines():
   print(employee)

print(f.readlines())

f.close()

f = open("demofile.txt", "a")
f.write("Now the file has one more line! \n ")


# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:

fileDelete = input('Do want to delete file? Y/N :')

if fileDelete == 'Y':
    if os.path.exists("demofile.txt"):
        os.remove("demofile.txt")
        print('File Deleted Successfully.')
    else:
        print("The file does not exist")    
else:
    print('File Not Deleted.')