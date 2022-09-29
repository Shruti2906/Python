from CustomerInfo import CustomerInfo

custInfo = CustomerInfo()

print("\n\n\n**************************** Customer Management CRUD ******************************")

while True:
    print("==================================== Main Menu =====================================")
    ch = int(input("\t\t\t1 : create \n\t\t\t2 : Display \n\t\t\t3 : Search\n\t\t\t4 : Delete\n\t\t\t5 : Insert\n\t\t\t6 : Transaction"))
    if ch == 1:
        lst = custInfo.accept()

    elif ch == 2:
        if(len(lst) > 0):
            custInfo.display(lst)
        else:
            print("-----------------------------------------------------------------------")
            print("\t\tNo Record Found..!!")
            print("-----------------------------------------------------------------------")

    elif ch == 3:
        id = int(input("\t\tEnter Customer Id : "))
        e = custInfo.search(lst, id)
        if(e != None):
            print("-----------------------------------------------------------------------")
            print("\t\tCustomer Found..!!")
            print("-----------------------------------------------------------------------")
        else:
            print("-----------------------------------------------------------------------")
            print("\t\tCustomer NOT Found..!!")
            print("-----------------------------------------------------------------------")

    elif ch == 4:
        id = int(input("\t\tEnter Customer Id : "))
        custInfo.delete(lst, id)

    elif ch == 5:
        lst = custInfo.insert(lst)

    elif ch==6:
        id = int(input("\t\tEnter Customer Id : "))
        custInfo.tracsactions(lst, id)

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