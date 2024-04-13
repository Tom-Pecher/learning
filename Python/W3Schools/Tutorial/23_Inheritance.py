
# PYTHON: W3Schools - Tutorial
# Section 23: Inheritance

# BASICS
    # We can use inheritance to share functionality between classes:
    # Parent class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print("1.", self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

    # Child class
class Student(Person): # We specify parent classes in the definition like so.
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname) # Same as Person.__init__(self, fname, lname)
    self.graduationyear = year
  def welcome(self):
    print("2.", "Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()