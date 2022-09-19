
class Employee:
     def accept(self):
         self.eid=int(input("Enter Employee Id : "))
         self.ename = input("Enter employee name : ")
         self.salary = input("Enter Employee Salary : ")

     def display(self):
         print("Employee id : ",self.eid)
         print("Employee Name : ",self.ename)
         print("Employee Salary : ",self.salary)

     def search(self, id):
         for x in range(len(emplst)):
             e = emplst[x]
             if(id == e.eid):
                 return True;
         return False;

     def delete(self, id):
         for x in range(len(emplst)):
            e = Employee()
            if(e.search(id)):
                emplst.remove(emplst[x])
                break;

emplst = []

print("************************************ Employee Management CRUD ***************************************")

while(True):
    print("1 : Create Employee List \n2 : Display Empoyee List \n3 : Search Employee from Employee List \n4 : Delete Employee From Employee List\n5 : Insert ")
    ch = int(input("Enter Your choice : "))

    if(ch ==1 ):
        while(True):
            e = Employee()
            e.accept()
            emplst.append(e)
            i = input("Do you want to enter more Employee(y/n) : ")
            if (i == 'y' or i == 'Y' or i == "Yes" or i == "yes"):
                continue
            break;
    if(ch == 2):
        print("============================ Employee Details ============================")
        for x in range(len(emplst)):
            e = emplst[x]
            e.display()
            print("---------------------------------------------------------------------")
    if(ch == 3):
        id = int(input("Enter employee Id to Search Employee : "))
        e = Employee()
        if(e.search(id)):
            print("---------------------------------------------------------------------")
            print("Employee Found")
            print("---------------------------------------------------------------------")
        else:
            print("---------------------------------------------------------------------")
            print("Employee Not Found ..!!")
            print("---------------------------------------------------------------------")
    if(ch == 4):
        id = int(input("Enter Employee Id to Delete Employee : "))
        e = Employee()
        if(e.search(id)):
            e.delete(id)
            print("---------------------------------------------------------------------")
            print("Employee Delted.!!")
            print("---------------------------------------------------------------------")
        else:
            print("---------------------------------------------------------------------")
            print("Sry ..Cannot Proceed Furthur..\nEmployee does not exist.!!")
            print("---------------------------------------------------------------------")
    if(ch == 5):
        e = Employee()
        e.accept()
        emplst.append(e)
        print("---------------------------------------------------------------------")
        print("Employee Inserted..!!")
        print("---------------------------------------------------------------------")

    i = input("Do you want to continue (y/n) : ")
    if (i == 'y' or i == 'Y' or i == "Yes" or i == "yes"):
        continue
    break;

print("Thank You ..!!")

