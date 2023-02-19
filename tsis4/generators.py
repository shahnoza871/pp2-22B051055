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
"""cntr = 0
def devisible(n):
    global cntr
    i = 0
    while i<=int(n):
        if i%3 == 0 and i%4 == 0:
            cntr += 1
            yield i
        i+=1
N = input('Enter a number: ')
x = devisible(N)
j = 0
while j < cntr:
    print(next(x))
    j+=1
"""
#4 Implement a generator called squares to yield the square of all numbers from (a) to (b).
"""import math
def square(a, b):
    for i in range(int(a), int(b)):
        yield pow(i, 2)
A = input('From: ')
B = input('To: ')
x = square(A, B)
len = int(B) - int(A)
i = 0
while i < len:
    print(next(x))
    i+=1"""

# Implement a generator that returns all numbers from (n) down to 0.
"""def funct(n):
    i = int(n)
    while i>=0:
        yield i
        i -= 1
N = input('Enter a number: ')
x = funct(N)
j = 0
while j<int(N):
    print(next(x))"""
