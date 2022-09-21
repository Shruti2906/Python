
class Employee1:

    def __init__(self):
        self._eid = 0
        self._ename = 'aaa'
        self._esal = 345
#attributes behaves lilke setter, getters and deleter    OR   getter, setter can be used as attributes
#when value is assigned to an attriute automatically setter will be called
#when value is assigned from an attriute (or while printing it) automatically getter will be called
#when del is used with an attriute automatically deletter will be called

    @property
    def eid(self):
        print("getter called emp1")
        return self._eid
    @eid.setter
    def eid(self, eid):

       # print("setter called emp1")
        self._eid = eid
    @eid.deleter
    def eid(self):
        self._eid = None

    @property
    def ename(self):
        return self._ename
    @ename.setter
    def ename(self, ename):
        self._ename = ename
    @ename.deleter
    def ename(self):
        self._ename = None

    @property
    def esal(self):
        return self._esal
    @esal.setter
    def esal(self, esal):
        self._esal = esal
    @esal.deleter
    def esal(self):
        self._esal = None


'''
e = Employee1()
e.eid = 10
e.ename = 'aaa'
e.esal = 10000

print(e.eid)
print(e.ename)
print(e.esal)
'''