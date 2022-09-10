#[] is for list
#() is for tuple
#{} is for set

#same as dynamic array in other language like vectors

marks = [100, 98, 88, 65, 73, 90, "math"]
print(marks)

#list in mutable
#e.g marks = [100]  is valid

print("marks[1] : ",marks[1])
print("marks[-1] : ",marks[-1])
print("marks[-1] : ",marks[-5]) #cannot go beyound -5 here as size is 5
print("marks[1:3] : ",marks[1:3])   #print list elements starting from 1 exclusive 3

#remove elements from marks fom index 0 to 2 (2 exclusive)
marks[0:2]= []
print("marks[0:2]= []",marks)

marks[0:2]= [98, 88]
print("marks[0:2]= [98, 88]",marks)

print("marks[: 3] = ",marks[: 3])   #from index 0 to 2
print("marks[0: ] = ",marks[0: ])   #from index 0 to end
print("marks[: ] = ",marks[: ])   #from index 0 to end (whole list)

print("print the elements of marks from certain to certain index..")
print(marks[0: 3])  #from index zero till 2 (3 exclusive)


#append function to add values to list
print("append 102 i.e add at end in the list")

marks.append(102)
print(marks)

#appends more than one value at one time use extends and []
#marks.append([10, 20]) it will andd 10 and 20 as onve value pair [10, 20]
marks.extend([89, 67])
print("append more than one value marks.extend(89, 67): ",marks)
print("index of element 88 : "+str(marks.index(88)))
print("insert 45 at index 1")
marks.insert(1, 45)
print(marks)


#pop function
print("marks.pop() : ",marks.pop())
print("marks.pop(2) : ",marks.pop(2))

#marks.sort()   //#it is not valid now as list cotains both int and str values
marks.remove('math')
marks.sort()
print("\n marks.sort() : ",marks)

print("98 present in marks : "+str(98 in marks))

print("Length of marks : "+str(len(marks)))

print("Elements of marks using while loop : ")
i=0
while i < len(marks):
    print(marks[i])
    i += 1

#we can store tuples, lists , sets in list
l = [{10,20}, {30,40}]
print(l)
print(type(l[0]))


print("delete list or list items using \"del\" keyword")
del marks[2]
print("after del marks[2] : ",marks)

marks.clear()
print("marks after clear : ")
print(marks)

#2d list
ll = [[10,20], [50, 30, 40]]
print(ll)
print(ll[0][1])
print(ll[1][0])

str = input("enter any strings : ")
print(str)
strLst = str.split("a")
print(strLst)
strLst = str.split()
print(strLst)

print(strLst[::-1])
