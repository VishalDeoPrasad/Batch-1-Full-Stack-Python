import os

try:
    os.rename("demo.txt", "tech.txt") 

except OSError:
    print("Cannot renamed! maybe file not found!")