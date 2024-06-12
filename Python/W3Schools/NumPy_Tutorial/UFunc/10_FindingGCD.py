
# PYTHON: W3Schools - NumPy Tutorial
# Section 10: Finding GCD

import numpy as np

# BASICS
    # The ufunc np.gcd() returns the greatest common divisor of two integers:
print("1.", np.gcd(4, 6))

    # We can also supply a collection and use the reduce() method:
arr = np.array([3, 6, 9])
print("2.", np.gcd.reduce(arr))
