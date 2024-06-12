
# PYTHON: W3Schools - Pandas Tutorial
# Section 2: Getting Started

import pandas as pd

# BASICS
    # We can import the pandas functionality like any other module:
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print("1.", myvar)

    # We can check the version like so:
print("2.", pd.__version__)
