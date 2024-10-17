
# PYTHON: W3Schools - Matplotlib Tutorial
# Section 2: Pyplot

# BASICS
    # Import matplotlib's pyplot:
import matplotlib.pyplot as plt
import numpy as np

    # Create data
xpoints = np.array(range(0, 6))
ypoints = np.random.rand(6)

    # Plot the data
plt.plot(xpoints, ypoints)
plt.show()
