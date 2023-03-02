#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re
txt = input("Enter a text: ")
if re.search("ab[2-3]?", txt):
    print("Match is found:", re.search("ab{2,3}", txt))
else:
    print("No match is found")
