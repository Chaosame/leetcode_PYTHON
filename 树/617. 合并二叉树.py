# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 可变不可变问题
class Solution:
    def mergeTrees(self, t1: 'TreeNode', t2: 'TreeNode') -> 'TreeNode':
        def merge(t1,t2):
            if t1 is None:
                return t2
            if t2 is None:
                return t1
            merged = 'TreeNode'(t1.val + t2.val)
            merged.left = merge(t1.left,t2.left)
            merged.right= merge(t1.right,t2.right)
            return merged
        return merge(t1,t2)

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None

    class Solution:
        def mergeTrees(self, t1: 'TreeNode', t2: 'TreeNode') -> 'TreeNode':
            def merge(t1, t2):
                if t1 is None:
                    t1 = t2
                    print(t1.val) # 需要用一个参数来接住 直接返回并不会改变原来的参数
                    return
                if t2 is None:
                    return
                else:
                    t1.val = t1.val + t2.val
                merge(t1.left, t2.left)
                merge(t1.right, t2.right)
                return t1

            return merge(t1, t2)

# 正解
    def mergeTrees(self, t1: 'TreeNode', t2: 'TreeNode') -> 'TreeNode':
        def merge(t1, t2):
            if t1 is None:
                t1 = t2
                return t1
            if t2 is None:
                return t1
            else:
                t1.val = t1.val + t2.val
            t1.left = merge(t1.left, t2.left)
            t1.right = merge(t1.right, t2.right)
            return t1

        return merge(t1, t2)

