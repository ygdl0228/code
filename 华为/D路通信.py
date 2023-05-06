# @Time    : 2023/5/6 22:12
# @Author  : ygd
# @FileName: D路通信.py
# @Software: PyCharm

'''
http://codefun2000.com/p/P1216
动态规划
'''
str1 = input()
str2 = input()
n, m = len(str1), len(str2)
dp = [[0] * (m + 1) for _ in range(n + 1)]
ans = 0
for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        dp[i][j] = dp[i + 1][j + 1] + 1 if str1[i] == str2[j] else 0
        ans = max(ans, dp[i][j])
print(ans)
