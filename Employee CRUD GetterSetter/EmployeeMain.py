from EmployeeInfo import EmployeeInfo

empinfo = EmployeeInfo()

print("\n\n\n**************************** Employee Management CRUD ******************************")

while True:
    print("==================================== Main Menu =====================================")
    ch = int(input("\t\t\t1 : create \n\t\t\t2 : Display \n\t\t\t3 : Search\n\t\t\t4 : Delete\n\t\t\t5 : Insert"))
    if ch == 1:
        lst = empinfo.accept()

    elif ch == 2:
        if(len(lst) > 0):
            empinfo.display(lst)
        else:
            print("-----------------------------------------------------------------------")
            print("\t\tNo Record Found..!!")
            print("-----------------------------------------------------------------------")

    elif ch == 3:
        id = int(input("\t\tEnter Employee Id : "))
        e = empinfo.search(lst, id)
        if(e != None):
            print("-----------------------------------------------------------------------")
            print("\t\tEmployee Found..!!")
            print("-----------------------------------------------------------------------")
        else:
            print("-----------------------------------------------------------------------")
            print("\t\tEmployee NOT Found..!!")
            print("-----------------------------------------------------------------------")

    elif ch == 4:
        id = int(input("\t\tEnter Employee Id : "))
        empinfo.delete(lst, id)

    elif ch == 5:
        lst = empinfo.insert(lst)

    else:
        print("-----------------------------------------------------------------------")
        print("\t\tInvalid Choice..!!")
        print("-----------------------------------------------------------------------")

    chh = input("\t\tDo you want to go to Main Menu?(y/n) : ")
    if(chh=='y' or chh=="Y" or chh=="Yes" or chh=="Yes" or chh=="YES"):
        continue
    break;

print("------------------------------------------------------------------------")
print("------------------------------------------------------------------------")
print("\t\t\t\tThank You ..!!")
print("------------------------------------------------------------------------")