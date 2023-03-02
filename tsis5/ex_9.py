# Write a Python program to insert spaces between words starting with capital letters.
import re
from re import sub
txt = input()
result = re.findall('[a-zA-Z][a-z]+', txt)
print(' '.join(result))