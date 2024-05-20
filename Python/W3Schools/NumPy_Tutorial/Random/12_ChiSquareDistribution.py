
# PYTHON: W3Schools - NumPy Tutorial
# Section 12: Chi-Square Distribution

import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

# BASICS
    # The function random.chisquare() samples from a chi-square distribution with the specified degrees of freedom:
print("1.", random.chisquare(df=2, size=(2, 3)))

    # Again, we can plot the distribution using the seaborn module:
sns.histplot(random.chisquare(df=1, size=1000), kde=False)
plt.show()
