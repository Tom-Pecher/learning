
# PYTHON: W3Schools - NumPy Tutorial
# Section 9: Array Reshape

import numpy as np

# BASICS
    # We can change the dimensions of an array by calling np.ndarray.reshape():
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)  # NOTE: If it is not possible to reshape the array (dimensions are uneven), an error will be thrown.
print("1.", newarr, newarr.shape)

    # Note that reshape returns a view and not a separate ndarray:
print("2.", arr.reshape(2, 6).base)


# UNKNOWN DIMENSIONS
    # Using -1, we can designate a dimension as unspecified and numpy will attempt to reshape the ndarray regardless:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, -1, 2)
print("3.", newarr)

    # With this, we can fully flatten an ndarray without explicitly using the np.ndarray.flatten() function:
arr = np.array([1, 2, 3], ndmin=5)
print("4.", arr, arr.reshape(-1))
