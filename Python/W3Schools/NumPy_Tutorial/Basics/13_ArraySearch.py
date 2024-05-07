
# PYTHON: W3Schools - NumPy Tutorial
# Section 13: Array Search

import numpy as np

# BASICS
    # To obtain the indices of a certain value in an ndarray, we can use np.where():
arr = np.array([1, 2, 3, 4, 5, 4, 4])
print("1.", np.where(arr == 4))

    # This condition can be anything, here is how we might find the indices of all even values:
print("2.", np.where(arr%2 == 0))

    # The function np.searchsorted() returns the index at which the specified item would be inserted if the order was preserved:
arr = np.array([6, 7, 8, 9])
print("3.", np.searchsorted(arr, 7))

    # We can also specify the search direction, notice here the new 7 would be inserted after the old one instead of before:
arr = np.array([6, 7, 8, 9])
print("4.", np.searchsorted(arr, 7, side='right'))

    # We can also search multiple values:
arr = np.array([6, 7, 8, 9])
print("4.", np.searchsorted(arr, [5, 7], side='right'))
