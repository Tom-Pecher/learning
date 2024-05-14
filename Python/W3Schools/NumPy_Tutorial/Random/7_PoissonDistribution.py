
# PYTHON: W3Schools - NumPy Tutorial
# Section 7: Poisson Distribution

import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

# BASICS
    # The function random.poisson() samples from a Poisson distribution with the specified lambda:
print("1.", random.poisson(lam=2, size=10))

    # Again, we can plot the distribution using the seaborn module:
sns.histplot(random.poisson(lam=2, size=1000), kde=False)
plt.show()
