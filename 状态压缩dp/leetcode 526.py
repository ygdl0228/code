# @Time    : 2023/5/10 16:31
# @Author  : ygd
# @FileName: leetcode 526.py
# @Software: PyCharm


'''
leetcode
526. 优美的排列
mid
https://leetcode.cn/problems/beautiful-arrangement/description/
'''

from functools import lru_cache


class Solution:
    def count_arrangement(self, n):
        @lru_cache(None)
        def dfs(pos, bits):
            if pos > n:
                return 1
            ret = 0
            for num in range(1, n + 1):
                used = (bits >> num) & 1
                if not used and (num % pos == 0 or pos % num == 0):
                    ret += dfs(pos + 1, bits + (1 << num))
            return ret

        return dfs(1, 0)
