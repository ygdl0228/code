# @Time    : 2023/5/18 11:14
# @Author  : ygd
# @FileName: leetcode 347.py
# @Software: PyCharm

'''
leetcode
347. 前 K 个高频元素
easy
https://leetcode.cn/problems/top-k-frequent-elements/description/
'''


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash = {}
        for i in nums:
            hash[i] = hash.get(i, 0) + 1
        small_head = []
        for i, j in hash.items():
            heapq.heappush(small_head, (j, i))
            if len(small_head) > k:
                heapq.heappop(small_head)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(small_head)[1])
        return res[::-1]
