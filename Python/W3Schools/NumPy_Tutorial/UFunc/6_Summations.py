
# PYTHON: W3Schools - NumPy Tutorial
# Section 6: Summations

import numpy as np

# BASICS
    # The ufunc np.sum() performs a summation of a list of collections:
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([7, 8, 9])
print("1.", np.sum([arr1, arr2, arr3]))

    # We can fix the sum to a certain direction (axis):
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([7, 8, 9])
print("2.", np.sum([arr1, arr2, arr3], axis=0))
print("3.", np.sum([arr1, arr2, arr3], axis=1))

    # Instead of a regular sum, we can also accumulate the sum at each step using np.cumsum():
arr = np.array([1, 4, 7])
print("4.", np.cumsum(arr))
