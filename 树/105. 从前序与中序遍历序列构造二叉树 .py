# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution0:
    """
    超时
    原因：多次遍历数组导致超时
    改进：不应当直接去遍历数组，因为我们只要知道多少个在左多少个在右即可
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        root = TreeNode(val=preorder[0])
        root_index = inorder.index(preorder[0])
        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index + 1:len(inorder)] if root_index < len(inorder) else []
        # 找第一个左树的最后一个元素的下标
        last_left_num = 0
        for i in range(len(preorder)):
            if i == 0:
                continue
            if len(left_inorder) == 0:
                break
            if preorder[i] in left_inorder:
                last_left_num = preorder.index(preorder[i])
            else:
                break
        if last_left_num == 0:
            left_preorder = []
        else:
            left_preorder = preorder[1:last_left_num + 1]
        if last_left_num == len(preorder) - 1:
            right_preorder = []
        else:
            right_preorder = preorder[last_left_num + 1:]
        # 　递归
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root


class Solution1:
    """
    改进方法：由于左右的节点都是聚集在一起的我们只要算出左树有多少个节点即可
    原因：多次遍历数组导致超时
    改进：不应当直接去遍历数组，因为我们只要知道多少个在左多少个在右即可
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:  # 边界
            return None
        root = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0])
        left_num = root_index
        root.left = self.buildTree(preorder[1:left_num + 1], inorder[0:root_index])
        root.right = self.buildTree(preorder[left_num + 1:], inorder[root_index + 1:])
        return root


class Solution2:
    """
    改进方法：能不能不产生新的数组 就原数组的下标建树 这样就可以用一个hashmap去储存inorder里的序号和值的对应关系重复使用
    原因：多次产生新数组，每次都需要对新的数组进行一次index查找耗时严重
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def myBuildTree(pre_left, pre_right, in_left, in_right):
            if (pre_left > pre_right) or (in_left > in_right):
                return None
            root = TreeNode(preorder[pre_left])  # pre的最左是root
            root_index = inorder_index[preorder[pre_left]]
            left_num = root_index - in_left  # root的序号减去pre左端点的序号就是左树的节点个数
            root.left = myBuildTree(pre_left+1, pre_left + left_num, in_left, root_index - 1)
            root.right = myBuildTree(pre_left + left_num+1, pre_right, root_index + 1, in_right)
            return root

        # 因为是原地的 inorder中的序号和值是不会变化的那么可以用hash存
        length = len(preorder)
        inorder_index = {inorder[i]: i for i in range(len(inorder))}  # 这是可行的是因为题目中说各个树不相等
        return myBuildTree(0, length - 1, 0, length - 1)


if __name__ == '__main__':
    solu = Solution2()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    head = solu.buildTree(preorder, inorder)
    print(head)
