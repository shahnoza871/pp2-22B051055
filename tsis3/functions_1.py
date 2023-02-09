#1 Create a function to convert grams to ounces. ounces = 28.3495231 * grams:
"""def gto(x):
    y = int(x)*28.3495231
    return(y)
a = input(How many grams? )
print(gto(a))
"""
#2  Calculate and display the equivalent centigrade temperature.
# The following formula is used for the conversion: C = (5 / 9) * (F – 32)
"""def temp(f):
    c = (5/9)*(int(f) - 32)
    print(c)
x = input('Enter the temperature: ')
temp(x)
"""
#3 We count 35 heads and 94 legs among the chickens and rabbits in a farm.
# How many rabbits and how many chickens do we have?
"""def solve(numheads, numlegs):
    numrabbits = (int(numlegs) - 2*int(numheads))/2
    numchicken = int(numheads) - int(numrabbits)
    print(int(numrabbits), int(numchicken))
x = input('Enter number of heads: ')
y = input("Enter number of legs: ")
solve(x, y)
"""
#4 Write a function filter_prime which will take list of numbers as an agrument
# and returns only prime numbers from the list.
"""def filter_prime(num):
    numbers = []
    for i in num:
        prime = True
        if int(i) < 2:
            continue
        for j in range(2, int(i) - 1):
            if int(i) % j == 0:
                prime = False
        if prime == True:
            numbers.append(int(i))
    return numbers
x = input("Enter numbers: ").split()
print(filter_prime(x))
"""
#5 Write a function that accepts string from user and print all permutations of that string.
"""from itertools import permutations
s1 = str(input("Enter a string: "))
s2 = permutations(s1)
for x in s2:
    print(x)
"""
#6 Write a function that accepts string from user, return a sentence with the words reversed.

#7 Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
"""def has_33(numbers):
    for x in range(0, len(numbers) - 1):
        if numbers[x] == 3 and numbers[x + 1] == 3:
            return True
    return False
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
"""
#8 Write a function that takes in a list of integers and returns True if it contains 007 in order
"""def spy_game(numbers):
    cntr = 0
    for x in range(0, len(numbers)):
        if numbers[x] == 0:
            cntr += 1
        if cntr >= 2 and numbers[x] == 7:
            return True
    return False
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
"""
#9 Write a function that computes the volume of a sphere given its radius.
"""import math
def volume():
    r = float(input())
    v = 4 / 3 * math.pi * r * r * r
    return v
print(volume())
"""
#10 Write a Python function that takes a list and returns a new list with unique elements of the first list.
"""l = input("Enter numbers: ").split()
def fUnique(l):
    d = {}
    myList = []
    for x in l:
        if x not in d.keys():
            d[x] = 1
    for x in d.keys():
        myList.append(x)
    return myList
print(fUnique(l))
"""
#11 Write a Python function that checks whether a word or phrase is palindrome or not.
"""s = input("Enter a word/sequence of numbers: ")
def ispalindrome():
    t = s[::-1]
    if(t == s):
        return True
    return False
if ispalindrome() == True:
    print("Palindrome")
else:
    print("Not a palindrome")
"""
#12 Define a functino histogram() that takes a list of integers and prints a histogram to the screen.
"""def histogram(num):
    for x in num:
        while x > 0:
            print("*", end = "")
            x -= 1
        print('')
histogram([4, 9, 7])
"""

#13 Write a program able to play the "Guess the number" - game,
# where the number to be guessed is randomly chosen between 1 and 20.
"""import random
def check(a, name,cnt):
    m = int(input())
    cnt += 1
    if m == a:
        print("Good job,", end = " ")
        print(name, end = "")
        print("! You guessed my number in",cnt,"guesses!")
    if m < a:
        print("Your guess is too low.")
        check(a,name,cnt)
    if m > a:
        print("Your guess is too high.")
        check(a,name,cnt)
print("Hello! What is your name?")
name = str(input())
print("Well,", end = " ")
print(name, end = ",")
print(" I am thinking of a number between 1 and 20.")
print("Take a guess.")
cnt = 0
a = random.randrange(1,20)
check(a,name,cnt)
"""

