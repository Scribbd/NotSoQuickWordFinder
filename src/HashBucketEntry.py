class HashBucketEntry:
    """
    A class to store a Hashed Entity

    """
    def __init__(self, value):    
        """A class to store a Hashed Entity
        
        Arguments:
            value {Hashable Object} -- The value that needs to be stored. This has to be hashable.
        """        
        self.value = value
        self.found = 1

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        self._value = new_value
        self._key = hash(new_value)
    
    @property
    def key(self):
        return self._key
    
    @key.setter
    def key(self, new_key):
        pass

    def __hash__(self):
        return self._key

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return hash(self) == hash(other)