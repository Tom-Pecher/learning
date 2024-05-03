
# PYTHON: W3Schools - NumPy Tutorial
# Section 12: Array Split

# BASICS
    # The function np.array_split() splits an ndarray into a specified number of parts: 
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print("1.", np.array_split(arr, 3))

    # It will attempt to do this evenly if possible:
print("2.", np.array_split(arr, 4)) # NOTE: The function np.split() does the same thing but throws an exception if an equal division is impossible.

    # This works on higher dimensional ndarrays as well:
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
print("3.", np.array_split(arr, 3))

    # We can also change the axis of the split:
print("4.", np.array_split(arr, 3, axis=1))

    # Alternatively, we can use np.hsplit() to achieve this (the opposite of np.hstack()):
print("5.", np.hsplit(arr, 3))
