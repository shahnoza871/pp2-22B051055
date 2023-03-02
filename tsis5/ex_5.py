# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re
txt = input("Enter a text: ")
print(re.search("a.*b$", txt))