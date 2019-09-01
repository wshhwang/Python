# Problem 1
#   http://interactivepython.org/courselib/static/pythonds/SortSearch/TheInsertionSort.html

def insertionSort(alist):
    for index in range(1,len(alist)):

        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]<currentvalue:   #swap smaller  to bigger only
            alist[position]=alist[position-1]
            position = position-1

        alist[position]=currentvalue

# Problem 2
#   http://interactivepython.org/courselib/static/pythonds/SortSearch/TheBubbleSort.html

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]<alist[i+1]:  # change only smaller to bigger "<"
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

# Problem 3
#   Selection Sort as shown in class: Lecture 19, Slide 45

def selectionSortK(alist, k):
    if k == 0:
        return
    
    for i in range(0,len(alist) - 1):
    
        min = i
        for j in range(i + 1, len(alist)):
        
            if alist[j] < alist[min]:
                min = j
                
        temp = alist[i]
        alist[i] = alist[min]
        alist[min] = temp
        if i == k: #stop up to k point , i equal to k
            return





# Problem 4
#   http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html

def mergeSort(alist, workspace=None, start=None, end=None):

    #### You can change this code if you want to, but it sufficient to implement a solution.
    #print("Splitting ",start, end)
    
    if workspace is None:
        workspace = [None] * len(alist)
        start = 0
        end = len(alist) #### Note that end is not a valid index into the array -- it's one past the last element!

    if end-start <= 1:
        return

    
        
    midpoint = (start+end)//2

    mergeSort(alist, workspace, start, midpoint)
    mergeSort(alist, workspace, midpoint, end)

    #### From here on, the code will look very similar to the code from the textbook
    ####    Be sure you understand what the code is doing before you copy it over!
    ####    Remember to copy the data back from the workspace!



    #lefthalf = workspace[start:midpoint]    #No SLICING!!!!!!!!!!!!!!!!!!
    #righthalf = workspace[midpoint:end]    # Slicing not allowed

    #lefthalf = range(start,midpoint)
    #righthalf =  range(midpoint, end)

        
    #print(lefthalf)
    #print(righthalf)
        
    startpoint = start
    halfpoint = midpoint
    endpoint = end
    #print(startpoint)
    #print(halfpoint)


    #for i in range(len(alist)):
    #while i <= len(range(start,end)):

    for i in range(startpoint,endpoint):
    #if alist[startpoint] <= alist[halfpoint]:
        #if halfpoint == endpoint or not startpoint == midpoint:


        if halfpoint == endpoint: #midpoint equal to last int   ## avoid IndexError: list index out of range
          #  if alist[startpoint] <= alist[halfpoint]:
            workspace[i] = alist[startpoint]
            startpoint = startpoint + 1
            
        elif alist[startpoint] < alist[halfpoint] and not startpoint == midpoint : #left side is smaller number
            workspace[i] = alist[startpoint]    #save leftside smaller number to workspace 
            startpoint = startpoint + 1         #move on to next number in the left side
        else:                                   # alist[startpoint] > alist[halfpoint] right side is smaller number
            workspace[i] = alist[halfpoint]     #save Right side smaller number to workspace 
            halfpoint = halfpoint + 1           #move on to next number in the Right side "midpoint +1"


    #for i in range ( startpoint, halfpoint -1):
     #   if alist[startpoint] < alist[halfpoint]
      #      workspace[i] = alist[startpoint]
       #     startpoint = startpoint + 1
#    for i in range ( halfpoint, endpoint):
 #       if alist[halfpoint] < alist[endpoint]
  #          workspace[i] = alist[halfpoint]
   #         halfpoint = halfpoint + 1

        
    #  i = 0
    # j = 0
    #k = 0

    # while i <= alist[lefthalf] or j <= alist[end]:
    #    if alist[lefthalf] < alist[righthalf]:
    #       workspace[k]=alist[lefthalf]
    #      lefthalf += 1
    # else:
    #    workspace[k]= alist[righthalf]
        #   righthalf += 1
        #k=k+1

    #while i < len(lefthalf):
    #   workspace[k]=lefthalf[i]
    #   i=i+1
    #   k=k+1

    #while j < len(righthalf):
    #   workspace[k]=righthalf[j]
     #  j=j+1
    # k=k+1
        
    #while i < len(alist):
    #   alist[i]=workspace[i]
     #  i+=1
    #for copy in range(startpoint,endpoint):  # 2) copy back the merged sorted list into alist filling
          #    alist[copy]=workspace[copy]       #the space where the left sorted half and right sorted
                                           #half came from
  
    for copy in range(start,end): 
        alist[copy]=workspace[copy]
    #print("Merging ",workspace)
    #print("Merged", alist)
































        
