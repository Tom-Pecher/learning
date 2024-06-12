
# PYTHON: W3Schools - Pandas Advanced Tutorial
# Section 2: Plotting

import pandas as pd
import matplotlib.pyplot as plt

# BASICS
    # Pandas uses df.plot() to create plots of the specified dataframe:
df = pd.read_csv('Python/W3Schools/Pandas_Tutorial/Advanced/example_files/data.csv')
df.plot()
plt.show()

    # To create a scatter graph, we need to specify it as such as well as the x and y axes:
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
plt.show()

    # To create a histogram, we need to specify it as such:
df["Duration"].plot(kind = 'hist')
plt.show()
