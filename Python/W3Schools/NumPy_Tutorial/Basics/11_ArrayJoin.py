
# PYTHON: W3Schools - NumPy Tutorial
# Section 11: Array Join

# BASICS
    # In numpy, we cannot use + to join ndarrays (this would add the contents), instead we can use np.concatenate():
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print("1.", arr)

    # We can change the axis on which we join the ndarrays:
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print("2.", arr)


# STACKING
    # When stacking two arrays, we essentially put one on top of the other (displayed as to the right):
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print("3.", arr)

    # The function np.hstack() stacks along rows:
arr = np.hstack((arr1, arr2))
print("4.", arr)

    # The function np.vstack() stacks along columns:
arr = np.vstack((arr1, arr2))
print("5.", arr)

    # The function np.dstack() stacks along height (depth):
arr = np.dstack((arr1, arr2))
print("6.", arr)
