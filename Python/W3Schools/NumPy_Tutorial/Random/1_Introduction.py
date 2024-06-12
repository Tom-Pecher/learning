
# PYTHON: W3Schools - NumPy Tutorial
# Section 1: Introduction

from numpy import random

# BASICS
    # The function random.rand() generates a pseudorandom float from 0 to 1 (inclusive):
x = random.rand()
print("1.", x)

    # The function random.randint(int) generates a pseudorandom integer from 0 to the given integer (inclusive):
x = random.randint(100)
print("2.", x)

    # The function random.choice(ndarray) picks an item pseudorandomly from the specified ndarray:
x = random.choice([3, 5, 7, 9])
print("3.", x)

    # For rand, we specify a shape and it will generate an ndarray of that shape filled with pseudorandom floats from 0 to 1:
x = random.rand(3, 5)
print("5.", x)

    # For randint, we must do this by specifyinmg the shape as a keyword argument instead:
x = random.randint(100, size=(3, 5))
print("4.", x)

    # The same is true for choice:
x = random.choice([3, 5, 7, 9], size=(3, 5))
print("6.", x)
