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
    优化方法：自底向上，把约束简化
"""
