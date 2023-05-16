# @Time    : 2023/5/10 16:09
# @Author  : ygd
# @FileName: leetcode 78.py
# @Software: PyCharm


'''
leetcode
78. 子集
mid
https://leetcode.cn/problems/subsets/description/
'''


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        sub_sets = []
        for i in range(1 << n):
            sub_set = []
            for j in range(n):
                if i >> j & 1:
                    sub_set.append(nums[j])
            sub_sets.append(sub_set)
        return sub_sets
