
# PYTHON: W3Schools - Pandas Cleaning Data Tutorial
# Section 3: Wrong Format

import pandas as pd

# BASICS
    # If some entries in a series are not of the correct format, we can assign them with their corrected datatype (in this case Date):
df = pd.read_csv('Python/W3Schools/Pandas_Tutorial/Cleaning_Data/example_files/data.csv')
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
print("1.", df.to_string())

    # To remove the NaT (Not-A-Time), we can drop the rows with a NaT as their date:
df.dropna(subset=['Date'], inplace=True)
print("2.", df.to_string())
