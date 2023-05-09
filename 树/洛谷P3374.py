# @Time    : 2023/5/7 17:04
# @Author  : ygd
# @FileName: 洛谷P3374.py
# @Software: PyCharm

'''
P3374 【模板】树状数组 1
https://www.luogu.com.cn/problem/P3374
'''

n, m = [5, 5]
nums = [1, 5, 4, 2, 3]
res = [[1, 2, 4, 2], [2, 3], [1, 1, 5, -1], [1, 3, 5, 7], [2, 4]]


class Bit:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def quary(self, x):
        x += 1
        return self.tree[x]

    def add(self, x, y, k):
        ans = 0
        while y > x:
            self.tree[y] += k
            y -= self.lowbit(y)
        while x > y:
            self.tree[y] -= k
            x -= self.lowbit(x)
        return ans

    def insert(self, x, val):
        x += 1
        while x < self.n:
            self.tree[x] += val
            x += self.lowbit(x)

    def lowbit(self, x):
        return x & -x


tree = Bit(n)
for i in range(n):
    tree.insert(i, nums[i])
print(tree.tree)
for num in res:
    if num[0] == 1:
        _, i, j, k = num
        tree.add(i - 1, j, k)
    elif num[0] == 2:
        print(tree.quary(num[1]))
print(tree.tree)
