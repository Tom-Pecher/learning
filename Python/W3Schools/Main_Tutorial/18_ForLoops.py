
# PYTHON: W3Schools - Main Tutorial
# Section 18: For Loops

# BASICS
    # The for loop iterates through all items in a collection:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print("1.", x)

    # Since strings also count as collections, we can also loop through each of their characters:
for x in "banana":
  print("2.", x)


# STATEMENTS
    # The same three statements discussed for while loops work the same with for loops.
    # break:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print("3.", x)
  if x == "banana":
    break

    # continue:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print("4.", x)

    # else:
for x in range(6):
  print("5.", x)
else:
  print("6.", "Finally finished!")

    # The for loop is most commonly associated with the builtin range() constructor:
for x in range(2, 30, 3):
  print("7.", x)
