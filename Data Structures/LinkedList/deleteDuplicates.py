# Solution of https://leetcode.com/problems/remove-duplicates-from-sorted-list/


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        
        pre = head
        cur = head.next
        
        while cur:
            if cur.val == pre.val:
                # pre remains on the first node, in the next loop again pre will be same
                pre.next = cur.next
                cur = cur.next
                
            else:
                pre = pre.next
                cur = cur.next
                
        return head
        
        
        
        
 
