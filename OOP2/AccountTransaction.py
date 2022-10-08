
class AccountTransaction:
    def __init__(self, c, id):
        self.c = c
        self._id = id

    def deposit(self, amt):
        self.c.acc.accBal = self.c.acc.accBal+amt;

    def withdraw(self, amt):
        if(self.c.acc.accBal-amt < 500):
            print("-----------------------------------------------------------------------")
            print("\t\tCannot Proceed Furthur Insufficient Fund..!!")
            print("-----------------------------------------------------------------------")
        else:
            self.c.acc.accBal = self.c.acc.accBal - amt;
            print("-----------------------------------------------------------------------")
            print("\t\tAmount withrawal Successfull..!!")
            print("-----------------------------------------------------------------------")





























