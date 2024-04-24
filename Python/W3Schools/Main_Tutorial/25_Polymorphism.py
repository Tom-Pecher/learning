
# PYTHON: W3Schools - Tutorial
# Section 25: Polymorphism

# BASICS
    # Polymorphism is when the same method has multiple different functionalities. For example, len():
x = "Hello World!"
my_tuple = ("Hello", "World", "!")
print("1.", len(x)) # Here len() returns the number of characters in a string.
print("2.", len(my_tuple)) # Here len() instead returns the number of entries in a tuple.

    # Polymorphism is most often used with class methods, in this case object.move():
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("3.", "Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("4.", "Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("5.", "Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

    # We see here that object.move() reacts differently for each object:
for x in (car1, boat1, plane1):
  x.move()

    # It is more efficient to do this with inheritance:
class Animal:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def speak(self):
    print("6.", "Yo!")

class Dog(Animal):
  pass

class Cat(Animal):
  def speak(self):
    print("7.", "Meow!")

class Snake(Animal):
  def speak(self):
    print("8.", "Ssss!")

dog1 = Dog("ALice", 3)
cat1 = Cat("Bob", 2)
snake1 = Snake("Charlie", 10)

for x in (dog1, cat1, snake1):
  print("9.", x.name)
  print("10.", x.age)
  x.speak()
