
# PYTHON: W3Schools - NumPy Ufunc Tutorial
# Section 4: Rounding Decimals

import numpy as np

# BASICS
    # The ufuncs np.trunc() and np.fix() truncate decimals in a collection to the nearest integer:
arr = np.trunc([-3.1666, 3.6667])
print("1.", arr)

    # The ufunc np.around() rounds the elements of a collection to a specified number of decimal places:
arr = np.around([-3.1666, 3.6667], 3)
print("2.", arr)

    # The ufunc np.floor() takes the floor of the elements in a collection:
arr = np.floor([-3.1666, 3.6667])
print("3.", arr)

    # The ufunc np.ceil() takes the ceiling of the elements in a collection:
arr = np.ceil([-3.1666, 3.6667])
print("4.", arr)
