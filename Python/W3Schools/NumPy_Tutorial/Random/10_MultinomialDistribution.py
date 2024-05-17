
# PYTHON: W3Schools - NumPy Tutorial
# Section 10: Multinomial Distribution

from numpy import random

# BASICS
    # The function random.logistic() samples from a logistic distribution with the specified mean (loc) and standard deviation (scale):
print("1.", random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6]))
