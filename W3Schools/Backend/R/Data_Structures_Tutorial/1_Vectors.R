
# R: W3Schools - Data Structures Tutorial
# Section 1: Vectors

# A vector in R is a collection of elements of the same data type, denoted with c():
fruits <- c("banana", "apple", "orange", "mango", "lemon")
print(fruits)

# We can get the length of a vector with the length() function:
print(length(fruits))

# We can also sort a vector with the sort() function:
print(sort(fruits))

# To access specific elements, we can refer to their, index (unlike most languages R indices start at 1):
print(fruits[1])

# We can also access multiple elements by providing a vector of indices:
print(fruits[c(1, 3)])

# The last elements can be accessed with negative indices:
print(fruits[-1])

# Change their elements:
fruits[1] <- "pear"
print(fruits)

# To repeat elements in a vector we can use the rep() function:
repeat_each <- rep(c(1,2,3), each = 3)
print(repeat_each )

# If instead we with to repeat the entire vector we can use the times parameter:
repeat_times <- rep(c(1,2,3), times = 3)
print(repeat_times)

# We can also create sequences of numbers:
numbers <- 1:10
print(numbers)

# We can also create more complicated sequences with the seq() function:
seq_numbers <- seq(from = 1, to = 10, by = 2)
print(seq_numbers)
