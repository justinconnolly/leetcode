# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def find_length(slow):
            curr = slow
            length = 0
            while True:
                curr = curr.next
                length += 1
                if curr == slow:
                    return length
                    
        def find_start(head, length):
            first, second = head, head
            while length > 0:
                second = second.next
                length -= 1
            while first != second:
                first = first.next
                second = second.next
            return first
                    
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                length = find_length(slow)
                return find_start(head, length)
        return None