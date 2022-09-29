
class AccountTransaction:
    def __init__(self, e, id):
        self.e = e
        self._id = id

    def deposit(self, amt):
        self.e.acc.accBal = self.e.acc.accBal+amt;

    def withdraw(self, amt):
        if(self.e.acc.accBal-amt < 500):
            print("-----------------------------------------------------------------------")
            print("\t\tCannot Proceed Furthur Insufficient Fund..!!")
            print("-----------------------------------------------------------------------")
        else:
            self.e.acc.accBal = self.e.acc.accBal - amt;
            print("-----------------------------------------------------------------------")
            print("\t\tAmount withrawal Successfull..!!")
            print("-----------------------------------------------------------------------")





























