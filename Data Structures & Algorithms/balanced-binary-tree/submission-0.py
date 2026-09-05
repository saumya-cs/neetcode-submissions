# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(root):

            if not root:
                return (0, True)
            l = helper(root.left)
            r = helper(root.right)
            leftH, leftBalance = l[0], l[1]
            rightH, rightBalance = r[0], r[1]

            if not rightBalance or not leftBalance or abs(leftH - rightH) > 1:
                return [max(leftH, rightH), False]
            return [1 + max(leftH, rightH), True]
        return helper(root)[1]
        