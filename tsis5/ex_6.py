# Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re
txt = input("Enter a text: ")
result = re.sub(" ", ";", txt)
result = re.sub(",", ";", result)
result = re.sub("[.]", ";", result)
print("Result: ", result)