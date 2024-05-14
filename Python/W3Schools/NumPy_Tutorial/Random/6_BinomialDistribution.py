
# PYTHON: W3Schools - NumPy Tutorial
# Section 6: Binomial Distribution

import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

# BASICS
    # The function random.binomial() samples from a binomial distribution with the specified n and p:
print("1.", random.binomial(n=10, p=0.5, size=10))

    # Again, we can plot the distribution using the seaborn module:
sns.histplot(random.binomial(n=10, p=0.5, size=1000), kde=False)
plt.show()
