from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        #   把只有一项的数组处理掉
        #   动态规划：
        #   递推关系：乘积：mul  dp[i]:包含nums[i]的最大乘积
        #   1. dp[i+1]=max(dp[i]*nums[i+1]，nums[i+1]) 但是这种没有考虑到负负得正的情况
        #   2. 分类讨论 如果num[i]是正数那么我们希望之前的是最大的。如果前面只能是负的那么合并到1.
        #   2. 如果num[i]是负的，那么我们其实希望它前面负的越多越好，看来有必要记录下i前的最小值
        #   3. 维护两个dp数组:1.dp_max[i]  = max(dp_max[i-1]*nums[i],nums[i],dp_min[i-1]*nums[i])
        #   2.dp_min[i] = min(dp_min[i-1]*dp[i],dp[i],dp_max[i-1]*nums[i])
        #   这样就完全覆盖了所有情况，最后遍历dp_max，找到最大的dp_max就是结果了
        nums_len = len(nums)
        dp_min = [0] * nums_len
        dp_max = [0] * nums_len
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        for i in range(1, nums_len):
            dp_max[i] = max(dp_max[i - 1] * nums[i], nums[i], dp_min[i - 1] * nums[i])
            dp_min[i] = min(dp_min[i - 1] * nums[i], nums[i], dp_max[i - 1] * nums[i])
        maxproduct = dp_max[0]
        for item in dp_max:
            if item > maxproduct:
                maxproduct = item
        return maxproduct
        #  写完ac
