

# PYTHON: W3Schools - Tutorial
# Section 4: Deleting Files

# BASICS
f = open("demofile.txt", "w")
f.close()

    # To delete files, we must import the OS module and run the os.remove(path) method:
import os
os.remove("demofile.txt") 

    # To prevent a FileNotFound error, we can check if the path exists using os.exists(path):
import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt") 
else:
  print("1.", "The file does not exist") 


# FOLDERS
    # To create a folder we use os.mkdir(path):
if not os.path.exists("demo_folder"):
    os.mkdir("demo_folder")
else:
  print("2.", "The path already exists.") 

    # Likewise, we can delete a folder using os.rmdir(path):
os.rmdir("demo_folder")
