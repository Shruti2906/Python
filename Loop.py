
#range
number = range(5)
print(number)
for x in number:
    print(x, end = " ")

i=1
while i<5:
    print(i)
    i = i+1

i=1
while i<5:
    print(i*'*')
    i=i+1

i=10
while i>=1:
    print(i, end="\t")
    i=i-1

i=1
n = int(input("\nEnter any number : "))
while i<10:
    print(n,"\t*\t",i, " = ", n*i)
    i = i+1

