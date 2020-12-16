# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: 'TreeNode') -> 'TreeNode':
        def vertree(root):
            if root is None:
                return
            tmp_node = root.left
            root.left = root.right
            root.right = tmp_node
            vertree(root.left)
            vertree(root.right)
            return root

        return vertree(root)
