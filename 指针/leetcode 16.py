# @Time    : 2023/5/24 16:47
# @Author  : ygd
# @FileName: leetcode 16.py
# @Software: PyCharm

'''
leetcode
16. 最接近的三数之和
mid
https://leetcode.cn/problems/3sum-closest/
'''


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        ans = 10e7
        for i in range(n):
            left, right = i + 1, n - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    return target
                if abs(total - target) < abs(ans - target):
                    ans = total
                if total > target:
                    while left != right and nums[right] == nums[right - 1]: right -= 1
                    right -= 1
                else:
                    while left != right and nums[left] == nums[left + 1]: left += 1
                    left += 1
        return ans


print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
