# @Time    : 2023/5/29 10:51
# @Author  : ygd
# @FileName: leetcode 3.py
# @Software: PyCharm


'''
leetcode
3. 无重复字符的最长子串
mid
https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n = len(s)
        max_len = 0
        ans = []
        for i in range(n):
            while s[i] in ans:
                ans.remove(ans[0])
            ans.append(s[i])
            max_len = max(max_len, len(ans))
        return max_len

print(Solution().lengthOfLongestSubstring("bbbbb"))
