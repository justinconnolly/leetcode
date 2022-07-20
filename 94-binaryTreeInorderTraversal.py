# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []
        self.inOrder(root, inorder)
        return inorder
    def inOrder(self, node, inorder):
        if node:
            self.inOrder(node.left, inorder)
            inorder.append(node.val)
            self.inOrder(node.right, inorder)
            