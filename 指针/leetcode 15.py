# @Time    : 2023/5/15 22:03
# @Author  : ygd
# @FileName: leetcode 15.py
# @Software: PyCharm

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            left, right = i + 1, n - 1
            if nums[i] > 0:
                break
            if nums[i] == nums[i - 1] and i > 0:
                continue
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left != right and nums[left] == nums[left + 1]: left += 1
                    while right != right and nums[right] == nums[right + 1]: right -= 1
                    left += 1
                    right -= 1
        return ans

print(Solution().threeSum([-1,0,1,2,-1,-4]))