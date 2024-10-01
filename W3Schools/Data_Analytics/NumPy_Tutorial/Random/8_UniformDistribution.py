
# PYTHON: W3Schools - NumPy Random Tutorial
# Section 8: Uniform Distribution

import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

# BASICS
    # The function random.uniform() samples from a continuous uniform distribution with the specified upper and lower bounds (0 and 1 by default):
print("1.", random.uniform(size=(2, 3)))

    # Again, we can plot the distribution using the seaborn module:
sns.histplot(random.uniform(size=1000), kde=False)
plt.show()
