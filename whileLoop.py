
ch = 0
n = 0
i = 2
while True:
    print('1-Factor\n2-Factorial\n3-Prime\n4-Fibbo\n5-armstrong\n6-exit : ')
    ch = int(input("Enter Your Choice : "))
    if ch == 1:
        n = int(input("Enter any no : "))
        print("Factor of ",n," are : ")
        i=2
        while(i<=n/2):
            if n%i == 0:
                print("\t",i,end=" ")
            i=i+1

    if ch == 2:
        n = int(input("Enter any no : "))
        i=1
        fact = 1
        while i<=n:
            fact = fact*i;
            i=i+1
        print("Factorial of ",n,"is : ",fact)

    if ch == 3:


    if ch == 6:
        break;

print("Thank You.!")


