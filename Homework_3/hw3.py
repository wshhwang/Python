# Your name and email here
#William Seunghyeon Hwang
# wshhwang@ucdavis.edu
# Problem 1

def findSmallest(items):
    #num_list = []
    #num_list.append(items)

    
    #smallest = num_list[0]
    #if it has one number
    len_items = len(items)
    smallest = items[0]
    if len_items == 1:
        smallest = items[0]
        return smallest
        
    
    next_smallest = findSmallest(items[1:])
    if smallest < next_smallest:
        return smallest
    else:
        return next_smallest
    return

# Problem 2
#using Node.py
from Node import Node

def findValue(value, linkedList):
    #len_linkedList = len(linkedList)
    #if linkedList == []:
    if not linkedList :
        return False

    search_value = linkedList.getData()
    
    if search_value == value:
        return True
    else:
        return findValue(value, linkedList.getNext())
    return False
    
    #next_value = linkedList.getNext()
    #if next_value == value:
     #   return True
    #else:
     #   return False
    
        
    
'''
   # elif findValue(linkedList.getNext()) == value:
    else:
        next_value = linkedList.getNext()
        if linkedList.getData() == next_value:
            return True
        return False'''
   

    

# Problems 3 and 5
#google interview question LOL

# equation : Rung(n) = Rung(n - 1 ) + rung (n-2)


# Problem 5 ->def ladder(length, knownResults = {}):
#def ladder(rungs):
def ladder(length, knownResults = {}):

#    caching -> checking from knownResults
    if length in knownResults: 
        # 4.12 text book (Recursively Counting Coins with Table Lookup (lst_change2))
        return knownResults[length] 


    num_ways = 0 #intial value
    
    if length <= 1:
        num_ways = 1
        knownResults[length] = num_ways
        return num_ways
    elif length == 2:
        num_ways = 2
        knownResults[length] = num_ways
        return num_ways
    else: 
        num_ways = ladder(length - 1,knownResults) + ladder(length -2, knownResults) # equation : Rung(n) = Rung(n - 1 ) + rung (n-2)
        knownResults[length] = num_ways
        return num_ways
    return num_ways

# Problem 4

def recPal(str):
    len_str = len(str)
    if len_str <= 1:
        return True # always panlindrome when str has empty or 1 letter


#https://piazza.com/class/jtqbsk4spmk58r?cid=230

    if str[0] == str [-1] and recPal(str[1:-1]): # check first[0] and last[0] & re-recPal for shorten letters
                                     #slicing 1:-1
        return True

    '''if str[0] == str [-1]:
        n = - 1 
        if str[1] == str [n]:
            n -= 1 
            return True'''

    
    return 
    















    
