# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 按中线对称
class Solution:
    def isSymmetric(self, root: 'TreeNode') -> bool:
        def judge_sym(t1, t2):
            if not t1 or not t2:
                return t1 == t2
            elif t1.val == t2.val:
                return judge_sym(t1.left, t2.right) and judge_sym(t1.right, t2.left)
            else:
                return False

        if not root:
            return True
        return judge_sym(root.left, root.right)


"""
最坑的是判断条件 几种情况要仔细 空树的处理
"""
