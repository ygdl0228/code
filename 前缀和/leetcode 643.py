# @Time    : 2023/4/24 15:14
# @Author  : ygd
# @FileName: leetcode 643.py
# @Software: PyCharm


'''
leetcode
643. 子数组最大平均数 I
easy
https://leetcode.cn/problems/maximum-average-subarray-i/
'''


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        presum=[0]*(len(nums)-k+1)
        presum[0]=sum(nums[0:k])
        for i in range(k, len(nums)):
            presum[i-k+1]=presum[i-k]+nums[i]-nums[i-k]
        return max(presum)/k

print(Solution().findMaxAverage([1,12,-5,-6,50,3],4))