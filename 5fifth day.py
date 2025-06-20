"""
def decor(Fuc1):
    def Inner():
        print("___---___")
        Fuc1()
        print("---___---")
    return Inner()





def msg():
    print("HELLO!!!")
msg = decor(msg)
print(msg)

"""

"""
d1 = {1:"Hello",2:"yo",3:"[hd]"}
print(d1)
print(d1[3])
print(type(d1[3]))

"""
"""
#Decorating Functions with Parameters
def do_twice(func):
    def wrapper_do_twice(*args, ** kargs):
        func(*args, ** kargs)
        func(*args, ** kargs)
    return wrapper_do_twice

@do_twice
def message(name, age, address):
    print(f"Hello {name} {age} {address}")
    
message("Mohit", 25, "Noida")I

"""
"""
#Apply Multiple Decorators to a Function
def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner
def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner

@decor1
@decor
def num(): #first decor and then decor1
    return 10
print(num())
"""

"""
def generator():
    yield"Hello"
    yield"World"

gen = generator()
print(next(gen))
print(next(gen))

"""

"""
def generate_numbers():
    for num in range(1, 11):
        yield num

numbers_generator = generate_numbers()
print(type(numbers_generator))

for number in numbers_generator:
    print(number)
"""
"""
for i in range(1,11):
    print(i)

"""
"""
def rev_str(my_str):
    length = len(my_str)
    for i in range(length -1,-1,-1):
        yield my_str[i]
for char in rev_str("HSDFGHJDFGHJDFGHJ"):
    print(char)
"""
floor =[1,2,3,4,5]
lift = iter(floor)
print(next(lift))
print(next(lift))
print(next(lift))
print(next(lift))




























