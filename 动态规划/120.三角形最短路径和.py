from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #   思路：dp dp[i]第i层的最小值 每步只能到下一行相邻的节点上
        #   这里有 序号i只能到下一行的序号i或者i+1
        #   存在短视情况，如何处理？相当于只能往下或者往右下走
        #   递推：dp[i][j] = min(dp[i-1][j]+dp[i-1][j]) + triangle[i+1][j+1] i>1

        if len(triangle) == 0:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        dp = triangle
        dp[1][0] = triangle[0][0] + triangle[1][0]
        dp[1][1] = triangle[0][0] + triangle[1][1]
        for i in range(2, len(triangle)):
            for j in range(0, len(triangle[i])):
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                elif 1 <= j < len(triangle[i - 1]):
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
                else:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
        min_path = dp[len(triangle) - 1][0]
        for item in dp[len(triangle) - 1]:
            if item < min_path:
                min_path = item

        return min_path

    """
        这题最恶心的在于越界问题，非常容易写着写着就越界了，此外如果从上往下，约束条件非常地不好写，
        此外获得最后的结果在从上往下的算法中也需要再次遍历最后一行获得，这非常的不方便
        优化方法：自底向上，把约束简化。除此之外我们可以直接利用triangle本身而不用新建dp数组，同时因为顶点是唯一的，所以只要输出[0][0]就行了
        递推：dp[i][j]= min(dp[i+1][j],dp[i+1][j+1])+dp[i][j]
        边界条件：最后一行没有下一行了，因此最后一行不进循环，循环到第1行为止
        
    """

    def minpath2(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle)-2,-1,-1):
            for j in range (len(triangle[i])):
                triangle[i][j]= triangle[i][j]+min(triangle[i+1][j],triangle[i+1][j+1])
        return triangle[0][0]
