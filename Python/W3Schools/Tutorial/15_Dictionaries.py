
# PYTHON: W3Schools - Tutorial
# Section 15: Dictionaries

# BASICS
    # Dictionaries are mutable, ordered collections of unique key-value pairs, denoted by the {key:value} brackets.
    # Dictionaries can contain all data types and even different data types at once.
this_dict =	{
  "brand" : "Ford",
  "model" : "Mustang",
  "year"  : 1964
}
print("1.", this_dict)

    # We can access the value with its key:
print("2.", this_dict["brand"]) # returns "Ford"

    # We can use len() to obtain the number of key-value pairs:
print("3.", len(this_dict))

    # keys and values can be any type
this_dict =	{
  "brand" : 3j,
  0       : False,
  3.1     : 1964,
  False   : ["red", "white", "blue"]
}
print("4.", this_dict)

    # Using type on a set will return <class 'dict'>:
print("5.", type(this_dict))

    # We can use the dict() constructor to convert a collection of kwargs into a dictionary:
this_dict = dict(name = "John", age = 36, country = "Norway")
print("6.", this_dict)


# ACCESSING ELEMENTS
    # As discussed, we can obtain the value of a specified key:
this_dict =	{
  "brand" : "Ford",
  "model" : "Mustang",
  "year"  : 1964
}
x = this_dict["model"]
print("7.", x)

    # This is shorthand for the dict.get(key) method:
x = this_dict.get("model")
print("8.", x)

    # dict.keys()
        # input type: None
        # output type: dict_keys
    # Returns a dict_keys object containing all of the keys in the dictionary:
x = this_dict.keys()
print("9.", x)

    # dict.values()
        # input type: None
        # output type: dict_values
    # Returns a dict_values object containing all of the keys in the dictionary:
x = this_dict.values() 
print("10.", x)

    # dict.items()
        # input type: None
        # output type: dict_items
    # Returns a dict_items object containing all of the keys in the dictionary as tuples:
x = this_dict.items() 
print("11.", x)

    # We can use the in keyword to check if a key is contained in the dictionary:
this_dict =	{
  "brand" : "Ford",
  "model" : "Mustang",
  "year"  : 1964
}
print("12.", "model" in this_dict)


# ADDING/CHANGING ELEMENTS
    # We can assign/reassign values of keys like so:
this_dict =	{
  "brand" : "Ford",
  "model" : "Mustang",
  "year"  : 1964
}
this_dict["year"] = 2018
this_dict["colour"] = "red"
print("13.", this_dict)

    # dict.update(dict)
        # Input type: dict
        # Output type: None
    # Adds and modifies entries of the original dictionary based on entries for the new dictionary:
this_dict =	{
  "brand" : "Ford",
  "model" : "Mustang",
  "year"  : 1964
}
this_dict.update({"year": 2020, "colour" : "red"}) 
print("14.", this_dict)


# REMOVING ELEMENTS
    # dict.pop(key)
        # Input type: any
        # Output type: any
    # Returns the value of the key and removes specified entry from the dictionary.
this_dict =	{
  "brand" : "Ford",
  "model" : "Mustang",
  "year"  : 1964
}
print("15.", this_dict.pop("model"))

    # dict.popitem()
        # Input type: None
        # Output type: any
    # Returns the last entered key-value pair as a tuple and removes the entry from the dictionary.
this_dict =	{
  "brand" : "Ford",
  "model" : "Mustang",
  "year"  : 1964
}
print("16.", this_dict.popitem())

    # Again, the del keyword completely deletes a dictionary:
del this_dict

    # dict.clear()
        # Input type: None
        # Output type: None
    # Empties the dictionary.
this_dict =	{
  "brand" : "Ford",
  "model" : "Mustang",
  "year"  : 1964
}
this_dict.clear()
print("17.", this_dict) 


# LOOPING THROUGH DICTIONARIES
    # We can loop over all keys in a dictionary like so:
this_dict =	{
  "brand" : "Ford",
  "model" : "Mustang",
  "year"  : 1964
}
for x in this_dict:
  print("19.", x)

    # Or all values:
for x in this_dict:
  print("19.", this_dict[x]) 

    # Or both simultaneously:
for x, y in this_dict.items():
  print("20.", x, y)


# COPYING A DICTIONARY
    # dict.copy()
        # input type: None
        # output type: dict
    # Creates a copy of the dict.
this_dict =	{
  "brand" : "Ford",
  "model" : "Mustang",
  "year"  : 1964
}
my_dict = this_dict.copy()

    # Or we can use the dict() constructor:
this_dict =	{
  "brand" : "Ford",
  "model" : "Mustang",
  "year"  : 1964
}
my_dict = dict(this_dict)
