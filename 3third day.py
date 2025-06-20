"""

class Run:
    def __init__(self,km,m):
        self.km=km + m //1000
        self.m = m%1000
    def __add__(self,other):
        total_km = self.km + other.km
        total_m = self.m + other.m
        if total_m >= 1000:
            total_km = total_km + total_m // 1000
            total_m = total_m % 1000
            return Run(total_km,total_m)
    def __repr__(self):
        return f"{self.km} km and {self.m} m"
fun1 = Run(2,23222)
fun2 = Run(4,232)
fun3 = Run(5,2002)
print(fun1)
print(fun2)
print(fun3)


"""
from enum import nonmember

"""
class Person:
    def __new__(cls,name,age):
        if age <18 :
            print("GROW UP")
            return None
        print("Creat object")
        return object.__new__(cls)
    def __init__(self,name,age):
        print("Initiali object")
        self.name=name
        self.age=age

    def display(self):
        return f"The name of the person is {self.name} and age is {self.age}"

p1 = Person("Mohit",23)
if p1:
    print(p1.display())

p2 = Person("Ankit",7)
if p2:
    print(p2.display())

"""


"""

class Box:
    def __init__(self,item):
        self.item=item

    def __add__(self,other):
        return Box(self.item + other.item)

    def display(self):
        return f"Box contains: {self.item}"

box1 = Box(["Apple","Banana"])

box2 = Box(["Orange","Grape"])

box3 = box1+box2
print(box3.display())

"""
"""
class Person:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return f"Person{self.name}"
class Greeting:
    def generate_greeting(self,name):
        return f"Hello,{person.name}"
person = Person("Alice")
greeting = Greeting()
message = greeting.generate_greeting(person)
print(message)


"""
"""
class Rectangle:
    def init_(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width" self.height
    def combine(self, other):
# Combine areas of Ewo pectangtes
        new_area self.area() + other.area()
# Create a new rectangle with the combined aned
#For simplicity, let's assume the width of the new rectongle is the some us the first rectongle
#and we calcuite the new height accordingty.
        new_width = self.width
        new_height = new_anea / new_width
        return Rectangle(new_width, new_height)
    def _str_(self):
        return f Rectangle({self.width], {self,height})"
rect1 = Rectangle(4, 5)
rect2 = Rectangle(3, 6)
combined_rect= rect1.combine(rect2)
print(combined_rect)

my_function()
print(x)

#Local namespace
def my_function():
    x = 5 #X IS LOCAL VARIABLE
    print(x)
my_function()
print(x)

"""
"""
#encLosing namespace
def outer_function():
    x = 20
    def inner_function():
#x =30
        print(x) # Accessing variable from the enclosing(outer namespace)
    inner_function()
outer_function()
"""
"""
x = 50
def my_function():
    print(x)
my_function()
print(x)

"""






