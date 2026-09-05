# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #first elem of preorder is root, find idx of root in inorder, and this divides left and right
        inorder_val_to_idx = dict()
        for i,val in enumerate(inorder):
            inorder_val_to_idx[val] = i
        self.preorderIdx = 0
        def dfs(left, right):
            if left > right:
                return
            node = TreeNode()
            middle_idx = inorder_val_to_idx[preorder[self.preorderIdx]]
            node.val = preorder[self.preorderIdx]
            self.preorderIdx += 1
            node.left = dfs(left, middle_idx - 1)
            node.right = dfs(middle_idx + 1, right)
            return node
        return dfs(0, len(inorder) - 1)
