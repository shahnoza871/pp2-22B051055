# Write a Python program that invoke square root function after specific milliseconds.
from time import sleep
# from math import sqrt
num = int(input("Enter num: "))
time = int(input("Enter time: "))
sleep(time/1000)
print('Square root of', num, 'after', time, 'milliseconds is', num ** 0.5)