# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def helper (self, root: TreeNode, maxValue: int):
        if root is None:
            return 0
        if root.val >= maxValue:
            return 1 + self.helper(root.right, root.val) + self.helper(root.left, root.val)
        else:
            return self.helper(root.right, maxValue) + self.helper(root.left, maxValue)
            
           
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return self.helper(root, root.val)
        