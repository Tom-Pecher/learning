
# PYTHON: W3Schools - Tutorial
# Section 22: Classes

# BASICS
    # Python is an object oriented programming language. We can define a class like so:
class MyClass:
  x = 5

    # We can then create instances of that class by calling its constructor:
p1 = MyClass()
print("1.", p1.x) 

class Person:
    # We can write a constructor using the __init__() method. This is called whenever a new object is created.
    # It is most commonly used to initialize the properties of an object:
  def __init__(self, name, age):
    # The self parameter is a reference to the current instance of the class:
    self.name = name 
    self.age = age

    # We can also write a __str__() method to specify how we want our object to be converted to a string:
  def __str__(self):
    return f"{self.name}({self.age})"
  
    # Instead of overriding existing functions, we can also create new ones:
  def my_func(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36) 
print("2.", p1.name)
print("3.", p1.age)
print("4.", p1)
print("5.", p1.my_func())

    # An objects attributes can be modified from outside of the class like so:
p1.age = 40
print("6.", p1.my_func())

    # We can also delete object attributes with the del keyword:
del p1.age

    # Or delete the object entirely:
del p1
