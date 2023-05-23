# @Time    : 2023/5/22 22:04
# @Author  : ygd
# @FileName: leetcode 743.py
# @Software: PyCharm

'''
leetcode
743. 网络延迟时间
mid
https://leetcode.cn/problems/network-delay-time/
'''


class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        g = [[float('inf')] * n for _ in range(n)]
        for x, y, time in times:
            g[x - 1][y - 1] = time
        used = [False] * n
        dist = [float('inf')] * n
        dist[k - 1] = 0
        for _ in range(n):
            x = -1
            for y, u in enumerate(used):
                if not u and (x == -1 or dist[y] < dist[x]):
                    x = y
            used[x] = True
            for y, time in enumerate(g[x]):
                dist[y] = min(dist[y], dist[x] + time)
        ans = max(dist)
        return ans if ans < float('inf') else -1
