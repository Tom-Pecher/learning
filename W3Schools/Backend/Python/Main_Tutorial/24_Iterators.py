
# PYTHON: W3Schools - Main Tutorial
# Section 24: Iterators

# BASICS
    # An iterator is an object that contains a countable number of values which you can traverse through.
    # Specifically it is an object that implements the methods __iter__() and __next__():
my_tuple = ("apple", "banana", "cherry")
my_iter = iter(my_tuple)

print("1.", next(my_iter))
print("2.", next(my_iter))
print("3.", next(my_iter))

    # This can be applied to any iterable object, even strings:
my_iter = iter("banana")

print("4.", next(my_iter))
print("5.", next(my_iter))
print("6.", next(my_iter))

    # This is what happens when we use a for loop to iterate through a collection:
for x in my_tuple:
  print("7.", x)

# CUSTOM ITERATORS
    # We can use classes to implement our own iterators
class MyNumbers:
  # Initializes iterator but must always return the iterator object itself.
  def __iter__(self):
    self.a = 1
    return self
  # Return the next item in the sequence:
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else: # Stop iterating at 20
      raise StopIteration

my_iter = iter(MyNumbers())
for x in my_iter:
  print("8.", x)
