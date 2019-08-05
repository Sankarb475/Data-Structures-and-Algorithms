A stack is a collection of objects that are inserted and removed according to the last-in, first-out (LIFO) principle.
a stack is an abstract data type (ADT) such that an instance S supports the following operations::

S.push(e): Add element e to the top of stack S.

S.pop(): Remove and return the top element from the stack S; an error occurs if the stack is empty.

S.top(): Return a reference to the top element of stack S, without removing it; an error occurs if the stack is empty.

S.is empty( ): Return True if stack S does not contain any elements.

len(S): Return the number of elements in stack S

-- generally when we define the stack class, we start with an empty python list and we push each element as we go by to that list. But it is 
more efficient in practice to construct a list with initial length n than it is to start with an empty list and append n items (even
though both approaches run in O(n) time). So we might wanna create a stack class, the constructor of which will ask for the maximum number
of element we would be pushing into the stack.

#traversing and poping through a Stack
while not stack.is_empty():
    stack.pop()
    
#Pushing a list element into a stack
for i in list1:
    stack.push(i)
    
