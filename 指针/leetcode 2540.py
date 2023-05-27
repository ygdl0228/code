# @Time    : 2023/5/26 16:41
# @Author  : ygd
# @FileName: leetcode 2540.py
# @Software: PyCharm


'''
leetcode
2540. 最小公共值
easy
https://leetcode.cn/problems/minimum-common-value/description/
'''


class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        return min(set(nums1) & set(nums2), default=-1)


print(Solution().getCommon([1, 2, 3], [2, 4]))
