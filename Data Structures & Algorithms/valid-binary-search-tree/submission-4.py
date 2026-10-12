# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root, low, high):
        if not root:
            return True
        if root.val >= high or root.val <= low:
            return False
        return self.helper(root.left, low, root.val) and self.helper(root.right, root.val, high)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float("-inf"), float("inf"))