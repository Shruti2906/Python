#tuple is one of the datatypes in python
#[] is for list
#() is for tuple
#{} is for set

#tuples are immutable
tup = (78, 56, 98, 98)
demo = 23, 55, 76 #valid

print(demo)

print(tup)

print(tup.count(98))
print(tup.index(98))

print("tup[0]",tup[0])
#tup[0] = 10 #cannot change value of tuple


#we can store lists, tuples and sets in tuple
m = ({10,20} ,[30,40, 50])
print(m)
print(type(m[0]))
print(type(m[1]))

#cannot append, insert..etc on tuple
#thus tuple is faster
#since we cannot change value of tuple iteration is faster in tuple