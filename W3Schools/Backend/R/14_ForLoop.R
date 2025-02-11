
# R: W3Schools - Main Tutorial
# Section 14: For Loop

# For loops are used to iterate over a sequence of elements:
for (x in 1:10) {
  print(x)
}


fruits <- list("apple", "banana", "cherry")

# We can use a for loop to iterate over elements in a list:
for (x in fruits) {
  if (x == "cherry") {
    break
  }
  print(x)
}
