
# PYTHON: W3Schools - NumPy Tutorial
# Section 7: Copying and Viewing

# BASICS
    # The np.ndarray.copy() function returns a new, separate ndarray:
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print("1.", arr, x)

    # The np.ndarray.view() function returns a reference to the original ndarray:
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print("2.", arr, x)

    # Changes to one affect the other (both ways) since they are the same object:
x[0] = 60
print("3.", arr, x)

    # The base attribute of an ndarray variable returns the original contents (returns None if it contains its own contents):
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print("4.", x.base)
print("5.", y.base)
