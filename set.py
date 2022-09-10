#set is one of the data type in python
#[] is for list
#() is for tuple
#{} is for set

#same as list..just..
#set stores only "unique" elemnts
#it will Not follow any sequence

marks = {95, 34, 98, 98}
print(marks)

#can store tuple in set but not List and Set as they are not hashable
s = {(10,20) ,(30,40, 50)}
print(s)

print(type(s))

#set is NOT sequential....as it uses 'Hash'
#thus indexing is not supported ..as do not have index
#print (marks[i]) #invalid as there is no index in set..'set' object is not subscriptable
#thus marks[0] =10 is not valis in set

for score in marks:
    print(score)

marks.add(10)
print(marks)


#frozensets ae immutable

fset = frozenset((910, 20, 30, 40))
print(fset)
#fset[0] =10;
marks.copy()

trial = {1:"apple", 2:"Ball", 3:{5:"cat", 3:"dog"}}
print(trial)