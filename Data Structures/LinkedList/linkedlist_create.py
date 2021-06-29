class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList():
    def __init__(self):
        self.head = None
        
    def listPrint(self):
        printval = self.head
        while(printval):
            print(printval.data)
            printval = printval.next
            
    def atBeginning(self, newdata):
        newhead = Node(newdata)
        newhead.next = self.head
        self.head = newhead
        
    def atEnd(self, data):
        newend = Node(data)
        printval = self.head
        if printval is None:
            self.head 
        while printval.next:
            if printval.next.next is None:
                printval.next.next = newend
                return
            printval = printval.next
                
                
    def insertNode(self,middleNode, newdata):
        if middleNode is None:
            print("The mentioned node is absent")
            return
        newnode = Node(newdata)
        newnode.next = middleNode.next
        middleNode.next = newnode
     
            
    def removeNode(self, remove):
        head = self.head
        
        # LL is empty
        if (Head == None):
            return
        
        # if the head is to be removed
        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return
        
        while head.next:
            if head.next == remove:
                head.next = remove.next
                return 
            head = head.next
            
ll = LinkedList()
Node1 = Node(1)

ll.head = Node1

ll.head.next = Node(2)

ll.head.next.next = Node(3)

ll.atBeginning(0)

ll.atEnd(4)
ll.atEnd(5)

ll.insertNode(ll.head.next, 1.5)

ll.removeNode(ll.head.next.next)

ll.listPrint()
