
# PYTHON: W3Schools - Tutorial
# Section 10: Booleans

# OPERATORS
    # Comparative operators return boolean outputs:
print(10 > 9)
print(10 >= 9)
print(10 == 9)
print(10 is 9)
print(10 < 9) 
print(10 <= 9)

# CONSTRUCTOR
    # bool(value)
        # input type: any
        # output type: bool
    # converts value to bool: all strings return True except the empty string,
    #                         all numbers return True except zero,
    #                         all collections return True except empty ones.
    # NOTE: any object whose __len__() function returns 0 will return False in bool(object).

    # The following all return True:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

    # The following all return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

    # Many built-in functions also return booleans:
x = 200
print(isinstance(x, int)) 