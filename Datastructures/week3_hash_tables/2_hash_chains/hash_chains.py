# import necessary packages
import sys
# query class
class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]

# using a dictionary for the phone book hashing problem
class HashTable:
    def __init__(self, length):
        self.size = length

        # initialize table with none
        self.ht = [[] for x in range(length)]

        # hash function parameters
        self.mult_ = 263
        self.prime = 1000000007

        # to track number of records
        self.counter = 0

    # defines hashfunction
    def hash_funct(self, string):
        res = 0

        for idx in range(len(string)):
            res += (ord(string[idx]) * self.mult_**idx)
        
        # taking care of negatives
        res = ((res % self.prime) + self.prime) % self.prime

        # return value
        return res % self.size

    # adds string
    def add_string(self, string):
        # extract hash value
        hv = self.hash_funct(string)

        # extract chaing
        h_row = self.ht[hv]
        
        # extract table 
        if string not in h_row:
            self.ht[hv].append(string)
        
    # deletes string
    def del_string(self, string):
        # extract hash value
        hv = self.hash_funct(string)

        # extract chaing
        h_row = self.ht[hv]

        # tracker for start and end locations
        fin_idx = len(h_row) 
        idx = 0

        # loop through array
        while idx < fin_idx:
            if string == h_row[idx]:
                h_row.pop(idx)
                fin_idx -= 1
            else:
                idx += 1

        # reassign
        self.ht[hv] = h_row
        
    # finds string
    def find_string(self, string):
        # extract hash value
        hv = self.hash_funct(string)

        # extract chaing
        h_row = self.ht[hv]

        if string in h_row:
            return "yes"

        return "no"

    # returns row
    def check(self, num):
        # if number out of bounds
        if num > len(self.ht) - 1 or num < 0:
            print("Number either > array list [{}] or less than zero".format(len(self.ht)))
            sys.exit(0)

        print(' '.join(self.ht[num][::-1]))
    
    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.check(query.ind)
        else:
            if query.type == 'find':
                print(self.find_string(query.s))
            elif query.type == 'add':
                self.add_string(query.s)
            else:
               self.del_string(query.s)

    def read_query(self):
        return Query(input().split())

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())
                

if __name__== "__main__":
    bucket_count = int(input())
    proc = HashTable(bucket_count)
    proc.process_queries()
    