
# PYTHON: W3Schools - NumPy Tutorial
# Section 9: Ufunc Finding LCM

import numpy as np

# BASICS
    # The ufunc np.lcm() returns the lowest common multiple of two integers:
print("1.", np.lcm(4, 6))

    # We can also supply a collection and use the reduce() method:
arr = np.array([3, 6, 9])
print("2.", np.lcm.reduce(arr))
