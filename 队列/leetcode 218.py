# @Time    : 2023/5/5 15:25
# @Author  : ygd
# @FileName: leetcode 218.py
# @Software: PyCharm

'''
leetcode
218. 天际线问题
hard
https://leetcode.cn/problems/the-skyline-problem/description/
'''

import heapq


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        s = []
        ans = []
        h = 0
        for left, right, height in buildings:
            while s and s[0][0] < left:
                r, rh = heapq.heappop(s)
                if rh == h:
                    rh = max(s, key=lambda val: val[1])[1] if s else 0
                    if rh != h:
                        h = rh
                        ans.append([r, h])
            if height > h:
                h = height
                # 避免左端点重复的问题
                if ans and left == ans[-1][0]:
                    ans[-1][1] = h
                else:
                    ans.append([left, h])
            heapq.heappush(s, [right, height])

        while s:
            r, rh = heapq.heappop(s)
            if rh == h:
                rh = max(s, key=lambda val: val[1])[1] if s else 0
                if rh != h:
                    h = rh
                    ans.append([r, h])
        return ans


print(Solution().getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
