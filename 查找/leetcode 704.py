# @Time    : 2023/5/5 15:13
# @Author  : ygd
# @FileName: leetcode 704.py
# @Software: PyCharm

'''
leetcode
704. 二分查找
easy
https://leetcode.cn/problems/binary-search/
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1

print(Solution().search([-1, 0, 3, 5, 9, 12], 13))
