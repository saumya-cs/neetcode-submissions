# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(r1, r2):
            if not r1 and not r2:
                return True
            if (not r1 and r2) or (r1 and not r2):
                return False
            if (r1.val != r2.val):
                return False
            return sameTree(r1.right, r2.right) and sameTree(r2.left, r1.left)
        
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if sameTree(node, subRoot):
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False

            
        