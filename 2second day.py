"""
d1 = {}

def fu1(name,price,quant):
    d1.update({"a":[name,price,quant]})
    print(d1)
print("Enter the products ::::")
n = str(input("Enter the name of the product : "))
p = int(input("Enter the price of the product : "))
q = int(input("Enter the quantity of the product : "))
print(fu1(n,p,q))

for i in range
    """

#filter

"""
age = [5,6,7,8,324,34,34,54,5432,32,23,21323,7]
def fu1(age):
    if age > 18:
        return True
    else :
        return False
adults = filter(fu1,age)
for x in adults:
    print(x,end=",")

"""
"""
age = [784,78,74,29,2,3,42,23,4,5,52]
adult = list(filter(lambda x: x>30,age))
print(adult)

"""
"""
from functools import reduce
num = [784,78,74,29,2,3,42,23,4,5,52]
sum = reduce (lambda x,y: x+y,num)
print(sum)
"""
"""
class greeting:
    message = "hi"

    def say(self):
        print(self.message)

greet = greeting()
greet.say()

"""

"""
class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def show_details(self):
        print(f"Name is {self.name},Age is {self.age},Gender is {self.gender}")
person=Person("abc",12,"M")
person.show_details()

"""

"""
class Employee:
    office_name = "ABC Corpration"
    def __init__(self,name,designation):
        self.name=name
        self.designation=designation
    def show_detail(self):
        print(F"Company name: {Employee.office_name}\n Name: {self.name}\n Designation: {self.designation}")
emp1 = Employee("Mohit","Designation")
emp1.show_detail()

"""
"""
class MathOperations:
    @staticmethod
    def add_nembers(a,b):
        return a+b
    @staticmethod
    def subtract_numbers(a,b):
        return a-b
obj = MathOperations()
result_add=MathOperations.add_nembers(10,5)
result_subtract = obj.subtract_numbers(10,5)
print(f"Addition: {result_add}")
print(f"Subtract:{result_subtract}")

"""
"""
class Student:
    def __init__(self):
        print("This is the default construct")
    def show(self,name):
        print("Hello",name)

print(Student)

"""
"""
class Addition:
    first= 0
    second = 0
    answer = 0
    def __init__(self,f,s):
        self.first = f
        self.second = s
    def display(self):
        print("FI")



"""
"""
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

person = Person("Alice",)

"""