
# PYTHON: W3Schools - Tutorial
# Section 20: Lambda

# BASICS
    # Lambda functions are small, anonymous functions:
x = lambda a : a + 10
print("1.", x(5))

    # One use case of lambda functions is generating a set of functions:
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print("2.", mydoubler(11))
print("3.", mytripler(11))
