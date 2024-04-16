
# PYTHON: W3Schools - Tutorial
# Section 26: Scope


# BASICS
    # Variables can only be accessed in the block of code they were defined in:
                    # Nothing in scope
x = "value 1"       # x in scope
def myfunc():       # 
  y = "value 2"     # x and y in scope
myfunc()            # x in scope

    # The same variable can have different values in different scopes:
x = "apple"
print("1.", x)            # prints "apple"
def myfunc():
  x = "orange"
  return x
print("2.", myfunc())     # prints "orange"
print("3.", x)            # prints "apple"

    # One can assign a global scope to a local variable:
if True:
  global a
  a = "fantastic"
myfunc()
print("4.", "Python is " + a) 

    # Or override the value of existing global variables:
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("5.", "Python is " + x) 
