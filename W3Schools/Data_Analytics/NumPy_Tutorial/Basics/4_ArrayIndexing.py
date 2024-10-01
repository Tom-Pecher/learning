
# PYTHON: W3Schools - NumPy Tutorial
# Section 4: Array Indexing

import numpy as np

# BASICS
    # Indexing works much the same way as for any other collection:
arr = np.array([[0, 1, 1, 2], [3, 5, 8, 13]])
print("1.", arr[1][-1])

    # However, since ndarrays usually have many dimesions, we can list indices using shorthand:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("2.", arr[0, 1, 2])
