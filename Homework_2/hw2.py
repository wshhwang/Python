from UnorderedList import UnorderedList

# Problem 1

class QueueFE:
    def __init__(self):
        self.items = []
        #raise NotImplementedError

    def isEmpty(self):
        return self.items == []
        #raise NotImplementedError

    def enqueue(self, item):
        self.items.insert( len(self.items), item)
        #raise NotImplementedError

    def dequeue(self):
        return self.items.pop(0)
        #raise NotImplementedError

    def size(self):
        return len(self.items)
       

# Problem 2

class Stack: #Last in First Out
    
    
     def __init__(self):
         
         self.newlist = UnorderedList() #creates new empty list
          
                    
        
     def isEmpty(self):
         
         #newlist = UnorderedList()
         return self.newlist.isEmpty() # see whether list is empty
            
     
        

     def push(self, item):
        # newlist = UnorderedList()
         return self.newlist.append(item) #add 
        
     

     def pop(self):
       #  newlist = UnorderedList() #pop() The front would be index 0, end will be size() -1
         return self.newlist.pop(self.newlist.size() -1)
         
        

                        #https://piazza.com/class/jtqbsk4spmk58r?cid=89
     def peek(self):    #Consider peek() as popping an item off the stack
                        #and then pushing it back on the stack before returning it. 
        # newlist = UnorderedList()
         item= self.newlist.pop(self.newlist.size() -1)
         self.newlist.append(item)
         return item # askingfor item
         #return self.newlist.append(item)

     def size(self):
       #  newlist = UnorderedList()
         return self.newlist.size()
        
     

# Problem 3

class Queue: #FIFO
    def __init__(self): #initialize
        self.newlist = UnorderedList()
        

    def isEmpty(self): #checking empty list
        #newlist = UnorderedList()
        return self.newlist.isEmpty()

    def enqueue(self, item): # enqueue 
        return self.newlist.append(item)
        #newlist = UnorderedList()
        #newlist.append(item)
        #newlist.size +=1
        
    def dequeue(self): #dequeue
      #  newlist = UnorderedList()
        return self.newlist.pop(0) #The front would be index 0, end will be size() -1

    def size(self): #return size
       # newlist = UnorderedList()
        return self.newlist.size()

# Problem 4

class Deque: #Double End Queue
    def __init__(self):
        self.newlist = UnorderedList()
        

    def isEmpty(self):
        return self.newlist.isEmpty()

    def addFront(self, item): #insert front
        self.newlist.insert(0, item)

    def addRear(self, item):    # add newest number and new position at the end
        self.newlist.append(item)

    def removeFront(self): 
        return self.newlist.pop(0) # 0 front index

    def removeRear(self): #https://piazza.com/class/jtqbsk4spmk58r?cid=151
        return self.newlist.pop(self.newlist.size() -1)
           

    def size(self):
        return self.newlist.size()



        
        
