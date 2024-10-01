
# PYTHON: W3Schools - NumPy Random Tutorial
# Section 9: Logistic Distribution

import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

# BASICS
    # The function random.logistic() samples from a logistic distribution with the specified mean (loc) and standard deviation (scale):
print("1.", random.logistic(loc=1, scale=2, size=(2, 3)))

    # Again, we can plot the distribution using the seaborn module:
sns.histplot(random.logistic(size=1000), kde=False)
plt.show()
