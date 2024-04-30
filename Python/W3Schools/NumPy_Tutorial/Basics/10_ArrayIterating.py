
# PYTHON: W3Schools - NumPy Tutorial
# Section 10: Array Iterating

# BASICS
    # We can iterate through an ndarray as with any other collection:
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
for x in arr:
  print("1.", x)

    # The same can be said for higher dimensions:
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  for y in x:
    print("2.", y)


# NDITER
    # Instead of creating a new for loop for each dimension, we can use np.nditer():
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print("3.", x)

    # The following changes the datatype of each element in place (buffered flags allow values to be changed in place and op_dtypes specifies the new datatype):
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print("4.", x)

    # Without the nditer, each x would be an ndarray, however this allows us to iterate across a higher dimensional ndarray as if it were flat:
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
  print("5.", x)
