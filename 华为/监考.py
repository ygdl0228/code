# @Time    : 2023/4/24 11:04
# @Author  : ygd
# @FileName: 监考.py
# @Software: PyCharm

'''
http://codefun2000.com/p/P1195
差分数组
'''

import sys
import os
import collections

n = int(input())
hashmap = collections.defaultdict(int)
for _ in range(n):
    a, b = map(int, input().split())
    hashmap[a] += 1
    hashmap[b + 1] -= 1

stack = []
for key, value in hashmap.items():
    stack.append([key, value])

stack.sort()
# print(stack)
cnt = 0
pre_time = stack[0][0]
ans = 0
for time, state in stack:
    delta = time - pre_time
    if cnt == 0:
        ans += delta
    elif cnt == 1:
        ans += delta * 3
    else:
        ans += delta << 2
    pre_time = time
    cnt += state
print(ans)

