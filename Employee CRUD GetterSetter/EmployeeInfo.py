from Employee1 import Employee1

class EmployeeInfo:

    def accept(self):
        lst = []
        while True:
            e = Employee1()
            e.eid = int (input("\t\t\tenter employee id : "))
            e.ename = input("\t\t\tEnter employee name : ")
            e.esal = float(input("\t\t\tEnter Employee Salary : "))
            lst.append(e)
            chh = input("\t\t\tWant to add more Employee ?(y/n) : ")
            if (chh == 'y' or chh == "Y" or chh == "Yes" or chh == "Yes" or chh == "YES"):
                continue
            break;
        return lst


    def display(self, lst):
        print("============================= Employee Details =============================")
        for x in range(len(lst)):
            e = lst[x]
            print("\t\tEmployee id : ", e.eid)
            print("\t\tEmployee Name : ", e.ename)
            print("\t\tEmployee Salary : ", e.esal)
            print("\n---------------------------------------------------------------------------")

    def search(self, lst, id):

        for x in range(len(lst)):
            e = lst[x]
            if(id == e.eid):
                return e
        return

    def delete(self, lst, id):
        e = self.search(lst, id)
        if(e != None):
          lst.remove(e)
          print("-----------------------------------------------------------------------")
          print("\t\tEmployee Deleted..!!")
          print("-----------------------------------------------------------------------")
        else:
            print("-----------------------------------------------------------------------")
            print("\t\tCannot Proceed To Delete The Record ..!\n\tEmployee does NOT Exist..!!")
            print("-----------------------------------------------------------------------")

    def insert(self, lst):
        e = Employee1()
        e.eid = int(input("\t\t\tenter employee id : "))
        e.ename = input("\t\t\tEnter employee name : ")
        e.esal = float(input("\t\t\tEnter Employee Salary : "))
        lst.append(e)
        return lst