
# PYTHON: W3Schools - Pandas Cleaning Data Tutorial
# Section 4: Wrong Data

import pandas as pd

# BASICS
    # If there are entries that are valid but obviously wrong, we can change them manually:
df = pd.read_csv('Python/W3Schools/Pandas_Tutorial/Cleaning_Data/example_files/data.csv')
df.loc[7, 'Duration'] = 45

    # We can set bounds for our values by iterating through:
df = pd.read_csv('Python/W3Schools/Pandas_Tutorial/Cleaning_Data/example_files/data.csv')
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120

    # Or we can remove the corresponding rows:
df = pd.read_csv('Python/W3Schools/Pandas_Tutorial/Cleaning_Data/example_files/data.csv')
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace=True)
