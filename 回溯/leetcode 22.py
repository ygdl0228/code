# @Time    : 2023/5/16 16:04
# @Author  : ygd
# @FileName: leetcode 22.py
# @Software: PyCharm

'''
leetcode
22. 括号生成
mid
https://leetcode.cn/problems/generate-parentheses/description/
'''


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def backstack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backstack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(')')
                backstack(S, left, right + 1)
                S.pop()

        backstack([], 0, 0)
        return ans


print(Solution().generateParenthesis(3))
