# @Time    : 2023/5/10 11:03
# @Author  : ygd
# @FileName: leetcode 474.py
# @Software: PyCharm


'''
leetcode
474. 一和零
mid
https://leetcode.cn/problems/ones-and-zeroes/
'''


class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(len(strs)):
            count1 = strs[i].count('1')
            count0 = strs[i].count('0')
            for j in range(m, count0 - 1, -1):
                for k in range(n, count1 - 1, -1):
                    dp[j][k] = max(dp[j][k], dp[j - count0][k - count1]+1)
        return dp[m][n]
