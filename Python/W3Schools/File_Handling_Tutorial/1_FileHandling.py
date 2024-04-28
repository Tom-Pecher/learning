
# PYTHON: W3Schools - File Handling Tutorial
# Section 1: File Handling

# BASICS
    # The main way of interacting with files in Python is with the open() method:
f = open("test_file_1.txt")

    # The open() method takes as input the filename and a mode
f = open("test_file_1.txt", "rt")

    # Once we are finished with a file, we must remember to close it using file.close():
f.close()

# MODES
    # Permission:
        #  "r" -  Read    - Default value. Opens a file for reading, error if the file does not exist
        #  "a" -  Append  - Opens a file for appending, creates the file if it does not exist
        #  "w" -  Write   - Opens a file for writing, creates the file if it does not exist
        #  "x" -  Create  - Creates the specified file, returns an error if the file exists

    # Format:
        #  "t" -  Text    - Default value. Text mode
        #  "b" -  Binary  - Binary mode (e.g. images)
