# Write a python program to convert snake case string to camel case string.
import re
txt = input()
result = re.split('_', txt)

res = []
for word in result:
    res.append(word.capitalize())

print("".join(res))