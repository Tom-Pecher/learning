
# R: W3Schools - Main Tutorial
# Section 9: Strings

# Strings can be defined using single quotes or double quotes, and across multiple lines:
str <- "Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."

# To insert line breaks at the new lines in the string, we can use the cat() function:
cat(str)

# To measure the length of a string, we can use the nchar() function:
nchar(str)

# The grepl() function allows us to search for a specific string within another string:
grepl("Hello", str)

# Concatenating strings can be done using the paste() function:
str1 <- "Hello"
str2 <- "World"
paste(str1, str2)

# Escape Characters:
    # \\ 	Backslash
    # \n 	New Line
    # \r 	Carriage Return
    # \t 	Tab
    # \b 	Backspace
    