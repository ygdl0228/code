# @Time    : 2023/4/24 15:57
# @Author  : ygd
# @FileName: leetcode 724.py
# @Software: PyCharm

'''
leetcode
724. 寻找数组的中心下标
easy
https://leetcode.cn/problems/find-pivot-index/
'''


class Solution:
    def pivotIndex(self, nums):
        num1 = [0] * len(nums)
        total = sum(nums)
        if sum(nums[1:]) == 0:
            return 0
        for i in range(1, len(nums)):
            num1[i] = num1[i - 1] + nums[i - 1]
            if num1[i] == total - nums[i] - num1[i]:
                return i
        return -1


print(Solution().pivotIndex([2, 1, -1]))
