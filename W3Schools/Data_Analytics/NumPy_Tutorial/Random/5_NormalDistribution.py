
# PYTHON: W3Schools - NumPy Random Tutorial
# Section 5: Normal Distribution

import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

# BASICS
    # The function random.normal() will create an ndarray of a specified size where the elements are sampled from the standard normal distribution:
print("1.", random.normal(size=(2, 3)))

    # We can specify a mean and standard deviation with the loc and scale keyword arguments respectively:
print("2.", random.normal(loc=1, scale=2, size=(2, 3)))

    # As mentioned previously, we can use the seaborn module to visualize this distribution:
sns.histplot(random.normal(size=1000))
plt.show()
