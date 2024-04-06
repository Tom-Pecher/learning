
# PYTHON: W3Schools - Tutorial
# Section 5: Variables

# RULES FOR NAMING VARIABLES
    # A variable name must start with a letter or the underscore character
    # A variable name cannot start with a number
    # A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    # Variable names are case-sensitive (age, Age and AGE are three different variables)
    # A variable name cannot be any of the Python keywords.

# NAMING CONVENTIONS
    # The general convention for Python naming is SNAKE CASE:
my_variable_name = "John"

    # Alteratives include CAMEL CASE:
myVariableName = "John"

    # And PASCAL CASE:
MyVariableName = "John"

    # Constant values are designated with UPPER CASE:
MY_CONSTANT = "3.14159265"

# VALUE ASSIGNMENT
    # Variable's values are assigned using the = operator:
x = "Orange"

    # Multiple values can be assigned at once:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

    # Or single values can be assigned to multiple variables:
x = y = z = "Orange"
print(x)
print(y)
print(z)

    # Similarly, we can unpack collections, using _ as a placeholder
fruits = ["apple", "banana", "cherry"]
x, _, y = fruits
print(x)
print(y)

# OUTPUT VARIABLES
    # We can use print() to output a variable's value:
x = "Python is awesome"
print(x)

    # Or multiple values:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

    # Alternatively, we can concatenate the variables into one and print:
x = "Python"
y = "is"
z = "awesome"
print(x + y + z)
# NOTE: This only works if the + operator is defined for the two variable types
# This is because some functions/operators work differently on different variable types

    # For integers rather than strings, + is a mathematical operator:
x = 5
y = 10
print(x + y)

# SCOPE BASICS
    # Variables can only be accessed in the block of code they were defined in:
                    # Nothing in scope
x = "value 1"       # x in scope
def myfunc():       # 
  y = "value 2"     # x and y in scope
myfunc()            # x in scope

    # The same variable can have different values in different scopes:
x = "apple"
print(x)            # prints "apple"
def myfunc():
  x = "orange"
  return x
print(myfunc())     # prints "orange"
print(x)            # prints "apple"

    # One can assign a global scope to a local variable:
if True:
  global a
  a = "fantastic"
myfunc()
print("Python is " + a) 

    # Or override the value of existing global variables:
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x) 
