
# PYTHON: W3Schools - NumPy Tutorial
# Section 5: Ufunc Logarithms

import numpy as np

# BASICS
    # The ufunc np.log2() takes the log (base 2) of the elements in a collection:
arr = np.arange(1, 10)
print("1.", np.log2(arr))

    # The ufunc np.log10() takes the log (base 10) of the elements in a collection:
arr = np.arange(1, 10)
print("2.", np.log10(arr))

    # The ufunc np.log() takes the natural log (base e) of the elements in a collection:
arr = np.arange(1, 10)
print("3.", np.log(arr))

    # Numpy does not have every log base built in so for other logarithms we have to use a custom ufunc:
from math import log
nplog = np.frompyfunc(log, 2, 1)
print("4.", nplog(100, 15))
