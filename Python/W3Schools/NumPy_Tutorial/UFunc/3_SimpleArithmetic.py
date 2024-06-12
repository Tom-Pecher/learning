
# PYTHON: W3Schools - NumPy Ufunc Tutorial
# Section 3: Simple Arithmetic

import numpy as np

# BASICS
    # The ufunc np.add() adds the elements of two collections:
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.add(arr1, arr2)
print("1.", newarr)

    # The ufunc np.subtract() subtracts the elements of two collections:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.subtract(arr1, arr2)
print("2.", newarr)

    # The ufunc np.multiply() multiplies the elements of two collections:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.multiply(arr1, arr2)
print("3.", newarr)

    # The ufunc np.divide() divides the elements of two collections:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])
newarr = np.divide(arr1, arr2)
print("4.", newarr)

    # The ufunc np.power() exponentiates the elements of the first collection to the elements of the second:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 6, 8, 2, 33])
newarr = np.power(arr1, arr2)
print("5.", newarr)

    # The ufuncs np.mod() and np.remainder() gives the remaiders of dividing the elements of the first collection by those in the second:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr = np.mod(arr1, arr2)
print("6.", newarr)

    # The ufunc np.divmod() returns both the quotients and remainders of dividing the elements of the first collection by those in the second:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr = np.divmod(arr1, arr2)
print("7.", newarr)

    # The ufuncs np.abs() and np.absolute() return the absolute values of elements in the collection:
arr = np.array([-1, -2, 1, 2, 3, -4])
newarr = np.absolute(arr)
print("8.", newarr)
