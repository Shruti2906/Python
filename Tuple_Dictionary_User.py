
menu = ("veg", "nonveg", "starter")

tuple = ()

lst1 = []
lst2 = []

tuple = (lst1, lst2)
lst1.append(10)
lst1.append(20)
lst1.append(30)

lst2.append(30)
lst2.append(20)
lst2.append(10)

print(tuple[0])
print(tuple[1])

#lst1.append(input('enter list item : '))

print("enter list 5 items : ")
for i in range(5):
    lst1.append(input());

print(tuple, end=" ")