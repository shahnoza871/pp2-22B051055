# Write a Python program to find sequences of lowercase letters joined with an underscore.
import re
txt = input("Enter a text: ")
print("All lowercase letters joined with an underscore:", re.findall("[a-z]_[a-z]", txt))
