
class Account:

    def __init__(self, accNo, accType, accBal):
        self._accNo = accNo
        self._accType = accType
        self._accBal = accBal

    #setter getter

    @property
    def accNo(self):
        return self._accNo
    @accNo.setter
    def accNo(self, accNo):
        self._accNo = accNo

    @property
    def accType(self):
        return self._accType
    @accType.setter
    def accType(self, accType):
        self._accType = accType

    @property
    def accBal(self):
        return self._accBal
    @accBal.setter
    def accBal(self, accBal):
        self._accBal = accBal




