
class Address:

    def __init__(self, city, state, pincode):
        self._city = city
        self._state = state
        self._pincode = pincode
        #string formater{}

    @property
    def city(self):
         return self._city

    @city.setter
    def city(self, city):
        self._city = city

    @city.deleter
    def city(self):
        self._city = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    @property
    def pincode(self):
        return self._pincode

    @pincode.setter
    def pincode(self, pincode):
        self._pincode = pincode

    def displayAddr(self):
        print('city : ',self._city)
        print('state : ', self._state)
        print('pincode : ', self._pincode)





