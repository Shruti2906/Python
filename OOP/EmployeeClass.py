
class Employee:
    def accept(self):
        self.eid=int(input("enter employee id : "))
        self.ename=input("enter employee name : ")
        self.salary=float(input("enter employee salary : "))

    def display(self):
        print("employee id : ",self.eid)
        print("Employee name : ",self.ename)
        print("employee salary : ",self.salary)

e=Employee()
e.accept()
e.display()