
name = (input('Enter Student Name : '))
rollNo = int(input('Enter Student Roll No : '))
sub1 = int(input('Enter Mark for subject 1 : '))
sub2 = int(input('Enter Mark for Subject 2 : '))
sub3 = int(input('Enter Mark for subject 3 : '))

total = sub1+sub2+sub3;
avg = total/3
perc = (total/300)*100;

print('\n\n')
print('Name of Student\t\t\t\t:\t\t',name)
print('RollNo of Student\t\t\t:\t\t',rollNo)
print('marks of 3 subjects are\t\t:\t\t',sub1,sub2,sub3)
print('Total is\t\t\t\t\t:\t\t',total)
print('Average\t\t\t\t\t\t:\t\t',avg)
print('Percentage is\t\t\t\t\t:\t\t',round(perc),'%')

print("Type of rollNo : ",type(rollNo))
print("Type of Name : ",type(name))

if sub1>=40 and sub2>=40 and sub3>=40:
    print('Result\t\t:\t\tPASS')

    if perc>=40 and perc<=70:
        print('Grade : C')
    elif perc>=70 and perc<85:
        print('Grade : B')
    else:
        print('Grade : A')


