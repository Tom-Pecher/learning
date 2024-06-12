
# PYTHON: W3Schools - NumPy Random Tutorial
# Section 14: Pareto Distribution

import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

# BASICS
    # The function random.pareto() samples from a Pareto distribution with the specified shape parameter:
print("1.", random.pareto(a=2, size=(2, 3)))

    # Again, we can plot the distribution using the seaborn module:
sns.histplot(random.pareto(a=2, size=1000), kde=False)
plt.show()
