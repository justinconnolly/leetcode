# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head1 = pointer1 = ListNode(0)
        head2 = pointer2 = ListNode(0)
        while head:
            if head.val < x:
                pointer1.next = head
                pointer1 = pointer1.next
            else:
                pointer2.next = head
                pointer2 = pointer2.next
            head = head.next
        pointer2.next = None
        pointer1.next = head2.next
        return head1.next