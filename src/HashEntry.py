class HashEntry:
    """
    A class to store an Hashed Entity

    """
    def __init__(self, value):
        """
        To 

        :value The value that needs to be stored
        """
        self.value = value
        self.key = hash(value)

