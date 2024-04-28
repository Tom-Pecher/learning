
# PYTHON: W3Schools - Main Tutorial
# Section 29: Math


# BUILTIN FUNCTIONS
    # min(collection)
        # input type: collection
        # output type: value
    # returns the smallest value in the collection

    # max(collection)
        # input type: collection
        # output type: value
    # returns the largest value in the collection
t = (5, 10, 25)
print("1.", min(t), max(t))

    # abs(value)
        # input type: value
        # output type: value
    # returns the absolute value of the specified number
print("2.", abs(-7.25))

    # pow(value, value)
        # input type: value, value
        # output type: value
    # returns the first value to the power of the second value
print("3.", pow(4, 3))

    # The shorthand is **:
print("4.", 49**0.5)


# MATH MODULE
    # For additional mathematical functionality, we can import the math module:
import math

    # The math.sqrt() function returns the square root of the specified value:
print("5.", math.sqrt(64))

    # The functions math.floor() and math.ceil() return the floor and ceiling of the specified float:
x = 1.4
print("6.", math.floor(x), math.ceil(x))

    # The math module also gives us access to mathematical constants:
print("7.", math.pi)
