
# PYTHON: W3Schools - Main Tutorial
# Section 20: Lambda

# BASICS
    # Lambda functions are small, anonymous functions:
x = lambda a : a + 10
print("1.", x(5))

    # One use case of lambda functions is generating a set of functions:
def my_func(n):
  return lambda a : a * n
my_doubler = my_func(2)
my_tripler = my_func(3)
print("2.", my_doubler(11))
print("3.", my_tripler(11))
