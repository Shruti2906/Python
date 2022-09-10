from p1 import display, show, moduleWithArgument
from math import factorial

display()
show()

n=int(input("enter any no : "))
fact = factorial(n)
print("factorial of ",n,"is : ",fact)

print("\nrange : ",end=" ")
for x in range(5):
    print(x,end=" ")

print("\narray : ",end=" ")
arr = [1,2,3,4,5]
for x in arr:
    print(x,end=" ")


print("\nString Array : ",end=" ")
str = ["abc", "bcd", "cde"]
for i in str:
    print(i,end=" ")


for x in [1,2]:
    pass

no = input("\nenter no : ")
print(type(no))

print('value passd to function is : ',moduleWithArgument(10))