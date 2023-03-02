# Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re
txt = input("Enter a text: ")
print("Found:", re.findall("[A-Z]_[a-z]+", txt))