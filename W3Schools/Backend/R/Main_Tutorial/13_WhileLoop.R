
# R: W3Schools - Main Tutorial
# Section 13: While Loop

i <- 0

# While loops run until the condition is false:
while (TRUE) {
  i <- i + 1
  if (i == 3) { # The next keyword skips the current iteration.
    next
  }

  if (i > 5) {
    break # The break keyword stops the loop.
  }
  print(i)
} 