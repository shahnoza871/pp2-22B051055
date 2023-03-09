# Write a Python program to copy the contents of a file to another file
import os
import json

f1 = open("C:\\Users\\DELL\\Desktop\\demo1.txt", "r")

f2 = open("C:\\Users\\DELL\\Desktop\\demo2.txt", "a")
f2.write(f1.read())
f2.close()

print(open("C:\\Users\\DELL\\Desktop\\demo2.txt", "r").read())