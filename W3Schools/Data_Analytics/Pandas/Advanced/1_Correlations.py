
# PYTHON: W3Schools - Pandas Advanced Tutorial
# Section 1: Correlations

import pandas as pd

# BASICS
    # The function df.corr() returns a correlation matrix (how related each numerical data column is to each other):
df = pd.read_csv('Python/W3Schools/Pandas_Tutorial/Advanced/example_files/data.csv')
print("1.", df.corr())
