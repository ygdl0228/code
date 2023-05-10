# @Time    : 2023/5/10 15:22
# @Author  : ygd
# @FileName: leetcode 518.py
# @Software: PyCharm

'''
leetcode
518. 零钱兑换 II
mid
https://leetcode.cn/problems/coin-change-ii/
'''


class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [1]+[0] * amount
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        return dp[amount]
