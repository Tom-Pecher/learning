
# PYTHON: W3Schools - NumPy Tutorial
# Section 13: Rayleigh Distribution

import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

# BASICS
    # The function random.chisquare() samples from a Rayleigh distribution with the specified standard deviation:
print("1.", random.rayleigh(scale=2, size=(2, 3)))

    # Again, we can plot the distribution using the seaborn module:
sns.histplot(random.rayleigh(size=1000), kde=False)
plt.show()
