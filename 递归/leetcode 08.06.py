# @Time    : 2023/4/23 16:04
# @Author  : ygd
# @FileName: leetcode 08.06.py
# @Software: PyCharm

'''
leetcode
面试题 08.06. 汉诺塔问题
简单
https://leetcode.cn/problems/hanota-lcci/
'''


class Solution(object):
    def hanota(self, A, B, C):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :rtype: None Do not return anything, modify C in-place instead.
        """
        n = len(A)
        self.remove(n, A, B, C)

    def remove(self, n, A, B, C):
        if n == 1:
            C.append(A[-1])
            A.pop()
            return
        else:
            self.remove(n - 1, A, C, B)
            C.append(A[-1])
            A.pop()
            self.remove(n - 1, B, A, C)
