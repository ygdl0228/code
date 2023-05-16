# @Time    : 2023/5/16 11:02
# @Author  : ygd
# @FileName: leetcode 70.py
# @Software: PyCharm

'''
leetcode
70. 爬楼梯
easy
https://leetcode.cn/problems/climbing-stairs/
'''


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
print(Solution().climbStairs(4))