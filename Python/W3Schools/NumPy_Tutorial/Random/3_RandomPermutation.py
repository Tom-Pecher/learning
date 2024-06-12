
# PYTHON: W3Schools - NumPy Random Tutorial
# Section 3: Random Permutation

from numpy import random
import numpy as np

# BASICS
    # There are two functions for rearranging ndarray elements. First, random.shuffle() which shuffles the specified array:
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print("1.", arr)

    # And random.permutation() which does the same thing except it returns a copy instead:
arr = np.array([1, 2, 3, 4, 5])
print("2.", random.permutation(arr)) 
