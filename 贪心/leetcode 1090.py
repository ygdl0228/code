# @Time    : 2023/5/23 22:37
# @Author  : ygd
# @FileName: leetcode 1090.py
# @Software: PyCharm


'''
leetcode
1090. 受标签影响的最大值
mid
https://leetcode.cn/problems/largest-values-from-labels/description/
'''
from collections import Counter


class Solution(object):
    def largestValsFromLabels(self, values, labels, numWanted, useLimit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type numWanted: int
        :type useLimit: int
        :rtype: int
        """
        n = len(values)
        idx = list(range(n))
        idx.sort(key=lambda x: values[x], reverse=True)
        ans = choose = 0
        cnt = Counter()
        for i in range(n):
            label = labels[idx[i]]
            if cnt[label] == useLimit:
                continue
            choose += 1
            ans += values[idx[i]]
            cnt[label] += 1
            if choose == numWanted:
                break
        return ans
