# @Time    : 2023/4/26 19:30
# @Author  : ygd
# @FileName: 没有上司的舞会.py
# @Software: PyCharm


'''
树dp
https://www.luogu.com.cn/problem/P1352
'''

n = int(input())
happy = []
for _ in range(n - 1):
    happy.append(int(input()))
happy = [0] + happy
root = [i + 1 for i in range(n)]
nums = {i + 1: [] for i in range(n)}
for _ in range(n - 1):
    l, k = list(map(int, input().split()))
    root.remove(l)
    nums[k].append(l)
f = [[0, 0] for _ in range(n + 1)]


def dfs(root):
    f[root][1] = happy[root]
    for i in nums[root]:
        dfs(i)
        f[root][0] += max(f[i][0], f[i][1])
        f[root][1] += f[i][0]
    return max(f[root][0], f[root][1])


res = []
dfs(root[0])
for i in range(n + 1):
    res.append(f[i][0])
    res.append(f[i][1])
print(max(res))
