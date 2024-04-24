
# PYTHON: W3Schools - Tutorial
# Section 14: Sets

# BASICS
    # Sets are immutable, unordered collections of unique elements, denoted by the {} brackets.
    # Sets can contain all data types and even different data types at once.
    # NOTE: However, values like True and False are considered as 1 and 0 and will be removed if 0 or 1 already exists.
this_set = {"apple", "banana", "cherry", True, 1, 2}
print("1.", this_set)

    # Again, len() can be used to obtain the length of a set:
this_set = {"apple", "banana", "cherry"}
print("2.", len(this_set))

    # Using type on a set will return <class 'set'>:
print("3.", type(this_set))

    # We can also use the list() constructor to convert other data types into lists:
this_set = set(("apple", "banana", "cherry"))
print("4.", this_set)


# ACCESSING ELEMENTS
    # Again, we can iterate through set elements with a for loop:
this_set = {"apple", "banana", "cherry"}
for x in this_set:
  print("5.", x)

    # And check if certain elements are contained within the set:
this_set = {"apple", "banana", "cherry"}
print("6.", "banana" in this_set)


# ADDING ELEMENTS
    # set.add(value)
        # input type: value
        # output type: None
    # Adds value to the set under the uniqueness property.
this_set = {"apple", "banana", "cherry"}
this_set.add("orange")
print("7.", this_set) 

    # set.update(collection)
        # input type: collection
        # output type: None
    # Adds collection's elements to the set under the uniqueness property.
this_set = {"apple", "banana", "cherry"}
this_set.update(("orange", "green"))
print("8.", this_set)


# REMOVING ELEMENTS
    # set.remove(value)
        # input type: value
        # output type: None
    # Removes value from the set, throws error if the item is not present.
this_set = {"apple", "banana", "cherry"}
this_set.remove("banana")
print("9.", this_set)

    # set.discard(value)
        # input type: value
        # output type: None
    # Removes value from the set, does not throw error if the item is not present.
this_set = {"apple", "banana", "cherry"}
this_set.discard("banana")
print("10.", this_set)

    # set.pop()
        # input type: None
        # output type: value
    # Removes and returns value from the set.
this_set = {"apple", "banana", "cherry"}
x = this_set.pop()
print("11.", this_set) 

    # set.clear()
        # input type: None
        # output type: None
    # Empties the set.
this_set = {"apple", "banana", "cherry"}
this_set.clear()
print("12.", this_set)


    # The del keyword will completely delete a set:
del this_set


# LOOPING THROUGH SETS
    # We cannot index sets, but we can still loop through each item:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print("13.", x)
