#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re
txt = input("Enter any text: ")
result1 = re.search("ab", txt)
result2 = re.search("a0", txt)
if re.search("ab", txt):
    print("Match found:", result1)
elif re.search("a0", txt):
    print("Match found:", result2)
else:
    print("No match found")