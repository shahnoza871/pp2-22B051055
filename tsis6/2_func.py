# Write a Python program with builtin function that accepts a string
# and calculate the number of upper case letters and lower case letters
a = input()
l = 0
u = 0
for i in a:
    if(i.islower()):
        l +=1
    else:
        u+=1
print("lowercase:", l, "uppercase:", u)