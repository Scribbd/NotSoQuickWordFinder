class HashTableEntry:
    """
    A class to store a Hashed Entity

    """
    def __init__(self, value):    
        """A class to store a Hashed Entity
        
        Arguments:
            value {Hashable Object} -- The value that needs to be stored. This has to be hashable.
        """        
        self.value = value

    @property
    def key(self):
        """ Get the key as generated property

        Returns:
            [Integer] -- Hash of the object. Will return None if value isnt hashable.
        """
        try:
            return hash(self.value)
        except TypeError:
            print("Can't hash " + self.value)
        except:
            print("It all broke")

        return None #There is nothing to return if nothing can be done.
    
    @key.setter
    def key(self, newKey):
        pass

    def get_bucket(self, size):
        return self.key % size

    def __hash__(self):
        return hash(self.value)

