
# PYTHON: W3Schools - NumPy Tutorial
# Section 2: Data Distributions

from numpy import random

# BASICS
    # Using random.choice(), we can define our own discrete probability distribution:
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print("1.", x)

    # And again, we can configure the shape of the ndarray in which we store our samples:
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print("2.", x)
