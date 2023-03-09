# Write a Python program to count the number of lines in a text file.
import os
path = input("Enter the path of your file: ")
file = open(path, "r")
numL = len(file.readlines())
print(numL)
