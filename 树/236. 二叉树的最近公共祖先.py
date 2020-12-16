# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    思路：后序遍历递归 左右儿子能找到p或q就返回并把这个节点加入列表 p q都找完时，从后往前找到最靠前的节点就是结果
    优化：递归时同时找p q（待实现)
"""


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_result = []
        q_result = []

        def find_path(root, p, p_result):
            if root.val == p.val:
                p_result.append(p)
                return True
            if root.left or root.right:
                l = False
                r = False
                if root.left:
                    l = find_path(root.left, p, p_result)
                if root.right:
                    r = find_path(root.right, p, p_result)
                if l or r:
                    p_result.append(root)
                    return True
                return False
            else:
                return False

        find_path(root, p, p_result)
        find_path(root, q, q_result)
        res = None
        for i in range(min(len(p_result), len(q_result))):
            if p_result[len(p_result) - 1 - i] == q_result[len(q_result) - 1 - i]:
                res = p_result[len(p_result) - 1 - i]
        return res
