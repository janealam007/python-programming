# Classes/Objects
# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Student:
   def __init__(self, name, major, gpa, is_on_probation):
       self.name = name
       self.major = major
       self.gpa = gpa
       self.is_on_probation = is_on_probation

   def on_honor_roll(self):
       if self.gpa >= 3.5:
           return True
       else:
           return False

# For Person Class Operation
p1 = Person("John", 36)

print(p1.name)
print(p1.age)


# For Student Class Operation
student = Student("Johnny Depp", "Drama", 2.0, False)

print(student.name + ' '+ student.major +' '+ str(student.gpa) +' '+ str(student.is_on_probation))
print(student.on_honor_roll())
