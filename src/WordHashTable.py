import sys
from .HashBucket import HashBucket

class WordHashTable:
    """
    Welcome to a bad implementation of a hashtable. Collisions will be chained. Non-hashables and duplicates will be rejected. See help(WordHashTable) for constructor arguments.
    
    """

    def __init__(self, size = 256):
        """
        Keyword Arguments:
            size {Integer} -- The amount of buckets generated (default: {256})
        """
        self._table = [None] * size
        self.size = size
        #Some fun stats
        self.buckets = 0
        self.length = 0
        self.duplicates = 0
        self.collisions = 0
        self.checks = 0
        
    
    def insert(self, value):
        """Inserts a value when it can
        
        Arguments:
            value {Hashable Object} -- A hashable object, will not do anything if the object isn't hashable.
        """
        if self._is_hashable(value):
            bucket_no = self._get_bucket_no(value)

            #Check if a new bucket needs to be made
            if not self._table[bucket_no]:
                self._table[bucket_no] = HashBucket(bucket_no)
                self.buckets += 1
            else:
                self.collisions += 1 
            
            #Toss it in the bucket and let it sort itself out
            if self._table[bucket_no].toss_in(value):
                self.length += 1
            else:
                self.duplicates += 1

    def has(self, value):
        """Checks if a value is already in one of the buckets
        
        Arguments:
            value {Hashable Object} -- A hashable object, will not do anything if the object isn't hashable.
        
        Returns:
            [Boolean] -- [If the bucket has the value]
        """ 
        self.checks += 1       
        if self._is_hashable(value):
            bucket_no = self._get_bucket_no(value)
            return self._table[bucket_no].rummage_through_and_find(value)
            

    def print_table(self):
        """Prints the worst table of the worst stats
        """        
        print("This WordHasTable is the worst with this as content:")
        for bucket in self._table:
            if bucket:
                print(bucket)

    def print_stats(self):
        """Prints the worst stats of the worst table
        """        
        print("This WordHashTable is the worst with {} as bucket size, and {} entries.\n".format(self.size, self.length) +
        "\tIt tossed out {} duplicates, and chained {} collisions.\n".format(self.duplicates, self.collisions) +
        "\tIt also has {} empty bucket spots and it checked itself {} times.".format(self.size - self.buckets, self.checks))

    def print_bucket_stats(self):
        min_hit = min_tossed = sys.maxsize
        max_hit = max_tossed = -sys.maxsize - 1
        for bucket in self._table:
            #Hits
            if min_hit > bucket.hit:
                min_hit = bucket.hit
            if max_hit < bucket.hit:
                max_hit = bucket.hit
            #Misses
            if min_tossed > bucket.missed:
                min_tossed = bucket.missed
            if max_tossed < bucket.missed:
                max_tossed = bucket.missed
            #Print its stats
            bucket.print_stats()
        #Print global stats
        print("Together this means the largest bucket size is: {}. Smallest: {}. Most missed: {}. Least missed: {}".format(max_hit, min_hit, max_tossed, min_tossed))


    def _get_bucket_no(self, value):
        return hash(value) % self.size

    def _is_hashable(self, value):
        """Python probably has a more elegant way to do this, but I don't care right now.

        Arguments:
            value {Object} -- Any object
        
        Returns:
            Boolean -- If the hash function borked out or not
        """        
        try:
            hash(value)
        except:
            return False
        return True