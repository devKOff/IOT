"""

class Animal:
    name=""
    def eat(self):
        print("I can eat")
class Dog(Animal):
    def display(self):
        print("My name is ",self.name)
labrador= Dog()
labrador.name = "Rohu"
labrador.eat()
labrador.display()

"""
"""
class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        print(f"First name is {self.fname}")
class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        print("Inside Student class init")

s = Student("Mohit","Kumar")

"""

"""
class Father:
    def __init__(self):
        print("Father class constructor")
    def show_father(self):
        print("Father class constructor")
class Son(Father):
    def __init__(self):
        print("son class constructor")
    def show_son(self):
        print("son class constructor")
class Grandson(Son):
    def __init__(self):
        print("Grandson class constructor")
    def show_grand_son(self):
        print("Grandson class constructor")
g = Grandson()
g.show_son()
g.show_father()
g.show_grand_son()

"""
"""
class Computer:
    def __init__(self):
        self.maxprice = 900
    def sell(self):
        print(f"Selling price: {self.maxprice}")
    def setMaxPrice(self,price):
c = Computer()
c.sell()
c.setMaxPrice(1000)
c.sell()


"""

"""
class Student:
    _name = None
    _roll = None
    _branch = None
    def __init__(self,name,roll,branch):
        self.name = name
        self.roll = roll
        self.branch = branch
    def _displayInfo(self):
        print("Roll: ",self._roll)
        print("Branch",self._branch)
class Learn(Student):
    def __init__(self,name,roll,branch):
        Student.__init__(self,name,roll,branch)
    def displayDetails(self):
        print("Name:",self._name)
        self._displayInfo()
obj = Learn("Aditya",101203,"IOT")
obj.displayDetails()
"""
"""

from abc import ABC,abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
    def message(self):
        print("Computer is an electronic device")
class Laptop(Computer):
    def process(self):
        print("Executing Desktop")
class Desktop(Computer):
    def process(self):
        print("Executing Desktop process")
com1 = Laptop()
com2 = Desktop()
com1.process()
com2.message()
com2.process()

"""
"""
class A:
    def method(self):
        print("Method in A")
class B(A):
    def method(self):
        print("Method in B")
class C(A):
    def method(self):
        print("Method in C")
class D(B, C):
    pass
d = D()
d.method()

print(D.mro())


"""

"""
class A:
    def abc(self):
        print("From class A")
class B(A):
    def abc(self):
        print("From class B")

a=A()
b=B()
a.abc()
b.abc()
"""
"""
#Method overloading
class MyClass:
    def sum(self, a= None, b= None, c= None):
        s=0
        if a != None and b != None and c != None:
            s=a+b+c
        elif a != None and b != None:
            s = a + b
        else:
            s=a
        return s
s = MyClass()
#sum of 1 integer
print(s.sum(1))
#sum of 2 integers
print(s.sum(3, 5))
#sum of 3 integers
print(s.sum(1, 2,3))


"""
"""
#method overriding (also include pass)
class Animal:
    def speak(self):
        print("The animal makes a sound")

class Dog (Animal):
    def speak(self):
        print("The dog barks")

class Cat(Animal):
    def speak(self):
        print("The cat meows")

animal = Animal()
dog = Dog()
cat = Cat()

animal.speak()
dog. speak()
cat.speak()
"""
"""
# Immutable tuple
coordinates = (10, 20)
#Any attempt to modify will create a new tuple
coordinates[1]=30
new_coordinates = coordinates + (30,)
print(coordinates)
#Output: (10, 20)
print(new_coordinates)
#Output: (10, 20, 30)

"""
"""
def outerFunction(text):
    text = text
    def innerFunction():
        print(text)
    return innerFunction()
myFunction = outerFunction('Hey')
myFunction()

"""
"""
#closure function
def make_counter():
    count = 0 # This is the en

    def counter():
        nonlocal count # This
        count += 1
        return count

    return counter

# Create two independent counte
counter1 = make_counter()
counter2 = make_counter()

# Using the first counter
print(counter1())
print(counter1())
print(counter1())

# Using the second counter
print(counter2())
print(counter2())

# The first counter is independ
print(counter1())

"""



