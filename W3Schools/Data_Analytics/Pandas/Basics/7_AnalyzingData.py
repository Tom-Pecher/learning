
# PYTHON: W3Schools - Pandas Tutorial
# Section 7: Analyzing Data

import pandas as pd

# BASICS
    # Use df.head(i) to print the first i rows of a dataframe (i=5 by default): 
df = pd.read_json('Python/W3Schools/Pandas_Tutorial/Basics/example_files/data.json')
print("1.", df.head(10))

    # Use df.tail(i) to print the last i rows of a dataframe (i=5 by default): 
df = pd.read_json('Python/W3Schools/Pandas_Tutorial/Basics/example_files/data.json')
print("2.", df.tail(10))

    # We can use df.info() to print some basic information about the data, such as the dimensions, memory usage and null values:
print("3.") 
df.info()
