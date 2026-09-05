# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append((root,0))
        if root is None:
            return []
        ans = []
        levelToNode = dict()
        lastLevel = 0
        while q:
            node, level = q.popleft()
            lst = levelToNode.get(level, [])
            lst.append(node.val)
            levelToNode[level] = lst
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
            if not q:
                lastLevel = level
        for i in range(lastLevel + 1):
            lst = levelToNode[i]
            ans.append(lst)
        return ans
        
