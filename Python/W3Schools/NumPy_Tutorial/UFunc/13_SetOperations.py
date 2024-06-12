
# PYTHON: W3Schools - NumPy Ufunc Tutorial
# Section 13: Set Operations

import numpy as np

# BASICS
    # The ufunc np.unique() returns an ndarray of unique elements in a collection:
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
print("1.", np.unique(arr))

    # To find the unique elements of two ndarrays, we can use np.union1d():
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
print("2.", np.union1d(arr1, arr2))

    # To find the shared elements of two ndarrays, we can use np.intersect1d():
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
print("3.", np.intersect1d(arr1, arr2, assume_unique=True)) # NOTE: We can set assume_unique to True if we are certain that both ndarrays are set arrays.

    # The ufunc np.setdiff1d() removes the elements of the second ndarray from the first ndarray (if they exist in it):
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
print("4.", np.setdiff1d(arr1, arr2, assume_unique=True))

    # The ufunc np.setxor1d() joins the ndarrays together whilst removing the shared elements:
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
print("5.", np.setxor1d(arr1, arr2, assume_unique=True))
