#1 Define a class which has at least two methods: getString.
"""class string:
    def getString(self):
        self.s = str(input())
    def printString(self):
        print(self.s.upper())
ans = string()
ans.getString()
ans.printString()
"""
#2 Define a class named Shape and its subclass Square.
"""class Shape:
    def __init__(self, length):
        self.length = length
    def area(self):
        print(0)
class Square(Shape):
    def area(self):
        print(self.length * self.length)
c = Shape(5)
c.area()
c = Square(5)
c.area()"""
#3 Define a class named Rectangle which inherits from Shape class from task 2.
"""class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width
class Rectangle(Shape):
    def area(self):
        a = self.length * self.width
        print(a)
m = Rectangle(5,4)
m.area()
"""
#4 Write the definition of a Point class.
"""class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, end = " ")
        print(self.y)
    def move(self,x1,y1):
        self.x += x1
        self.y += y1
        print(self.x, end = " ")
        print(self.y)
    def dist(self,Point):
        print(abs(Point.x - self.x), end = " ")
        print(abs(Point.y - self.y))
p1 = Point(3,4)
p2 = Point(1,1)
p1.show()
p1.move(2,2)
p1.dist(p2)
"""
#5 Create a bank account class that has attributes owner, balance and two methods deposit and withdraw.
"""class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,money):
        self.balance += money
    def withdraw(self,money):
        self.balance -= money
        if self.balance < 0:
            print("You haven't enough money")
        else:
            print(self.balance)
a = Account("Abylaikhan",5000)
a.deposit(3000)
a.withdraw(6000)
"""
#6 Write a program which can filter prime numbers in a list by using filter function.
"""def Prime(x):
    for i in range(2, x - 1):
        if x % i == 0:
            return False
    return True
class List():
    def __init__(self,arr):
        self.arr = arr
    def filtering(self):
        return list(filter(lambda x : Prime(x), self.arr))
l = List([2,3,4,5,6,7,8,9,10,11,12,13])
print(l.filtering())
"""
