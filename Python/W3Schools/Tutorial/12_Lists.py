
# PYTHON: W3Schools - Tutorial
# Section 12: Lists

# BASICS
    # Lists are mutable, ordered collections of nonunique elements, denoted by the [] brackets.
    # Lists can contain all data types and even different data types at once.

    # We can use len() to determine the number of elements in a list.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(len(thislist))

    # Using type on a list will return <class 'list'>:
print(type(thislist))

    # We can also use the list() constructor to convert other data types into lists:
thislist = list(("apple", "banana", "cherry"))


# ACCESSING ELEMENTS
    # We can access elements at specific positions in a list by indexing:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1])      # prints second item

    # Indices can be negative, starting from the end of the list:
print(thislist[-1])     # prints last item

    # We can also take a range of indices:
print(thislist[2:5])    # prints a list containing the third, fourth and fifth elements

    # We do not have to specify two limits:
print(thislist[:4])     # prints a list containing the first four elements

    # We can also check if an item is contained in a list using the in operator:
thislist = ["apple", "banana", "cherry"]
print("apple" in thislist)


# CHANGING ELEMENTS
    # We can reassign elements of a list using their index:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

    # We can do this for a range of values as well:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# NOTE: The list length will change if the range is different from the collection being inserted.


# ADDING ELEMENTS
    # list.insert(index, value)
        # input types: int, value
        # output type: None
    # Inserts an item to the list at index position.
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

    # list.append(value)
        # input type: value
        # output type: None
    # Adds item to the end of the list.
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

    # list.extend(collection)
        # input type: collection
        # output type: None
    # Adds items from the collection to the end of the list.
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


# REMOVING ITEMS
    # list.remove(value)
        # input type: value
        # output type: None
    # Removes first occurence of value from the list.
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

    # list.pop(index=-1)
        # input type: int
        # output type: value
    # Returns value at index position after removing it from the list, index is -1 by default.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

    # We can also use the del keyword to completely delete an element:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

    # Or the entire list
del thislist

    # list.clear()
        # input type: None
        # output type: None
    # Empties list.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


# LOOPING THROUGH LISTS:
    # We can use a for loop to loop through each element in a list:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

    # We can also use list comprehension as shorthand to create new lists with a for loop:
print([x**2 for x in range(5)])

    # List comprehension can also have an if statement that filters values of the for loop:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

    # The expression itself can also contain conditional statements that manipulate the outcome rather than filtering:
newlist = [x if x != "banana" else "orange" for x in fruits]


# SORTING
    # list.sort(key=function, reverse=False)
        # input type: function, bool
        # output type: None
    # Sorts the list based on a function, sorts alphanumerically by default.
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

    # We can also sort in descending order:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

    # Here we sort based on a function:
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

    # Here we do the same thing but with a lambda function:
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = lambda x: abs(x - 50))
print(thislist)

    # This is how one might do case-insensitive sort:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

    # sorted(collection, key=function, reverse=False)
        # input type: collection, function, bool
        # output type: collection
    # Returns sorted collection without changing the original:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
print(sorted(thislist))

    # list.reverse()
        # input type: None
        # output type: None
    # Reverses the order of the list.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


# COPYING A LIST
    # To copy a list's contents, we cannot simply write list1 = list2 as this is pass-by-reference and so they are still
    # the same object (changes to one list will also change the other).

    # list.copy()
        # input type: None
        # output type: list
    # Creates a copy of the list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

    # Since list() is a constructor, it also makes copies:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


# JOINING LISTS
    # The + operator can be used on lists to join them:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
