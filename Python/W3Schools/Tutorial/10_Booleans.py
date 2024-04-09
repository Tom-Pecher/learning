
# PYTHON: W3Schools - Tutorial
# Section 10: Booleans

# OPERATORS
    # Comparative operators return boolean outputs:
print("1.", 10 > 9)
print("2.", 10 >= 9)
print("3.", 10 == 9)
print("4.", 10 is 9)
print("5.", 10 < 9) 
print("6.", 10 <= 9)


# CONSTRUCTOR
    # bool(value)
        # input type: any
        # output type: bool
    # converts value to bool: all strings return True except the empty string,
    #                         all numbers return True except zero,
    #                         all collections return True except empty ones.
    # NOTE: any object whose __len__() function returns 0 will return False in bool(object).

    # The following all return True:
print("7.", bool("abc"))
print("8.", bool(123))
print("9.", bool(["apple", "cherry", "banana"]))

    # The following all return False:
print("10.", bool(False))
print("11.", bool(None))
print("12.", bool(0))
print("13.", bool(""))
print("14.", bool(()))
print("15.", bool([]))
print("16.", bool({}))

    # Many built-in functions also return booleans:
x = 200
print("17.", isinstance(x, int)) 