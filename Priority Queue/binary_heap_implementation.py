'''
A balanced binary tree has roughly the same number of nodes in the left and right subtrees of the root.
A complete binary tree is a tree in which each level has all of its nodes.
In a heap, for every node x with parent p, the key in p is smaller than or equal to the key in x.
Since the entire binary heap can be represented by a single list, all the constructor will do is initialize the list and an 
attribute currentSize to keep track of the current size of the heap.
'''

'''
Because the tree is complete, Because the tree is complete, the left child of a parent (at position p) is the node that is 
found in position 2p in the list. Similarly, the right child of the parent is at position 2p+1 in the list.
Given that a node is at position n in the list, the parent is at position n/2.
'''

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
        
      
