
# PYTHON: W3Schools - File Handling Tutorial
# Section 3: Writing and Creating Files

# BASICS
    # We can add to an existing file using the append permission and the file.write(text) function:
f = open("test_file_2.txt", "a")
f.write("Now the file has more content!\n")
f.write("Now the file has even more content!")

f = open("test_file_2.txt", "r")
print("1.", f.read()) 

    # To overwrite existing text we use the same function with the write permission:
f = open("test_file_2.txt", "w")
f.write("Now the file has different content!")

f = open("test_file_2.txt", "r")
print("2.", f.read()) 
f.close()
# NOTE: Both of these permissions will create the specified file if it does not already exist.
