
# PYTHON: W3Schools - Tutorial
# Section 30: JSON


# BASICS
    # We can manipulate JSON data with the with the json module:
import json

    # We can convert json into a dictionary using json.loads()
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print("1.", y["age"]) 

    # Likewise, we can convert a dictionary to JSON using json.dumps():
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x)
print("2.", y) 

    # json.dumps() converts all of the following to JSON like so:
        # dict 	        Object
        # list 	        Array
        # tuple 	    Array
        # str 	        String
        # int 	        Number
        # float 	    Number
        # True 	        true
        # False 	    false
        # None 	        null

# FORMATTING
    # Here is a dictionary containing all legal datatypes:
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print("3.", json.dumps(x))

    # We can specify the formatting we require:
print("4.", json.dumps(x, indent=4, separators=(". ", " = ")))

    # And if we want the result to be sorted:
print("5.", json.dumps(x, indent=4, sort_keys=True))
