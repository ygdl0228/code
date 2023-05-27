# @Time    : 2023/5/27 20:50
# @Author  : ygd
# @FileName: leetcode 67.py
# @Software: PyCharm


'''
leetcode
67. 二进制求和
easy
https://leetcode.cn/problems/add-binary/description/
'''


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return '{0:b}'.format(int(a, 2) + int(b, 2))
