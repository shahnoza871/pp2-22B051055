# Write a Python program to test whether a given path exists or not.
# If the path exist find the filename and directory portion of the given path.
import os
path = input("Enter a path: ")
if os.access(path, os.F_OK):
    print("Exists", os.path.basename(path), os.path.dirname(path))
else:
    print("Does not exist")