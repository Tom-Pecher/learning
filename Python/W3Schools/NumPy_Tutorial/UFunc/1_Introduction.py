
# PYTHON: W3Schools - NumPy Tutorial
# Section 1: Introduction

import numpy as np

# Universal functions (ufuncs) are numpy functions that can be applied to collections.
# They use vectorization rather than iterating over the elements, making the much faster.
# They also provide additional functionality that is useful for computation:
#   where   - boolean array or condition defining where the operations should take place.
#   dtype   - defining the return type of elements.
#   out     - output array where the return value should be copied

# BASICS
    # For example, the add function allows us to quickly add two lists:
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
print("1.", np.add(x, y))

    # Whereas normally, we would have to iterate like so:
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []
for i, j in zip(x, y):
  z.append(i + j)
print("2.", z)
