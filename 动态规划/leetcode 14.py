# @Time    : 2023/5/6 16:52
# @Author  : ygd
# @FileName: leetcode 14.py
# @Software: PyCharm


'''
leetcode
14. 最长公共前缀
easy
https://leetcode.cn/problems/longest-common-prefix/description/
'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        n, m = len(strs[0]), len(strs)
        for i in range(n):
            c=strs[0][i]
            if any(i == len(strs[j]) or c!=strs[j][i] for j in range(1,m)):
                return strs[0][:i]
        return strs[0]

print(Solution().longestCommonPrefix(["flower","flower","flower","flower"]))