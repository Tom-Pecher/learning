
# PYTHON: W3Schools - Pandas Tutorial
# Section 4: Data Frames

import pandas as pd

# BASICS
    # A pandas data frame is a 2-dimensional structure, a table containing data:
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print("1.", df)

    # Pandas uses the loc keyword to refer to series (columns) in the table:
print("2.", df.loc[0])

    # To access multiple series, we can use shorthand index notation:
print("3.", df.loc[[0, 1]])

    # Again, we can label the rows of our table:
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print("4.", df)

    # And access series using those labels:
print("5.", df.loc["day2"])
