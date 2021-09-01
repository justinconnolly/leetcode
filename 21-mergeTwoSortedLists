class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            returnHead = l1
            l1 = l1.next
        else:
            returnHead = l2
            l2 = l2.next
        currentNode = returnHead

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                currentNode.next = l1
                currentNode = l1
                l1 = l1.next
            else:
                currentNode.next = l2
                currentNode = l2
                l2 = l2.next
        if l1 is not None:
            currentNode.next = l1
        elif l2 is not None:
            currentNode.next = l2

        return returnHead
