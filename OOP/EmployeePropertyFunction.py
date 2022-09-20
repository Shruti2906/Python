#settergettrer@prperty private variables __

class Employee1:
    def __init__(self):
        self._eid = 0
        self._ename = 'aaa'
        self._esal = 345

    def get_eid(self):
        return self._eid
    def set_eid(self, e):
        self._eid = e
    def del_eid(self):
        del self.eid

    def get_ename(self):
        return self._ename
    def set_ename(self, en):
        self._ename = en
    def del_ename(self):
        del self._ename

    def get_esal(self):
        return self._ename
    def set_esal(self, en):
        self._ename = en
    def del_esal(self):
        del self._ename

    eid = property( get_eid, set_eid, del_eid);
    ename = property( get_ename, set_ename, del_ename);
    esal = property(get_esal, set_esal, del_esal);



'''
e = Employee1()
e.eid = 10
e.ename = "xyz"
e.esal = 10000
print(e.eid)
print(e.ename)
print(e.esal)
'''

