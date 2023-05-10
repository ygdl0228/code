# @Time    : 2023/5/10 15:29
# @Author  : ygd
# @FileName: leetcode 1449.py
# @Software: PyCharm

'''
leetcode
1449. 数位成本和为目标值的最大数字
hard
https://leetcode.cn/problems/form-largest-integer-with-digits-that-add-up-to-target/
'''


class Solution(object):
    def largestNumber(self, cost, target):
        """
        :type cost: List[int]
        :type target: int
        :rtype: str
        """
        dp = [[float("-inf")] * (target + 1) for _ in range(10)]
        where = [[0] * (target + 1) for _ in range(10)]
        dp[0][0] = 0

        for i, c in enumerate(cost):
            for j in range(target + 1):
                if j < c:
                    dp[i + 1][j] = dp[i][j]
                    where[i + 1][j] = j
                else:
                    if dp[i][j] > dp[i + 1][j - c] + 1:
                        dp[i + 1][j] = dp[i][j]
                        where[i + 1][j] = j
                    else:
                        dp[i + 1][j] = dp[i + 1][j - c] + 1
                        where[i + 1][j] = j - c

        if dp[9][target] < 0:
            return "0"

        ans = list()
        i, j = 9, target
        while i > 0:
            if j == where[i][j]:
                i -= 1
            else:
                ans.append(str(i))
                j = where[i][j]

        return "".join(ans)


