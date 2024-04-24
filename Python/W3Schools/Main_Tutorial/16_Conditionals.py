
# PYTHON: W3Schools - Tutorial
# Section 16: Conditionals

# BASICS
    # Like other programming languages, Python has three main conditional statements:
a = 200
b = 33
if b > a:
  print("1.", "b is greater than a")  # Executes if statement 1 is true
elif a == b:
  print("2.", "a and b are equal")    # Executes if statement 1 is false and statement 2 is true
else:
  print("3.", "a is greater than b")  # Executes otherwise


# SHORTHAND
    # We can write a single if statement on one line like so:
if a > b: print("4.", "a is greater than b")

    # We can write if-else statements on one line also (sometimes referred to as a ternary operator):
a = 2
b = 330
print("5.", "A") if a > b else print("6.", "B")

    # These can be chained together
a = 330
b = 330
print("7.", "A") if a > b else print("8.", "=") if a == b else print("9.", "B")

    # We can, of course, nest conditional statements:
x = 41
if x > 10:
  print("8.", "Above ten,")
  if x > 20:
    print("9.", "and also above 20!")
  else:
    print("10.", "but not above 20.") 

# Conditional statements cannot be left empty: they can be filled with the pass keyword will perform no action:
a = 33
b = 200
if b > a:
  pass


# OPERATORS
    # The and operator returns true only if the boolean expressions either side are both true:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("11.", "Both conditions are True")

    # The or operator returns true if at least one of the boolean expressions either side is true:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("12.", "At least one of the conditions is True")

    # The not operator inverts the boolean expression to the right:
a = 33
b = 200
if not a > b:
  print("13.", "a is NOT greater than b")
