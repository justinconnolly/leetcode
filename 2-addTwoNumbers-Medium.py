# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        if not l1:
            return l2
        if not l2:
            return l1
        head = l1
        while l1 and l2:
            l1.val += l2.val + carry
            if l1.val >= 10:
                carry = 1
                l1.val -= 10
            else:
                carry = 0
            prev_l1 = l1
            l1 = l1.next
            l2 = l2.next
            if not l1 and not l2:
                if carry:
                    prev_l1.next = ListNode(carry)
                    return head
        if l1:
            while l1:
                prev_l1 = l1
                l1.val += carry
                if l1.val >= 10:
                    carry = 1
                    l1.val -= 10
                else:
                    carry = 0
                l1 = l1.next
                if carry == 0:
                    return head
            if carry:
                prev_l1.next = ListNode(carry)

        if l2:
            prev_l1.next = l2
            while l2:
                prev_l1 = l2
                l2.val += carry
                if l2.val >= 10:
                    carry = 1
                    l2.val -= 10
                else:
                    carry = 0
                l2 = l2.next
                if carry == 0:
                    return head
            if carry:
                prev_l1.next = ListNode(carry)
        return head