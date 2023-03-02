# Write a Python program to convert a given camel case string to snake case.
import re
res = []
txt = input()
result = re.findall('[a-zA-Z][a-z]+', txt)
for word in result:
    res.append(word.lower())
print("_".join(res))
