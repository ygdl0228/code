# @Time    : 2023/5/10 15:09
# @Author  : ygd
# @FileName: leetcode 322.py
# @Software: PyCharm

'''
leetcode
322. 零钱兑换
mid
https://leetcode.cn/problems/coin-change/
'''


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j - coin] + 1)
        print(dp)
        return dp[amount] if dp[amount]!=float('inf') else -1

print(Solution().coinChange([1, 2, 5],  11))
