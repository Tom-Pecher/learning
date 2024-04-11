
# PYTHON: W3Schools - Tutorial
# Section 19: Functions

# BASICS
    # A function is a block of code that runs wherever it is called:
def my_function1():  # defines the function
  print("1.", "Hello from a function")
my_function1()       # calls the function

    # We can supply parameters to a function like so:
def my_function2(fname):
  print("2.", fname + " Refsnes")
my_function2("Emil")
my_function2("Tobias")
my_function2("Linus") 


# ARBITRARY ARGUMENTS
    # A function must be supplied the exact number of parameters specified.
    # We can set a function to accept an arbitrary number of arguements with a single *:
def my_function3(*kids):
  print("3.", "The youngest child is " + kids[2])
my_function3("Emil", "Tobias", "Linus")

    # Or an arbitrary number of keyword arguments with a double *:
def my_function4(**kid):
  print("4.", "His last name is " + kid["lname"])
my_function4(fname = "Tobias", lname = "Refsnes")

    # We can set the default values of parameters like so:
def my_function5(country="Norway"):
  print("5.", "I am from " + country)
my_function5("Sweden")
my_function5()


# RETURNING VALUES
    # We can return values to be used outside of the function using the return statement:
def my_function6(x):
  return 5 * x
print("6.", my_function6(3))
print("7.", my_function6(5))
print("8.", my_function6(9)) 


# CONSTRAINING PARAMETER TYPES
    # All parameters before the / must be positional (regular) arguments and all parameters after the * must be keyword 
    # arguments. Doing otherwise will throw an error:
def my_function(a, b, /, *, c, d):
  print("9.", a + b + c + d)
my_function(5, 6, c = 7, d = 8)



# RECURSION
    # Python also accepts recursion, which is where a function calls itself:
def tri_recursion(k):
  if k > 0:
    result = k + tri_recursion(k - 1)
    print("10.", result)
  else:
    result = 0
  return result

print("11.", "Recursion Example Results")
tri_recursion(6)
