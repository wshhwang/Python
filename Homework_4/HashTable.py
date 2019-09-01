# William Hwang
#wshhwang@ucdavis.edu
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.count_emptyslot = self.size # O(1) modify to the __init__ method the put method to keep the O(1) complexity
                                        #modify in def put()
        
               
        # https://planetmath.org/goodhashtableprimes
        self.good_sizes = [11,23,53,97,193,389,769,1543]





    
    
    def hashfunction(self,key,size):
         return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def get(self,key):
        startslot = self.hashfunction(key,len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and  \
                           not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

    
        

    
    # Problem 3 Part 1
    
    
    def empty_slots(self):

#not O(1) complexity
#        default = 0
#
#       for a in self.slots:
#            if a == None:
#               default += 1
#           else:
#               default -=1
#
#       return default
        #empty_slot = self.size

#https://piazza.com/class/jtqbsk4spmk58r?cid=327

#To keep the O(1) complexity, you will need to add a variable to instances
#of the HashTable class (in the __init__ method) that keeps track of
#the number of empty slots. The variable should not be named empty_slots
#since that will conflict with the method empty_slots().
#
# We would expect you to modify to the __init__ method the put method \
#to keep the O(1) complexity.

        return self.count_emptyslot


    #def NextPrimeNumber(self):
     #   def CheckPrime(number):







    #def checkFullSize(self):
     #   if self.count_emptyslot == 0:
      #      return True
        
    def getNextPrime(self):

        for size in self.good_sizes: #for loop to find next size in good_sizes list
            if size == self.size:    # if size is same , skip
                return True
            elif size > self.size:   # to get next size number, it should be bigger value
                new_size = size      # assign new_size as next size number
        return new_size
           

    # Problem 3 Part 2
#https://piazza.com/class/jtqbsk4spmk58r?cid=368


    
    def put(self,key,data):  #key = slots ,, #data = value


#self.put(key, value)  https://piazza.com/class/jtqbsk4spmk58r?cid=369
         #if self.size % 2 == 0 or self.size %3 ==0:
          #  return False
        #else:
         #   prime_number= self.size

        #if prime_number not in self.good_sizes:
         #   self.good_sizes.append(prime_number)           

    


        
        if self.count_emptyslot == 0: #If the table is full, emptyslot is 0
            
            new_size = self.getNextPrime() # you will create a new table using the next value in the good_sizes list
            oldkey = self.slots #assign oldkey to save for new table
            olddata = self.data #assign olddata to save for new table
            
            self.size = new_size     #get next value from self.getNextPrime and become as self.size (*updated)
            self.slots = [None] * self.size 
            self.data = [None] * self.size
            
            self.count_emptyslot = self.size
            #self = [[] for _ in range(self.size)]
            for a in range(0,len(oldkey)): #re-insert each key from the previous table into the new table
                self.put(oldkey[a], olddata[a]) # re-insert as same order (key, data)
            
            



        
        hashvalue = self.hashfunction(key,len(self.slots))

        if self.slots[hashvalue] == None: #slots = key , if key is empty
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
            self.count_emptyslot  -= 1 # reduce self.size by -1 , at the end(table is full) -> size= 11 will become 0
            
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  #replace
          
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))
                while self.slots[nextslot] != None and \
                          self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                   # self.count_emptyslot = self.count_emptyslot - 1 #for part 1 :https://piazza.com/class/jtqbsk4spmk58r?cid=332

                    

                else:
                    self.data[nextslot] = data #replace
                    #self.count_emptyslot = self.count_emptyslot + 1
                    

                 
