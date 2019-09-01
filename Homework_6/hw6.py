# ECS32B Spring 2019 Homework 6
# Your name here! William Hwang


# Grab some helper functions into the current namespace
from hw6_tools import *
import operator



# Problem 1 # https://piazza.com/class/jtqbsk4spmk58r?cid=520

#expTree = ['(','(','3','+','(','1','/','2',')',')','*','(','5','-','2',')',')']

"""
def expressTree(leftTree, operator, rightTree):
    tree = ExpTree(operator)
    tree.setLeftChild(leftTree)
    tree.setRightChild(rightTree)
    return tree
    
expTree = expressTree(expressTree(3,"+",expressTree(1,"/",2)),"*",expressTree(5,"-",2))
"""
def expressTree(leftnode, operator, rightnode):
    tree = ExpTree(operator)
    lefttree = ExpTree(leftnode)
    righttree = ExpTree(rightnode)
    
    tree.setLeftChild(lefttree)
    tree.setRightChild(righttree)
    
    return tree
    
expTree = expressTree(expressTree(3,"+",expressTree(1,"/",2)),"*",expressTree(5,"-",2))
#expTree = ("((3+(1/2))*(5-2))")

#print(expTree)

"""
def evaluate(value):
    tree = ExpTree(value)
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftC = tree.getLeftChild()
    rightC = tree.getRightChild()

    if leftC and rightC:
        fn = opers[tree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return tree.getRootVal()
    return tree

expTree = evaluate ("((3+(1/2))*(5-2))")
"""



#def evaluate(leftChild, operator, rightChild):
 #   expTtree = ExpTree(operator)
    

# Problem 2
# Make sure your code uses the ExpTree class functions/methods provided
# for all the traversals, and you should be good.
# http://interactivepython.org/courselib/static/pythonds/Trees/TreeTraversals.html

def postorder(tree):


    if tree.getLeftChild():
        postorder(tree.getLeftChild())
    if tree.getRightChild() :
        postorder(tree.getRightChild())
    print(tree.getRootVal(), end= ' ')
    
    """
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal(), end= ' ')

    return
    """

def preorder(tree):

    
    print(tree.getRootVal(), end= ' ')
    if tree.getLeftChild():
        preorder(tree.getLeftChild())
    if tree.getRightChild():
        preorder(tree.getRightChild())
"""
    if tree:
        print(tree.getRootVal(), end= ' ')
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
    return
"""
def inorder(tree):
    

    #if tree != None:
    #    inorder(tree.getLeftChild() )
    #    print(tree.getRootVal(), end= ' ')
    #    inorder(tree.getRightChild())
    #return

    if tree.getLeftChild():
        inorder(tree.getLeftChild())
    print(tree.getRootVal(), end= ' ')
    if tree.getRightChild():
        inorder(tree.getRightChild())





    

# Problem 3
#For our expression trees, an operator always has two children (operands)
# because we only are considering binary operators.
# A number has no children because it has no operands.

def printexp(tree):

    #sVal = ""
#   if tree:
 #       sVal = '(' + printexp(tree.getLeftChild())
  #      sVal = sVal + str(tree.getRootVal())
   #     sVal = sVal + printexp(tree.getRightChild())+')'
    #return sVal

    if tree.getLeftChild() != None:
        leftNode= printexp(tree.getLeftChild())
        node= tree.getRootVal()
        rightNode= printexp(tree.getRightChild())
        exp = ('(' +leftNode+node+rightNode+ ")")
        
        return exp

    else:
        return str(tree.getRootVal())

    
    
   
# Problem 4

problem4_breadth_first_traversal = [0,1,2,5,3,4,6,8,7]
problem4_depth_first_traversal = [0,1,3,4,8,7,2,6,5]

# Problem 5
# The function dijkstra does not return anything. The work is does is reflected
# in changes made to the vertex objects. 
# Shortest path distances are stored in the Vertex objects.
# The goal is for you figure out how to recover it from the vertex
# objects to print out the table.
# flights = Graph()

#dijkstra(flights,flights.getVertex('SMF'))
       ##same as
#smf = flights.addVertex("SMF")
#dijkstra(flights,smf)

#http://interactivepython.org/courselib/static/pythonds/Graphs/TheGraphAbstractDataType.html?highlight=getvertex
flights = Graph()
flights.addEdge("SMF", "SFO", 47) #addEdge(fromVert, toVert, weight) Adds a new, weighted,
                                  #directed edge to the graph that connects two vertices.
flights.addEdge("SMF", "LAX", 98)
flights.addEdge("SMF", "LAS", 198)
flights.addEdge("SFO", "LAS", 98)
flights.addEdge("SFO", "PHX", 198)
flights.addEdge("SFO", "LAX", 49)
flights.addEdge("LAX", "PHX", 98)

dijkstra(flights,flights.getVertex('SMF'))
print("from To Cost")

for final in flights.getVertices(): #getVertices() returns the list of all vertices in the graph.
    if 'SMF' != final:
        print(f"{'SMF'} {final} {flights.getVertex(final).getDistance()}") #getVertex(vertKey) finds the vertex
                                                                            #in the graph named vertKey.
    











