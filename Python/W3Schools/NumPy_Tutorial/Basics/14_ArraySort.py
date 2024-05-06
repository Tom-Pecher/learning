
# PYTHON: W3Schools - NumPy Tutorial
# Section 14: Array Sort

# BASICS
    # We can use numpy to sort ndarrays:
import numpy as np

arr = np.array([3, 2, 0, 1])
print("1.", np.sort(arr)) # NOTE: np.sort() returns a copy and leaves the original intact.

    # This works on strings as well:
arr = np.array(['banana', 'cherry', 'apple'])
print("2.", np.sort(arr))

    # And booleans:
arr = np.array([True, False, True])
print("3.", np.sort(arr))

    # Applying to higher dimensional ndarrays will sort all 1D ndarrays within:
arr = np.array([[3, 2, 4], [5, 0, 1]])
print("4.", np.sort(arr))
