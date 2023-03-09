# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import os
import string
for letter in string.ascii_uppercase:
    file = open("C:\\Users\\DELL\\Desktop\\" + letter + ".txt", 'x')

print("Done")