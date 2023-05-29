# @Time    : 2023/5/29 22:32
# @Author  : ygd
# @FileName: leetcode 473.py
# @Software: PyCharm

'''
leetcode
473. 火柴拼正方形
mid
https://leetcode.cn/problems/matchsticks-to-square/description/
'''


class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        if sum(matchsticks) % 4 != 0:
            return False
        Tlen = sum(matchsticks) // 4
        dp = [-1] * (1 << len(matchsticks))
        dp[0] = 0
        for s in range(1, len(dp)):
            for k, v in enumerate(matchsticks):
                if s & (1 << k) == 0:
                    continue
                s1 = s & ~(1 << k)
                if dp[s1] >= 0 and dp[s1] + v <= Tlen:
                    dp[s] = (dp[s1] + v) % Tlen
                    break
        return dp[-1] == 0
