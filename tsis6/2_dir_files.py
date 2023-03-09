# Write a Python program to check for access to a specified path. Test the existence, readability,
# writability and executability of the specified path
import os
path = input("Enter a path: ")
if os.access(path, os.F_OK):
    print('Exists')
else:
    print('DNE')
if os.access(path, os.R_OK):
    print('Readable')
else:
    print('INR')
if os.access(path, os.W_OK):
    print('Writable')
else:
    print('INW')
if os.access(path, os.X_OK):
    print("Executable")
else:
    print('INE')