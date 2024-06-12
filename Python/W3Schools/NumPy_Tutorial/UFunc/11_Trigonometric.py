
# PYTHON: W3Schools - NumPy Tutorial
# Section 11: Trigonometric

import numpy as np

# BASICS
    # The ufunc np.sin() takes radians and returns the corresponding sine value:
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
print("1.", np.sin(arr))

    # The ufunc np.cos() takes radians and returns the corresponding cosine value:
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
print("2.", np.cos(arr))

    # The ufunc np.tan() takes radians and returns the corresponding tangent value:
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
print("3.", np.tan(arr))

    # We can convert degrees to radians using np.deg2rad():
arr = np.array([90, 180, 270, 360])
print("4.", np.deg2rad(arr))

    # We can convert radians to degrees using np.rad2deg():
arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
print("5.", np.rad2deg(arr))

    # The ufunc np.arcsin() takes radians and returns the corresponding inverse sine value:
arr = np.array([1, -1, 0.1])
print("6.", np.arcsin(arr))

    # The ufunc np.arccos() takes radians and returns the corresponding inverse cosine value:
arr = np.array([1, -1, 0.1])
print("7.", np.arccos(arr))

    # The ufunc np.arctan() takes radians and returns the corresponding inverse tangent value:
arr = np.array([1, -1, 0.1])
print("8.", np.arctan(arr))

    # The ufunc np.hypot() returns the length of the hypotenuse of a right-angled triangle given the opposite and adjacent sides:
print("9.", np.hypot(6, 8))
