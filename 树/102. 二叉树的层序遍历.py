# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 层次遍历需要将借助队列 python中是list 用pop 出首个元素


"""
这里的要点在于 我需要先把每层的节点先加入一个列表在放入结果中 那么我需要把他们按顺序查出所有孩子 之后再统一删除 这和单纯的层次遍历是不同的 单纯的层次遍历只需要 每次把队列第一的pop掉即可
"""


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []  # 结果
        queue = [root]
        while queue:
            layer = []  # 保存每层
            nextqueue = []  # 下一层
            for item in queue:  # 在遍历一次层
                layer.append(item.val)
                if item.left:
                    nextqueue.append(item.left)
                if item.right:
                    nextqueue.append(item.right)
            queue = nextqueue
            res.append(layer)
        return res
