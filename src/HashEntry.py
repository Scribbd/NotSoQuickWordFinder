class HashEntry:
    """
    A class to store a Hashed Entity

    """
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, newValue):
        self.__value = newValue
        self.key = hash(newValue)

    @property
    def key(self):
        return hash(self.value)
    
    @key.setter
    def key(self, newKey):
        pass

    def __hash__(self):
        return hash(self.value)

