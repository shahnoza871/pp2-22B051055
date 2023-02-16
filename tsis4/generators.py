#1 Create a generator that generates the squares of numbers up to some number N.
"""import math
def generator(n):
    i = 1
    while i<=int(n):
        yield pow(i, 2)
        i += 1
N = input('Enter a number: ')
x = generator(N)
j = 1
while j<=int(N):
    print(next(x))
    j+=1"""
#2 Write a program using generator to print the even numbers between 0 and N in comma separated form.
"""def generator(n):
    i = 1
    while i<=int(n):
        if i>1 and i%2 == 0:
            yield i
        i += 1
N = input("Enter a number: ")
x = generator(N)
j = 0
while j<int(N)/2:
    print(next(x))
    j+=1"""
#3 Define a function with a generator which can iterate the numbers,
# which are divisible by 3 and 4, between a given range 0 and n.


