# @Time    : 2023/5/6 22:19
# @Author  : ygd
# @FileName: 幼儿园.py
# @Software: PyCharm

'''
http://codefun2000.com/p/P1217
'''

n = 4
high = [1, 2, 1, 3]


class Bit:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def insert(self, x):
        while x < self.n:
            self.tree[x] += 1
            x += x & (-x)

    def query(self, x):
        x += 1
        ans = 0
        while x > 0:
            ans += self.tree[x]
            x -= x & (-x)
        return ans


tree = Bit(5)
for i in range(n):
    tree.insert(high[i])
print(tree.tree)
for j in range(n):
    print(tree.query(high[j]))
