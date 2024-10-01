
# PYTHON: W3Schools - File Handling Tutorial
# Section 2: Reading Files

# BASICS
    # We can use the file.read() function to read all contents from a file object:
f = open("test_file_1.txt", "r")
print("1.", f.read()) 

    # We can specify to read a certain number of characters:
f = open("test_file_1.txt", "r")
print("2.", f.read(6)) 

    # We can also read a file line by line:
f = open("test_file_1.txt", "r")
print("3.", f.readline())

    # Using a for loop on a file object will iterate through the lines:
f = open("test_file_1.txt", "r")
for x in f:
  print("4.", x)

    # Again, we must always remeber to close the file object once it is no longer needed:
f.close()