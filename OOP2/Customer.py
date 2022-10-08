
class Customer:

    def __init__(self, cid, cname, csal, addr, acc):
        self._cid = cid
        self._cname = cname
        self._csal = csal
        self._addr = addr
        self._acc = acc

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



