# @Time    : 2023/5/16 15:28
# @Author  : ygd
# @FileName: leetcode 20.py
# @Software: PyCharm


'''
leetcode
20. 有效的括号
easy
https://leetcode.cn/problems/valid-parentheses/
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict_stack = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i in dict_stack:
                if not stack or dict_stack[i]!=stack.pop():
                    return False
            else:
                stack.append(i)
        return not stack