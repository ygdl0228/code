# @Time    : 2023/5/1 23:56
# @Author  : ygd
# @FileName: 华为 引擎模块初始化.py
# @Software: PyCharm

'''
http://codefun2000.com/p/P1229
拓扑排序
'''

from collections import deque

N = int(input())

indegre = [0 for _ in range(N + 1)]
nxs = {i: [] for i in range(N + 1)}

for i in range(1, N + 1):
    lines = [int(c) for c in input().split(" ")]
    if lines[0] == 0: continue
    for j in range(1, len(lines)):
        nxs[lines[j]].append(i)
        indegre[i] += 1

q = deque()
for i in range(1, N + 1):
    if indegre[i] == 0:
        q.append(i)

cnt1 = 0
cnt2 = 0
while len(q):
    size = len(q)
    cnt1 += 1
    for i in range(size):
        node = q.popleft()
        cnt2 += 1
        for nx in nxs[node]:
            indegre[nx] -= 1
            if indegre[nx] == 0: q.append(nx)

if cnt2 == N:
    print(cnt1)
else:
    print(-1)
