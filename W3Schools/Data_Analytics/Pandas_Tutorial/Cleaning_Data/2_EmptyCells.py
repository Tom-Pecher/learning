
# PYTHON: W3Schools - Pandas Cleaning Data Tutorial
# Section 2: Empty Cells

import pandas as pd

# BASICS
    # One way to deal with missing cells is to remove all rows with missing cells, which is achieve with df.dropna():
df = pd.read_csv('Python/W3Schools/Pandas_Tutorial/Cleaning_Data/example_files/data.csv')
new_df = df.dropna()
print("1.", new_df.to_string())

    # By default, df.dropna() does not modify the original, however we can allow this by setting inplace to True:
df = pd.read_csv('Python/W3Schools/Pandas_Tutorial/Cleaning_Data/example_files/data.csv')
df.dropna(inplace=True) # NOTE: it no longer returns a new dataframe because it modifies the original.
print("2.", df.to_string())


# REPLACEMENT
    # An alternative is filling empty cells with a specified value, achieved with df.fillna(), inplace can also be specified:
df = pd.read_csv('Python/W3Schools/Pandas_Tutorial/Cleaning_Data/example_files/data.csv')
df.fillna(130, inplace=True)
print("3.", df.to_string())

    # Here is how we can apply this to just a single series:
df = pd.read_csv('Python/W3Schools/Pandas_Tutorial/Cleaning_Data/example_files/data.csv')
df["Calories"].fillna(130, inplace=True) 
print("4.", df.to_string())

    # Pandas also allows us to calculate averages which we can use to fill empty cells:
df = pd.read_csv('Python/W3Schools/Pandas_Tutorial/Cleaning_Data/example_files/data.csv')
x = df["Calories"].mean()
y = df["Calories"].median()
z = df["Calories"].mode()[0] # NOTE: df.mode() returns a series so we must index to obtain the value.
df["Calories"].fillna(z, inplace=True) 
print("5.", df.to_string())
