# @Time    : 2023/5/29 19:20
# @Author  : ygd
# @FileName: leetcode 698.py
# @Software: PyCharm

'''
leetcode
698. 划分为k个相等的子集
mid
https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/description/
'''


class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if sum(nums) % k != 0:
            return False
        n = len(nums)
        target = sum(nums) // k
        nums.sort()
        if nums[-1] > target:
            return False

        def dfs(state, summ):
            if state == (1 << n) - 1:
                return True
            for i in range(n):
                if summ + nums[i] > target:
                    break
                if state & (1 << i) == 0:
                    next_state = state + 1 << i
                    if dfs(next_state, (summ + nums[i]) % target):
                        return True
            return False

        return dfs(0, 0)
