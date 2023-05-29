# @Time    : 2023/5/29 19:56
# @Author  : ygd
# @FileName: leetcode 473.py
# @Software: PyCharm


'''
leetcode
473. 火柴拼正方形
mid
https://leetcode.cn/problems/matchsticks-to-square/description/
'''


class Solution:
    def makesquare(self, matchsticks):
        totallen = sum(matchsticks)
        if totallen % 4 != 0:
            return False
        matchsticks.sort(reversed=True)
        edges = [0] * 4

        def dfs(idx):
            if idx == len(matchsticks):
                return True
            for i in range(4):
                edges[i] += matchsticks[idx]
                if edges[i] <= totallen // 4 and dfs(idx + 1):
                    return True
                edges[i] -= matchsticks[idx]
            return False

        return dfs(0)
