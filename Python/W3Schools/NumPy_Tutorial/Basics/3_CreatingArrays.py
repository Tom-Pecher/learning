
# PYTHON: W3Schools - NumPy Tutorial
# Section 3: Creating Arrays

import numpy as np

# BASICS
    # Numpy's main datatype for manipulating collections of numbers is the ndarray (n-dimensional):
arr = np.array([1, 2, 3, 4, 5]) # NOTE: Strings also count.
print("1.", arr)
print("2.", type(arr)) 

    # We can pass any collection of numbers to np.array to create an ndarray:
arr = np.array((0.0, 1.0, 2.0))
print("3.", arr)

    # Supplying evenly-sized nested collections will essentially result in an n-dimesional tensor:
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("4.", a.ndim, b.ndim, c.ndim, d.ndim)

    # For more complicated tensors, we may specify the minimum dimension:
arr = np.array([1, 2, 3, 4], ndmin=5)
print("5.", arr)
print("6.", arr.ndim) 
