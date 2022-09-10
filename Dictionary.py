
#keys are immutable values are mutable

dict = {1:"ram", 2:"sham", 3:"sundar"}

print(dict)
dict[1] = "radha"
print(dict)

marks = {"english": 95, "math" : 98}

print(marks)

print(marks["english"])

#print(marks[0])#key does not exist

marks["Physics"] = 98

print(marks)

marks["math"] = 80
print(marks)

trial = {}
print(type(trial))