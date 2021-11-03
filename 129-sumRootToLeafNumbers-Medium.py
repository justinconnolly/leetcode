# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        curr = root
        prev = None
        next = None
        path = [None]
        leafSum = []
        while curr:
            if prev is path[len(path) - 1]:
                if curr.left:
                    next = curr.left
                    path.append(curr)
                elif curr.right:
                    next = curr.right
                    path.append(curr)
                else:
                    leafSum.append(path[1:])
                    leafSum[len(leafSum) - 1].append(curr)
                    next = path.pop()
            elif curr.left and prev is curr.left:
                if curr.right:
                    next = curr.right
                    path.append(curr)
                else:
                    next = path.pop()
            else:
                next = path.pop()
            prev = curr
            curr = next

        sum = 0
        for valList in leafSum:
            strSum = ""
            for value in valList:
                strSum += str(value.val)
            sum += int(strSum)
        return sum
