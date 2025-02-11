
# R: W3Schools - Data Structures Tutorial
# Section 2: Lists

# A list is a collection of values which may be of different types:
thislist <- list("apple", 2, FALSE)
print(thislist)

# Like vectors, we can index them:
print(thislist[1])

# And modify them:
thislist[1] <- "blackcurrant"
print(thislist[1])

# And obtain the length of the list:
print(length(thislist))

# We can check if an item exists in the list:
print("apple" %in% thislist)

# Add elements to the list:
append(thislist, "orange")
print(length(thislist))

# Remove element from list:
thislist <- thislist[-1]
print(thislist)

# Join two lists:
list1 <- list("a", "b", "c")
list2 <- list(1,2,3)
list3 <- c(list1,list2)

print(list3)
