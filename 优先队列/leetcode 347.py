# @Time    : 2023/5/5 15:42
# @Author  : ygd
# @FileName: leetcode 347.py
# @Software: PyCharm

'''
leetcode
347. 前 K 个高频元素
mid
https://leetcode.cn/problems/top-k-frequent-elements/
'''

import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = map.get(nums[i], 0) + 1
        small_head = []
        for i, j in map.items():
            heapq.heappush(small_head, (j, i))
            if len(small_head) > k:
                heapq.heappop(small_head)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(small_head)[1])
        return res[::-1]


print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
