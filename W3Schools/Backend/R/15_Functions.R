
# R: W3Schools - Main Tutorial
# Section 15: Functions

# A function is a piece of code that can be reused:
my_function1 <- function() { # Function definition.
  print("Hello World!")
}

my_function1() # Function call.

# We can configure our function to take input parameters:
my_function <- function(fname="Brian") { # Default value for parameter.
  return (paste(fname, "Griffin")) # And also to return output values.
}

print(my_function("Peter"))
print(my_function("Lois"))
print(my_function("Stewie"))

# One difference of R compared to other languages is that it encourages function nesting and recursion:
Nested_function <- function(x, y) {
  a <- x + y
  return(a)
}

print(Nested_function(Nested_function(2,2), Nested_function(3,3)))

# Recursion is where a function calls itself:
tri_recursion <- function(k) {
  if (k > 0) {
    result <- k + tri_recursion(k - 1)
    print(result)
  } else {
    result = 0
    return(result)
  }
}

# This recursive function computes the nth triangular number:
tri_recursion(6)

# Like other languages, variable values can only be accessed within the scope of the function:
txt <- "awesome"
my_function3 <- function() {
  txt <<- "fantastic" # To set a global variable, we use the assignment operator <<- :
  paste("R is", txt)
}

print(my_function3())
