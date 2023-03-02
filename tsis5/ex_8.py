# Write a Python program to split a string at uppercase letters.
import re
txt = input()
result = re.split('[A-Z]', txt)
print(result)