
# PYTHON: W3Schools - Tutorial
# Section 33: Try Except

# BASICS
    # The try block lets you test a block of code for errors.
    # The except block lets you handle the error.
    # The else block lets you execute code when there is no error.
    # The finally block lets you execute code, regardless of the result of the try- and except blocks:
try:
  print("1.", "try")
except:
  print("2.", "except")
else:
  print("3.", "else")
finally:
  print("4.", "finally")

    # If we want to catch different types of exceptions, we may use multiple except statements:
x = 0
try:
  print(x)
except NameError:
  print("5.", "Variable x is not defined")
except:
  print("6.", "Something else went wrong") 


# EXCEPTIONS
    # We can create custom exceptions with the raise keyword:
x = -1
if x < 0:
  #raise Exception("Sorry, no numbers below zero")
  pass

    # Based on the type of exception, we can define what kind of error to raise:
x = "hello"
if not type(x) is int:
  #raise TypeError("Only integers are allowed")
  pass
