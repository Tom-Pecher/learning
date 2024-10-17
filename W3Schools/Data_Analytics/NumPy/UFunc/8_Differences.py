
# PYTHON: W3Schools - NumPy Ufunc Tutorial
# Section 8: Differences

import numpy as np

# BASICS
    # The ufunc np.diff() subtracts every element i from the next element i+1:
arr = np.array([10, 15, 25, 5])
print("1.", np.diff(arr))

    # We can repeat this process n times by specifying n:
arr = np.array([10, 15, 25, 5])
print("2.", np.diff(arr, n=2))
