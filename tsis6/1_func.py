import math
l = input("Enter numbers: ")
li = []
for x in l:
    li.append(int(x))
r = math.prod(li)
print(r)