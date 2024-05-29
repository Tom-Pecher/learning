
# PYTHON: W3Schools - NumPy Tutorial
# Section 15: Zipf Distribution

import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

# BASICS
    # The function random.zipf() samples from a Zipf distribution with the distribution parameter:
print("1.", random.zipf(a=2, size=(2, 3)))

    # Again, we can plot the distribution using the seaborn module:
sns.histplot(random.zipf(a=2, size=1000), kde=False)
plt.show()
