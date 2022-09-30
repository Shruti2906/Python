from Customer import Customer
from Address import Address
from OOP2.Account import Account
from OOP2.AccountTransaction import AccountTransaction


class CustomerInfo:

    def accept(self):
        lst = []
        while True:

            cid = int (input("\t\t\tenter Customer id : "))
            cname = input("\t\t\tEnter Customer name : ")
            csal = float(input("\t\t\tEnter Customer Salary : "))

            city = input("\t\t\tEnter City : ")
            state = input('\t\t\tEnter State : ')
            pin = int(input('\t\t\tEnter Pincode : '))

            accno = int(input('\t\t\tEnter Account Number : '))
            acctype = input('\t\t\tEnter Account Type : ')
            accBal = float(input("\t\t\tEnter account Balance : "))

            addr = Address(city, state, pin)

            acc = Account(accno, acctype, accBal)

            e = Customer(cid, cname, csal, addr, acc)

            lst.append(e)
            chh = input("\t\t\tWant to add more Customer ?(y/n) : ")
            if (chh == 'y' or chh == "Y" or chh == "Yes" or chh == "Yes" or chh == "YES"):
                continue
            break;
        return lst


    def display(self, lst):
        print("============================= Customer Details =============================")
        for x in range(len(lst)):
            e = lst[x]
            print(f"\t\tCustomer id\t\t\t:\t\t{e.cid}")
            print(f"\t\tCustomer Name\t\t:\t\t{e.cname}")
            print(f"\t\tCustomer Salary\t\t:\t\t{e.csal}")

            print(f"\t\tCustomer City\t\t:\t\t{e.addr._city}")
            print(f"\t\tCustomer State\t\t:\t\t{e.addr._state}")
            print(f"\t\tCustomer Pincode\t:\t\t{e.addr._pincode}")

            print(f"\t\tAccount No\t\t\t:\t\t{e.acc.accNo}")
            print(f"\t\tCustomer Type\t\t:\t\t{e.acc.accType}")
            print(f"\t\tCustomer Balance\t:\t\t{e.acc.accBal}")

            print("\n---------------------------------------------------------------------------")

    def search(self, lst, id):

        for x in range(len(lst)):
            e = lst[x]
            if(id == e.cid):
                return e
        return

    def delete(self, lst, id):
        e = self.search(lst, id)
        if(e != None):
          lst.remove(e)
          print("-----------------------------------------------------------------------")
          print("\t\tCustomer Deleted..!!")
          print("-----------------------------------------------------------------------")
        else:
            print("-----------------------------------------------------------------------")
            print("\t\tCannot Proceed To Delete The Record ..!\n\tCustomer does NOT Exist..!!")
            print("-----------------------------------------------------------------------")

    def insert(self, lst):

        cid = int(input("\t\t\tenter Customer id : "))
        cname = input("\t\t\tEnter Customer name : ")
        csal = float(input("\t\t\tEnter Customer Salary : "))
        city = input('\t\t\tEnter City : ')
        state = input("\t\t\tEnter state : ")
        pincode = int(input("\t\t\tEnter pincode : "))
        accno = int(input('\t\t\tEnter Account Number : '))
        acctype = input('\t\t\tEnter Account Type : ')
        accBal = float(input("\t\t\tEnter account Balance : "))

        acc = Account(accno, acctype, accBal)
        addr = Address(city, state, pincode)
        e = Customer(cid, cname, csal, addr, acc)

        lst.append(e)
        return lst

    def tracsactions(self, lst, id):

        e = self.search(lst, id)
        if (e != None):

                acctrans = AccountTransaction(e, id)

                ch = int(input("\n\t\t\t1 : Deposit\t\t2 : Withdraw\t"))
                if(ch == 1):
                    amt = float(input('Enter Amount to deposit : '))
                    if (amt > 0):
                        acctrans.deposit(amt)
                        print("-----------------------------------------------------------------------")
                        print("\t\tAmount Deposited Successfully..!!")
                        print("-----------------------------------------------------------------------")
                    else:
                        print("-----------------------------------------------------------------------")
                        print("\t\tInvalid Amount..Transaction Failed..!!")
                        print("-----------------------------------------------------------------------")

                elif(ch == 2):
                    amt = float(input('Enter Amount to Withdraw : '))
                    if (amt > 0):
                        acctrans.withdraw(amt)

                    else:
                        print("-----------------------------------------------------------------------")
                        print("\t\tInvalid Amount..Transaction Failed..!!")
                        print("-----------------------------------------------------------------------")

                else:
                    print("-----------------------------------------------------------------------")
                    print("\t\tInvalid Choice..Transaction Failed..!!")
                    print("-----------------------------------------------------------------------")

        else:
            print("-----------------------------------------------------------------------")
            print("\t\tCannot Perform The Transaction ..!\n\tCustomer does NOT Exist..!!")
            print("-----------------------------------------------------------------------")


