# @Time    : 2023/4/24 14:04
# @Author  : ygd
# @FileName: leetcode 1109.py
# @Software: PyCharm

'''
leetcode
1109. 航班预订统计
mid
https://leetcode.cn/problems/corporate-flight-bookings/
'''


class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        nums = [0] * n
        for l, r, inc in bookings:
            nums[l - 1] += inc
            if r < n:
                nums[r] -= inc
        for i in range(1, n):
            nums[i] += nums[i - 1]
        return nums


print(Solution().corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5))
