
# PYTHON: W3Schools - NumPy Tutorial
# Section 12: Hyperbolic

import numpy as np

# BASICS
    # The ufunc np.sinh() takes radians and returns the corresponding hyperbolic sine value:
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
print("1.", np.sinh(arr))

    # The ufunc np.cosh() takes radians and returns the corresponding hyperbolic cosine value:
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
print("2.", np.cosh(arr))

    # The ufunc np.tanh() takes radians and returns the corresponding hyperbolic tangent value:
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
print("3.", np.tanh(arr))

    # The ufunc np.arcsinh() takes radians and returns the corresponding inverse hyperbolic sine value:
arr = np.array([0.1, 0.2, 0.5])
print("4.", np.arcsinh(arr))

    # The ufunc np.arccosh() takes radians and returns the corresponding inverse hyperbolic cosine value:
arr = np.array([1.1, 1.2, 1.5])
print("5.", np.arccosh(arr))

    # The ufunc np.arctanh() takes radians and returns the corresponding inverse hyperbolic tangent value:
arr = np.array([0.1, 0.2, 0.5])
print("6.", np.arctanh(arr))
