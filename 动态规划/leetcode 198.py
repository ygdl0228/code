# @Time    : 2023/4/26 20:25
# @Author  : ygd
# @FileName: leetcode 198.py
# @Software: PyCharm

'''
leetcode
198. 打家劫舍
mid
https://leetcode.cn/problems/house-robber/
'''


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        dp[0]=nums[0]
        for i in range(1, len(nums)):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        return max(dp)
