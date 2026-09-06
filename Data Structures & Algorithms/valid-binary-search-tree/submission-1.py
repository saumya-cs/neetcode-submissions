# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def validityHelper(self, root: Optional[TreeNode], minimum: int, maximum: int):
     
        if root is None:
            return True
        minimum = min(minimum, root.val)
        maximm = max(maximum, root.val)
        if root.left:
            if root.left.val >= maximum:
                return False
        if root.right:
            if root.right.val <= minimum:
                return False
        return self.validityHelper(root.left, minimum, maximum) and self.validityHelper(root.right, minimum, maximum)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validityHelper(root, root.val, root.val)