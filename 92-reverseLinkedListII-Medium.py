# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        
        curr, prev = head, None
        
        for i in range(left - 1):
            prev = curr
            curr = curr.next
        
        tail = curr
        start = prev
        
        for i in range(right - left + 1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        if start:
            start.next = prev
        else:
            head = prev
            
        tail.next = curr
        return head