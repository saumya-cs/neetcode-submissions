# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def validityHelper(self, root: Optional[TreeNode], minimum, maximum):
     
        if root is None:
            return True
        return root.val > minimum and root.val < maximum and self.validityHelper(root.left, minimum, root.val) and self.validityHelper(root.right, root.val, maximum)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validityHelper(root, float('-inf'), float('inf'))