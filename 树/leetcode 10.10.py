# @Time    : 2023/5/7 16:36
# @Author  : ygd
# @FileName: leetcode 10.10.py
# @Software: PyCharm

'''
leetcode
面试题 10.10. 数字流的秩
mid
https://leetcode.cn/problems/rank-from-stream-lcci/description/
树状数组
'''


class Bit:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, x):
        x += 1
        while x <= self.n:
            self.tree[x] += 1
            x += x & (-x)

    def query(self, x):
        x += 1
        ans = 0
        while x > 0:
            ans += self.tree[x]
            x -= x & (-x)
        return ans


class StreamRank:
    def __init__(self):
        self.bit = Bit(50001)

    def track(self, x):
        self.bit.update(x)

    def getRankOfNumber(self, x):
        return self.bit.query(x)
