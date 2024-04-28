
# PYTHON: W3Schools - Main Tutorial
# Section 17: While Loops

# BASICS
    # While loops will execute their code so long as their condition is met:
i = 1
while i < 6:
  print("1.", i)
  i += 1


# STATEMENTS
    # The break statement immediately exits the loop:
i = 1
while i < 6:
  print("2.", i)
  if i == 3:
    break
  i += 1 

    # The continue statement skips one iteration of the loop:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print("3.", i)

    # We can add an else statement to the while loop: this will execute its code once the while loop's condition is broken:
i = 1
while i < 6:
  print("4.", i)
  i += 1
else:
  print("5.", "i is no longer less than 6")
