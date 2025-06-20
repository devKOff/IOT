"""
for i in range(5):
    for j in range(i):
        print(j+1,end=" ")
    print()

"""
"""
n = int(input("enter the end number : "))
for i in range(0,n):
    if n//2==0:
        print("*");
    else:
        print("error");
"""
# prymid
"""
n = int(input("enter no of lines : "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    print("*"*(2*i-1))
"""
"""
print("HELLO world".lower())
print("HELLO world".upper())
print("HELLO world".capitalize())
print("HELLO world".title())
print("HELLO world".casefold())


"""



"""
passw = ["apple","ted"]
n = int(input("Enter the no of terms : "))
l1 = []
for i in range(0,n):

    x=input("Enter the tearm : ")
    for j in range(n-1):
        l1.append(x)        
if l1 == passw :
    print("correct")

else :
    print("ERRor")
"""
"""
d1 = {1:"bob",2:"rob",3:"stark"}
print(d1)
print(type(d1))
print(d1[1])
print(d1[2])
print(d1[3])

x = int(input("enter th term : "))
y = input("Enter the keyword : ")
if x < 4 :
    d1[x]=y
    print(d1)
else:
    print("erroR")

"""


"""
def add(a,b):

    sum = a+b
    return sum
x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))

print(add(x,y))

"""

# recursion
"""
def fac(n):
    f=1
    for i in range(1,n+1):
        f = f*i

    return f
x = int(input("Enter the number : "))
print(fac(x))

"""

# lambda function

"""

result= lambda n1,n2,n3:n1+n2+n3;

x = int(input("Enter the 1 term : "))
y = int(input("Enter the 2 term : "))
z = int(input("Enter the 3 term : "))

print("the sum of the three tearms are : ",result(x,y,z))

"""
#mapfunction


"""
def resu(a,b,c,d,e):
    ans = a+b+c+d+e
    avg = (ans/500)*100
    return avg

x = int(input("Enter your first sub marks : "))
y = int(input("Enter your second sub marks : "))
z = int(input("Enter your third sub marks : "))
p = int(input("Enter your fourth sub marks : "))
q = int(input("Enter your fifth sub marks : "))

print("your result is ",resu(x,y,z,p,q),"percent")

"""





