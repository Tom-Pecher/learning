
# PYTHON: W3Schools - NumPy Tutorial
# Section 10: Multinomial Distribution

from numpy import random

# BASICS
    # The function random.multinomial() samples from a multinomial distribution with the specified n and an ndarray of the probability of each outcome:
print("1.", random.multinomial(n=10, pvals=[1/6, 3/6, 2/6]))
