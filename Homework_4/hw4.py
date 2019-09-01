# William Hwang
#wshhwang@ucdavis.edu
# Problem 1

#Textbook 5.3 The sequential Search


def sequentialSearchRec(alist, item, index=0):
    default = 0
    result = False

    while default < len(alist) and not result:
        if alist[default] == item:
            result= True
        else:
            default += 1 #next order in list
    return result

# Problem 2

def binarySearchRec(alist, item, first=None, last=None):

 #Trial 1 == not working = NotAllowed: You should not be using slicing for this assignment!
  #  if len(alist) == 0:
   #     return False
    #else:
     #   midpoint = len(alist) //2
      #  if alist[midpoint]== item:
       #     return True
        #else:
         #   if item < alist[midpoint]:
          #      return binarySearchRec(alist[:midpoint],item,first,last)
           # else:
            #    return binarySearchRec(alist[midpoint+1:],item,first,last)

#Trial 2 == not working
    #if first == None or last == none:
     #   return False
      #  
    #if first > last:
     #   return False
    #else:
     #   midpoint = (first + last)//2
      #  if item == alist[midpoint]:
       #     return True
        #elif item < alist[midpoint]:
         #   return binarySearchRec(alist[first:midpoint],item,first,last)
        #else:
         #   return binarySearchRec(alist[midpoint+1:last],item,first,last)

#Trial 3 = Textbook!! 5.4 
    if first == None: #making a default
        first = 0
    if last == None:  # making default
        last = len(alist) -1  #-1 
    result = False

    while first <= last and not result:
        midpoint = (first + last)//2 
        if alist[midpoint] == item:
            result = True
        else:
            if item < alist[midpoint]:
                last = midpoint -1
            else:
                first = midpoint +1

    return result
         
    



            
