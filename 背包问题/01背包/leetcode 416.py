# @Time    : 2023/5/10 9:20
# @Author  : ygd
# @FileName: leetcode 416.py
# @Software: PyCharm


'''
leetcode
416. 分割等和子集
mid
https://leetcode.cn/problems/partition-equal-subset-sum/
'''


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        total = sum(nums)
        if total / 2 < max(nums):
            return False
        if total % 2 == 1:
            return False
        dp = [True] + [False] * (total // 2)

        for num in nums:
            for j in range(total // 2, num - 1, -1):
                dp[j] |= dp[j - num]
        return dp[total // 2]


print(Solution().canPartition([1, 5, 11, 5]))
