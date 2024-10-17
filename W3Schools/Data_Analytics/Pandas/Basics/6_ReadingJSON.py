
# PYTHON: W3Schools - Pandas Tutorial
# Section 6: Reading JSON

import pandas as pd

# BASICS
    # We can use pd.read_json() to extract the contents of a JSON file:
df = pd.read_json('Python/W3Schools/Pandas_Tutorial/Basics/example_files/data.json')
print("1.", df)

    # JSON objects function identically to dictionaries so we can make dataframes from them:
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}
df = pd.DataFrame(data)
print("2.", df)
