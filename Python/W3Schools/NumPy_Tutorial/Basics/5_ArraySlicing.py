
# PYTHON: W3Schools - NumPy Tutorial
# Section 5: Array Slicing

import numpy as np

# BASICS
    # Slicing also works much the same way as for any other collection:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("1.", arr[1:4])

    # This includes setting a step size:
print("2.", arr[1:6:2])
print("3.", arr[1::3])

    # Conveniently, this can also be performed on higher-dimensional tensors:
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])
