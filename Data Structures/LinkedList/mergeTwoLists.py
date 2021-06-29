# solution of https://leetcode.com/problems/merge-two-sorted-lists


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if l1 == None and l2 == None:
            return
        
        cur = sortedLL = ListNode(0)
        
        while l1 or l2:
            
            if l1 == None and l2!=None:
                cur.next = ListNode(l2.val)
                cur = cur.next
                l2 = l2.next
                
            elif l2 == None and l1!=None:
                cur.next = ListNode(l1.val)
                cur = cur.next
                l1 = l1.next
                
            elif l2.val <= l1.val:
                cur.next = ListNode(l2.val)
                cur = cur.next
                l2 = l2.next
                
            elif l1.val < l2.val:
                cur.next = ListNode(l1.val)
                cur = cur.next
                l1 = l1.next
        
        
        return sortedLL.next
            
