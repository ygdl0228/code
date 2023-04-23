# @Time    : 2023/4/23 16:19
# @Author  : ygd
# @FileName: leetcode 509.py
# @Software: PyCharm

'''
leetcode
509. 斐波那契数
easy
https://leetcode.cn/problems/fibonacci-number/
'''


class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1)+self.fib(n-2)


