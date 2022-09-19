
class Employee:
    def accept(self):
        self.eid=int(input("enter employee id : "))
        self.ename=input("enter employee name : ")
        self.salary=float(input("enter employee salary : "))

    def display(self):
        print("employee id : ",self.eid)
        print("Employee name : ",self.ename)
        print("employee salary : ",self.salary)

list = []
while(True):
    e=Employee()
    e.accept()
    list.append(e)
    i = input("Do you want to continue(Y/N) : ")
   # if(i !='y' ):
    #    break;
    if(i == 'y' or i=='Y' or i=="yes"):
        continue
    break;

print("-----------------------------------------------------------------------")

for x in range(len(list)):
    e = list[x]
    e.display()
    print("-----------------------------------------------------------------------")

print("Thank You ..!!")
