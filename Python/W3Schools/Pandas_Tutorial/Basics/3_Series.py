
# PYTHON: W3Schools - Pandas Tutorial
# Section 3: Series

import pandas as pd

# BASICS
    # A pandas series is like a column in a table: a 1-dimensional array capable of holding any datatype:
a = [1, 7, 2]
myvar = pd.Series(a)
print("1.", myvar)

    # If we do not specify labels, we may index the series like any other array:
print("2.", myvar[1])

    # To add labels, we simple supply them as an additional collection:
a = [1, 7, 2]
index = ["x", "y", "z"]
myvar = pd.Series(a, index)
print("3.", myvar)

    # Now it is essentially a dictionary and we can access the items through the labels:
print("4.", myvar["y"])
