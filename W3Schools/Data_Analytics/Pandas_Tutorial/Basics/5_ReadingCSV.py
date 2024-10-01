
# PYTHON: W3Schools - Pandas Tutorial
# Section 5: Reading CSV

import pandas as pd

# BASICS
    # We can use pd.read_csv() to extract the contents of a CSV file:
df = pd.read_csv('Python/W3Schools/Pandas_Tutorial/Basics/example_files/data.csv')
print("1.", df)

    # To print the whole dataframe, we can use df.to_string() to convert this to a Python string:
print("2.", df.to_string())

    # Or we can modify the number of display rows (dataframes with more rows than this are reduced to the first 5 and last 5 rows):
pd.options.display.max_rows = 9999
print("3.", df)
