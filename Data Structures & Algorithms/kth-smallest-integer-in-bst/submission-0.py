# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, node):
       
        if node.left:
            self.helper(node.left)
       
        self.count = self.count - 1
        if self.count == 0:
            self.result = node.val
        if node.right:
            self.helper(node.right)
        return self.result
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k
        self.result = None
        return self.helper(root)
        
        