# Python Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:
x = Person("Johnny", "Depp")
x.printname()

# Now the Student class has the same properties and methods as the Person class.
class Student(Person):
    pass

# Use the Student class to create an object, and then execute the printname method:
x = Student("Kevin", "Feige")
x.printname()