
# PYTHON: W3Schools - Tutorial
# Section 27: Modules


# BASICS
    # Modules are files that we can access to add additional functionality to our code. These can be built in or custom.
    # We can import Python modules using the input keyword:
import random
print("1.", random.randint(0, 10))

    # If the path to the module is not stored, we can use the from keyword to specify it:
from example_files import mymodule1
print("2.", mymodule1.person1["age"])
print("3.", mymodule1.greeting("Alice"))

    # Some modules are very large so to import specific functionality, we write:
from example_files.mymodule2 import farewell1
print("4.", farewell1("Bob")) # NOTE: we no longer have to specify the module name here

    # We can import all functionality with an asterisk:
from example_files.mymodule2 import *
print("5.", farewell2("Charlie"))

    # We can alias modules using the as keyword:
import math as m
print("6.", m.pi)
