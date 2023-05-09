# @Time    : 2023/5/8 21:10
# @Author  : ygd
# @FileName: leetcode 279.py
# @Software: PyCharm

'''
leetcode
279. 完全平方数
mid
https://leetcode.cn/problems/perfect-squares/description/
'''


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        ps = [i * i for i in range(1, int(n ** 0.5) + 1)][::-1]  # 从大到小减去，帮助加速
        pset = set(ps)
        queue, cache = [n], {n: 1}
        while queue:
            val = queue.pop(0)
            if val in pset: return cache[val]
            for p in ps:
                if val - p > 0 and val - p not in cache:
                    queue.append(val - p)
                    cache[val - p] = cache[val] + 1
        return -1

print(Solution().numSquares(12))