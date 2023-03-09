# Write a Python program to write a list to a file.
import os
import json

fruits = ['banana', 'apple', 'orange']
str_fruits = json.dumps(fruits)

file = input("Enter a path to your file: ")

f = open(file, 'a')
f.write(str_fruits)
f.close()

print(open(file, 'r').read())