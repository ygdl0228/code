# @Time    : 2023/4/24 14:57
# @Author  : ygd
# @FileName: leetcode 1480.py
# @Software: PyCharm

'''
leetcode
1480. 一维数组的动态和
easy
https://leetcode.cn/problems/running-sum-of-1d-array/
'''


class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        return nums

