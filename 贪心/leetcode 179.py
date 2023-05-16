# @Time    : 2023/5/16 10:35
# @Author  : ygd
# @FileName: leetcode 179.py
# @Software: PyCharm


'''
leetcode
179. 最大数
mid
https://leetcode.cn/problems/largest-number/description/
'''
import functools


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        srts = map(str, nums)

        def cmp(a, b):
            if a + b == b + a:
                return 0
            elif a + b > b + a:
                return 1
            else:
                return -1

        strs = sorted(srts, key=functools.cmp_to_key(cmp), reverse=True)
        return ''.join(strs) if strs[0] != '0' else 0


print(Solution().largestNumber([0, 0, 0]))
