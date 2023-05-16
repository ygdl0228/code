# @Time    : 2023/5/15 21:48
# @Author  : ygd
# @FileName: leetcode 415.py
# @Software: PyCharm


'''
leetcode
415. 字符串相加
easy
https://leetcode.cn/problems/add-strings/description/
'''


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n, m, ans = len(num1) - 1, len(num2) - 1, 0
        res = ''
        while n >= 0 or m >= 0:
            n1 = int(num1[n]) if n >= 0 else 0
            n2 = int(num2[m]) if m >= 0 else 0
            tmp = n1 + n2 + ans
            ans = tmp // 10
            res = str(tmp % 10) + res
            n, m = n - 1, m - 1
        return '1'+res if ans else res


print(Solution().addStrings('11', '123'))
