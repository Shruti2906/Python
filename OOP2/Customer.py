
class Customer:

    def __init__(self, cid, cname, csal, addr, acc):
        self._cid = cid
        self._cname = cname
        self._csal = csal
        self._addr = addr
        self._acc = acc
#attributes behaves lilke setter, getters and deleter    OR   getter, setter can be used as attributes
#when value is assigned to an attriute automatically setter will be called
#when value is assigned from an attriute (or while printing it) automatically getter will be called
#when del is used with an attriute automatically deletter will be called

    @property
    def cid(self):
        return self._cid
    @cid.setter
    def cid(self, cid):
         self._cid = cid

    @cid.deleter
    def cid(self):
        self._cid = None

    @property
    def cname(self):
        return self._cname
    @cname.setter
    def cname(self, cname):
        self._cname = cname
    @cname.deleter
    def cname(self):
        self._cname = None

    @property
    def csal(self):
        return self._csal
    @csal.setter
    def csal(self, csal):
        self._csal = csal
    @csal.deleter
    def esal(self):
        self._csal = None

    @property
    def addr(self):
        return self._addr

    @addr.setter
    def addr(self, addr):
        self._addr = addr;

    @addr.deleter
    def addr(self):
        self.addr = None


    @property
    def acc(self):
        return self._acc;

    @acc.setter
    def acc(self, acc):
        self.acc = acc

    @acc.deleter
    def acc(self):
        self.acc = None



'''
e = Employee1()
e.eid = 10
e.ename = 'aaa'
e.esal = 10000

print(e.eid)
print(e.ename)
print(e.esal)
'''