
# PYTHON: W3Schools - NumPy Random Tutorial
# Section 11: Exponential Distribution

import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

# BASICS
    # The function random.exponential() samples from an exponential distribution with the specified inverse lambda value:
print("1.", random.exponential(scale=2, size=(2, 3)))

    # Again, we can plot the distribution using the seaborn module:
sns.histplot(random.exponential(size=1000), kde=False)
plt.show()
