# @Time    : 2023/4/23 16:24
# @Author  : ygd
# @FileName: leetcode 509.py
# @Software: PyCharm

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
        if n==0:
            return 0

        F=[0]*(n+1)
        F[1]=1
        for i in range(2,n+1):
            F[i]=F[i-1]+F[i-2]
        return F[n]

print(Solution().fib(2))