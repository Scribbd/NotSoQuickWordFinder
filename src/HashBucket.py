from .HashBucketEntry import HashBucketEntry

class HashBucket:
    """I am just having fun now. This is formally a list with extra stats added and funny functions.    

    """    

    def __init__(self, bucket_no):
        self._list = []
        self.bucket_no = bucket_no
        self.checked = 0 #How often I rumaged through my bucket
        self.missed = 0 #How often it didn't go in (dupes)
        self.hit = 0 #How often I scored
        
    def toss_in(self, value):
        """Crumple it up and toss it in, I guess. Will miss when something similar is already in the bucket. 
        
        Arguments:
            value {Hashable Object} -- Anything really that can be hash()-ed or has a __hash__() that works.

        Returns:
            [Boolean] -- [True when successfull in adding. False if it missed]
        """        
        if value is not HashBucketEntry:
            value = HashBucketEntry(value)
        
        if not self.rummage_through_and_find(value):
            self._list.append(value)
            self.hit += 1
            return True
        #implied else
        self.missed += 1
        return False

    def rummage_through_and_find(self, value):
        """Panick! Now you gotta find that thing you tossed in.
        
        Arguments:
            value {HashBucketEntry} -- Anything really that can be hash()-ed or has a __hash__() that works.
        """
        self.checked += 1                
        for entry in self._list:
            if entry == value:
                return True
        return False

    def print_stats(self):
        repeat_miss = []
        for entry in self._list:
            if not repeat_miss:
                repeat_miss.append(entry)
            elif entry.found == repeat_miss[0].found:
                repeat_miss.append(entry)
            if entry.found > repeat_miss[0].found:
                repeat_miss.clear()
                repeat_miss.append(entry)
        print("Hi, bucket {} agian, back with some stats: I scored {} things, and I missed {} times.\n".format(self.bucket_no, self.hit, self.missed) + 
        "\tThe most following words have been found {} times: ".format(repeat_miss[0].found), end='')
        for entry in repeat_miss:
            print(" {},".format(entry.value), end='')

        print("")


    def __str__(self):
        out = "This is bucket {} and I has the following content:".format(self.bucket_no)
        for entry in self._list:
            out += " " + str(entry) + ","
        return out
