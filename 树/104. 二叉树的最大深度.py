# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: 'TreeNode') -> int:
        def deep(root):
            if not root:
                return 0
            leftdeep = deep(root.left)
            rightdeep = deep(root.right)
            return max(leftdeep, rightdeep) + 1

        return deep(root)
