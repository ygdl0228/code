# @Time    : 2023/5/16 10:47
# @Author  : ygd
# @FileName: leetcode 54.py
# @Software: PyCharm

'''
leetcode
54. 螺旋矩阵
mid
https://leetcode.cn/problems/spiral-matrix/description/
'''


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n, m = len(matrix), len(matrix[0])
        ans = []
        l, r, t, b = 0, m - 1, 0, n - 1
        while len(ans) < n * m:
            for i in range(l, r + 1):
                if len(ans)<n*m:
                    ans.append(matrix[t][i])
            t += 1
            for j in range(t, b + 1):
                if len(ans) < n * m:
                    ans.append(matrix[j][r])
            r -= 1
            for k in range(r, l - 1, -1):
                if len(ans) < n * m:
                    ans.append(matrix[b][k])
            b -= 1
            for z in range(b, t - 1, -1):
                if len(ans) < n * m:
                    ans.append(matrix[z][l])
            l += 1
        return ans
