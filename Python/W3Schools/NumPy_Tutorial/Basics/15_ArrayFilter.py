
# PYTHON: W3Schools - NumPy Tutorial
# Section 15: Array Filter

import numpy as np

# BASICS
    # Using a list of booleans, we can filter the values of an ndarray:
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
print("1.", arr[x]) 

arr = np.array([41, 42, 43, 44])

    # Here is how we might iteratively generate a filter array:
filter_arr = []
for element in arr:
    filter_arr.append(element > 42)
print("2.", arr[filter_arr])

    # The better way to do this is to apply the boolean to the whole ndarray and it will evaluate each element:
filter_arr = arr % 2 == 0
print("3.", arr[filter_arr])
