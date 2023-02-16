#ex1
i = 1
while i<=10:
    print(i)
    i+=1

    #ex2
i=1
while i<10:
    print(i)
    if i == 5:
        break
    i+=1

#ex3
i = 0
while i<=9:
    i+=1
    if i == 2:
        continue
    print(i)

#ex4
i=1
while i<10:
    print(i)
    i+=1
else:
    print('i is no longer less than 10')
