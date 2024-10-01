
# PYTHON: W3Schools - Main Tutorial
# Section 13: Tuples

# BASICS
    # Tuples are immutable, ordered collections of nonunique elements, denoted by the () brackets.
    # Tuples can contain all data types and even different data types at once.

    # To create a tuple with one item, we must add a comma:
this_tuple = ("apple",)
print("1.", type(this_tuple))

    # NOTE: Not a tuple:
this_tuple = ("apple")
print("2.", type(this_tuple)) 

    # We can use len() to determine the number of elements in a tuple.
this_tuple = ("apple", "banana", "cherry")
print("3.", len(this_tuple))

    # Using type on a tuple will return <class 'tuple'>:
print("4.", type(this_tuple))

    # We can also use the tuple() constructor to convert other data types into tuples:
this_tuple = tuple(["apple", "banana", "cherry"])
print("5.", this_tuple)


# ACCESSING ELEMENTS
    # As with lists, we can index tuples the same way:
this_tuple = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("6.", this_tuple[1])

    # We can also check if an item is contained in a tuple using the in operator:
this_tuple = ["apple", "banana", "cherry"]
print("7.", "apple" in this_tuple)


# ADDING ELEMENTS
    # While tuples are immutable, we can still join tuples together:
this_tuple = ("apple", "banana", "cherry")
other_tuple = ("orange",)
this_tuple += other_tuple
print("8.", this_tuple)


# DELETING TUPLES
    # We cannot remove elements from a tuple, we can only delete the whole thing:
this_tuple = ("apple", "banana", "cherry")
del this_tuple


# UNPACKING TUPLES
    # One of the most common uses of tuples is packing and unpacking several variables together:
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print("9.", green)
print("10.", yellow)
print("11.", red)

    # We can use * to unpack as many values as necessary, and _ as a placeholder:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry", "cabbage")
green, *tropic, red, _ = fruits     # NOTE: The () brackets of the tuple are implicit here.
print("12.", green)
print("13.", tropic)
print("14.", red)


# LOOPING THROUGH TUPLES
    # Like lists, we can loop through tuples with a for loop:
this_tuple = ("apple", "banana", "cherry")
for x in this_tuple:
  print("15.", x)

    # We can also perform tuple comprehension:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_tuple = (x for x in fruits if "a" in x)
print("16.", new_tuple)


# JOINING TUPLES:
    # As discussed, we can join tuples with the + operator.
    # We can also duplicate a tuple's contents:
fruits = ("apple", "banana", "cherry")
my_tuple = fruits * 2
print("17.", my_tuple)
