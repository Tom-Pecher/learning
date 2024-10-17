
# PYTHON: W3Schools - NumPy Ufunc Tutorial
# Section 7: Products

import numpy as np

# BASICS
    # The ufunc np.prod() performs a product of a list of collections:
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([7, 8, 9])
print("1.", np.prod([arr1, arr2, arr3]))

    # We can fix the product to a certain direction (axis):
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([7, 8, 9])
print("2.", np.prod([arr1, arr2, arr3], axis=0))
print("3.", np.prod([arr1, arr2, arr3], axis=1))

    # Instead of a regular product, we can also accumulate the multiplication at each step using np.cumprod():
arr = np.array([1, 4, 7])
print("4.", np.cumprod(arr))
