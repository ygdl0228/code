# @Time    : 2023/5/15 9:40
# @Author  : ygd
# @FileName: leetcode 319.py
# @Software: PyCharm


'''
leetcode
319. 灯泡开关
mid
https://leetcode.cn/problems/bulb-switcher/
'''


class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1

        ans = [1] * n
        for j in range(1, n, 2):
            ans[j] = 0
        for i in range(2, n, 3):
            ans[i] = 1 if ans[i] == 0 else 0
        return ans.count(1)


print(Solution().bulbSwitch(6))
