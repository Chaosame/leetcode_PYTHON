# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List
"""
中序遍历根在中
"""


class Solution:
    def inorderTraversal(self, root: 'TreeNode') -> List[int]:
        res = []  # 返回结果
        self.midorder(root, res)
        return res

    def midorder(self, root, res):
        if not root:
            return  # 空树直接返回了

        self.midorder(root.left, res)
        res.append(root.val)
        self.midorder(root.right, res)
