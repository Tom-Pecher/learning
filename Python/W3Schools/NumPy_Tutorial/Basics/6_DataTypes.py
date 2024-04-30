
# PYTHON: W3Schools - NumPy Tutorial
# Section 6: Data Types

# NUMPY DATATYPES
    #   i   -   integer
    #   b   -   boolean
    #   u   -   unsigned integer
    #   f   -   float
    #   c   -   complex float
    #   m   -   timedelta
    #   M   -   datetime
    #   O   -   object
    #   S   -   string
    #   U   -   unicode string
    #   V   -   fixed chunk of memory for other type (void)



# BASICS
    # We can check the datatype of a numpy object with its dtype attribute:
import numpy as np

arr = np.array([1, 2, 3, 4])
print("1.", arr.dtype) 

    # We can also specify a type, in this case the numbers are stored as strings:
arr = np.array([1, 2, 3, 4], dtype='S') # NOTE: If a value cannot be converted, an error will be raised.
print("2.", arr, arr.dtype)

    # We can define the size as well, in this case the elements are integers with 4 bytes:
arr = np.array([1, 2, 3, 4], dtype='i4')
print("3.", arr, arr.dtype)

    # As well as specifying datatypes at creation, we can also convert between them:
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print("4.", newarr, newarr.dtype)
