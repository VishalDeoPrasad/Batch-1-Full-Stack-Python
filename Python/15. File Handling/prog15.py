import os

if os.path.exists("demo1.txt"):
    os.remove("demo1.txt")
    print("your file is deleted!")
else:
    print("File does not exist!")