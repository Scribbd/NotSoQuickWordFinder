from .HashBucketEntry import HashBucketEntry

class HashBucket:
    """I am just having fun now. This is formally a list with extra stats added and funny functions.    

    """    

    def __init__(self, bucket_no):
        self._list = {None}
        self.bucket_no = bucket_no
        
    def toss_in(self, value):
        """Crumple it up and toss it in, I guess.
        
        Arguments:
            value {Hashable Object} -- Anything really that can be hash()-ed or has a __hash__() that works.
        """        
        if value is HashBucketEntry:
            self._list.add(value)
        else:
            self._list.add(HashBucketEntry(value))

    def rummage_through_and_find(self, value):
        """Panick! Now you gotta find that thing you tossed in.
        
        Arguments:
            value {Hashable Object} -- Anything really that can be hash()-ed or has a __hash__() that works.
        """                
        for entry in self._list:
            if entry == value:
                return True
        return False


    def __str__(self):
        out = "This bucket has the following content:"
        for entry in self._list:
            out += " " + str(entry) + ","
        return out
