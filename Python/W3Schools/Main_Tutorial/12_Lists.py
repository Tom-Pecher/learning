
# PYTHON: W3Schools - Main Tutorial
# Section 12: Lists

# BASICS
    # Lists are mutable, ordered collections of nonunique elements, denoted by the [] brackets.
    # Lists can contain all data types and even different data types at once.

    # We can use len() to determine the number of elements in a list.
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("1.", len(this_list))

    # Using type on a list will return <class 'list'>:
print("2.", type(this_list))

    # We can also use the list() constructor to convert other data types into lists:
this_list = list(("apple", "banana", "cherry"))


# ACCESSING ELEMENTS
    # We can access elements at specific positions in a list by indexing:
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("3.", this_list[1])      # prints second item

    # Indices can be negative, starting from the end of the list:
print("4.", this_list[-1])     # prints last item

    # We can also take a range of indices:
print("5.", this_list[2:5])    # prints a list containing the third, fourth and fifth elements

    # We do not have to specify two limits:
print("6.", this_list[:4])     # prints a list containing the first four elements

    # We can also check if an item is contained in a list using the in operator:
this_list = ["apple", "banana", "cherry"]
print("7.", "apple" in this_list)


# CHANGING ELEMENTS
    # We can reassign elements of a list using their index:
this_list = ["apple", "banana", "cherry"]
this_list[1] = "blackcurrant"
print("8.", this_list)

    # We can do this for a range of values as well:
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
this_list[1:3] = ["blackcurrant", "watermelon"]
print("9.", this_list)
# NOTE: The list length will change if the range is different from the collection being inserted.


# ADDING ELEMENTS
    # list.insert(index, value)
        # input types: int, value
        # output type: None
    # Inserts an item to the list at index position.
this_list = ["apple", "banana", "cherry"]
this_list.insert(2, "watermelon")
print("10.", this_list)

    # list.append(value)
        # input type: value
        # output type: None
    # Adds item to the end of the list.
this_list = ["apple", "banana", "cherry"]
this_list.append("orange")
print("11.", this_list)

    # list.extend(collection)
        # input type: collection
        # output type: None
    # Adds items from the collection to the end of the list.
this_list = ["apple", "banana", "cherry"]
this_tuple = ("kiwi", "orange")
this_list.extend(this_tuple)
print("12.", this_list)


# REMOVING ITEMS
    # list.remove(value)
        # input type: value
        # output type: None
    # Removes first occurence of value from the list.
this_list = ["apple", "banana", "cherry", "banana", "kiwi"]
this_list.remove("banana")
print("13.", this_list)

    # list.pop(index=-1)
        # input type: int
        # output type: value
    # Returns value at index position after removing it from the list, index is -1 by default.
this_list = ["apple", "banana", "cherry"]
this_list.pop(1)
print("14.", this_list)

    # We can also use the del keyword to completely delete an element:
this_list = ["apple", "banana", "cherry"]
del this_list[0]
print("15.", this_list)

    # Or the entire list
del this_list

    # list.clear()
        # input type: None
        # output type: None
    # Empties list.
this_list = ["apple", "banana", "cherry"]
this_list.clear()
print("16.", this_list)


# LOOPING THROUGH LISTS:
    # We can use a for loop to loop through each element in a list:
this_list = ["apple", "banana", "cherry"]
for x in this_list:
  print("17.", x)

    # We can also use list comprehension as shorthand to create new lists with a for loop:
print("18.", [x**2 for x in range(5)])

    # List comprehension can also have an if statement that filters values of the for loop:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = [x for x in fruits if "a" in x]
print("19.", new_list)

    # The expression itself can also contain conditional statements that manipulate the outcome rather than filtering:
new_list = [x if x != "banana" else "orange" for x in fruits]


# SORTING
    # list.sort(key=function, reverse=False)
        # input type: function, bool
        # output type: None
    # Sorts the list based on a function, sorts alphanumerically by default.
this_list = [100, 50, 65, 82, 23]
this_list.sort()
print("20.", this_list)

    # We can also sort in descending order:
this_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
this_list.sort(reverse = True)
print("21.", this_list)

    # Here we sort based on a function:
def myfunc(n):
  return abs(n - 50)
this_list = [100, 50, 65, 82, 23]
this_list.sort(key = myfunc)
print("22.", this_list)

    # Here we do the same thing but with a lambda function:
this_list = [100, 50, 65, 82, 23]
this_list.sort(key = lambda x: abs(x - 50))
print("23.", this_list)

    # This is how one might do case-insensitive sort:
this_list = ["banana", "Orange", "Kiwi", "cherry"]
this_list.sort(key = str.lower)
print("24.", this_list)

    # sorted(collection, key=function, reverse=False)
        # input type: collection, function, bool
        # output type: collection
    # Returns sorted collection without changing the original:
this_list = ["banana", "Orange", "Kiwi", "cherry"]
print("25.", sorted(this_list))

    # list.reverse()
        # input type: None
        # output type: None
    # Reverses the order of the list.
this_list = ["banana", "Orange", "Kiwi", "cherry"]
this_list.reverse()
print("26.", this_list)


# COPYING A LIST
    # To copy a list's contents, we cannot simply write list1 = list2 as this is pass-by-reference and so they are still
    # the same object (changes to one list will also change the other).

    # list.copy()
        # input type: None
        # output type: list
    # Creates a copy of the list
this_list = ["apple", "banana", "cherry"]
my_list = this_list.copy()
print("27.", my_list)

    # Since list() is a constructor, it also makes copies:
this_list = ["apple", "banana", "cherry"]
my_list = list(this_list)
print("28.", my_list)


# JOINING LISTS
    # The + operator can be used on lists to join them:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print("29.", list3)

    # We can also duplicate a list's contents:
fruits = ["apple", "banana", "cherry"]
my_list = fruits * 2
print("30.", my_list) 
