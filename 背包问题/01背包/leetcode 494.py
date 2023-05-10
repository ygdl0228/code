# @Time    : 2023/5/10 14:44
# @Author  : ygd
# @FileName: leetcode 494.py
# @Software: PyCharm

'''
leetcode
494. 目标和
mid
https://leetcode.cn/problems/target-sum/
'''


class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        neg = sum(nums) - target
        if neg < 0 or neg % 2 == 1:
            return 0
        neg = neg // 2
        dp = [1] + [0] * neg
        for num in nums:
            for i in range(neg, num - 1, -1):
                dp[i] += dp[i - num]
        return dp[neg]
