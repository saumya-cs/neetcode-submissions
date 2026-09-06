# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def validityHelper(self, root: Optional[TreeNode]):
        if root is None:
            return True
        if root.left:
            if root.left.val >= root.val:
                return False
        if root.right:
            if root.right.val <= root.val:
                return False
        return self.validityHelper(root.left) and self.validityHelper(root.right)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validityHelper(root)