# @Time    : 2023/5/6 16:39
# @Author  : ygd
# @FileName: leetcode 719.py
# @Software: PyCharm


'''
leetcode
718. 最长重复子数组
mid
https://leetcode.cn/problems/maximum-length-of-repeated-subarray/description/
'''


class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n, m = len(nums1), len(nums2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                dp[i][j] = dp[i + 1][j + 1] + 1 if nums1[i] == nums2[j] else 0
                ans = max(ans, dp[i][j])
        return ans


print(Solution().findLength([1, 2, 3, 2, 1], [3, 2, 1, 4]))
