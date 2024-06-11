
# PYTHON: W3Schools - NumPy Tutorial
# Section 2: Ufunc Creation

import numpy as np

# We can create custom ufuncs using the frompyfunc() method.
# The frompyfunc() method takes the following arguments:
#   function  - the name of the function.
#   inputs    - the number of input arguments (arrays).
#   outputs   - the number of output arrays.


# BASICS
    # Here we create a standard custom addition function and create a vectorized ufunc from it:
def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)
print("1.", myadd([1, 2, 3, 4], [5, 6, 7, 8]))

    # We can check if a function is a ufunc using the builtin type() function:
print("2.", type(myadd))

    # If it is not, it will return some other type:
print("3.", type(np.concatenate))

    # We can test if a function is a ufunc like so:
if type(np.add) == np.ufunc:
  print("4.", 'add is ufunc')
else:
  print("5.", 'add is not ufunc')
