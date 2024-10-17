
# PYTHON: W3Schools - Pandas Cleaning Data Tutorial
# Section 5: Removing Duplicates

import pandas as pd

# BASICS
    # The function df.duplicated() returns a boolean for each row stating if it is a duplicate:
df = pd.read_csv('Python/W3Schools/Pandas_Tutorial/Cleaning_Data/example_files/data.csv')
print("1.", df.duplicated())

    # We can remove duplicate rows using df.drop_duplicates():
df.drop_duplicates(inplace = True) 
print("2.", df.to_string())
