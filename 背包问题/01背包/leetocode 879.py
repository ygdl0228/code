# @Time    : 2023/5/10 14:56
# @Author  : ygd
# @FileName: leetocode 879.py
# @Software: PyCharm

'''
leetcode
879. 盈利计划
hard
https://leetcode.cn/problems/profitable-schemes/
'''


class Solution(object):
    def profitableSchemes(self, n, minProfit, group, profit):
        """
        :type n: int
        :type minProfit: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        length = len(group)
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(length + 1)]
        dp[0][0][0] = 1
        for i in range(1, length + 1):
            member, earn = group[i - 1], profit[i - 1]
            for j in range(n + 1):
                for k in range(minProfit + 1):
                    if j<member:
                        dp[i][j][k]=dp[i-1][j][k]
                    else:
                        dp[i][j][k]=(dp[i-1][j][k]+dp[i-1][j-member][max(0,k-earn)])%(10**9+7)
        return sum(dp[length][j][minProfit] for j in range(n+1))%(10**9+7)
