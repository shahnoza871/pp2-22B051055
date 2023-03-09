#Write a Python program to list only directories, files and all directories, files in a specified path.
import os
path = input("Enter a path: ")
obj = os.listdir(path)
for x in obj:
    dir = os.path.join(path, x)
    if os.path.isdir(dir):
        print(x)