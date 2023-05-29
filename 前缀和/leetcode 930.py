# @Time    : 2023/5/27 20:56
# @Author  : ygd
# @FileName: leetcode 930.py
# @Software: PyCharm


'''
leetcode
930. 和相同的二元子数组
mid
https://leetcode.cn/problems/binary-subarrays-with-sum/description/
'''


class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        nums = [0] + nums
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        has = {0: 1}
        ans = 0
        for i in range(n - 1):
            r = nums[i + 1]
            l = r - goal
            ans += has.get(l, 0)
            has[r] = has.get(r, 0) + 1
        return ans
