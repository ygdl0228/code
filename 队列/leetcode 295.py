# @Time    : 2023/5/5 19:33
# @Author  : ygd
# @FileName: leetcode 295.py
# @Software: PyCharm

'''
leetcode
295. 数据流的中位数
hard
https://leetcode.cn/problems/find-median-from-data-stream/description/
'''

import heapq


class MedianFinder:

    def __init__(self):
        self.queMin = list()
        self.queMax = list()

    def addNum(self, num: int) -> None:

        if not self.queMin or num <= -self.queMin[0]:
            heapq.heappush(self.queMin, -num)
            if len(self.queMax) + 1 < len(self.queMin):
                heapq.heappush(self.queMax, -heapq.heappop(self.queMin))
        else:
            heapq.heappush(self.queMax, num)
            if len(self.queMax) > len(self.queMin):
                heapq.heappush(self.queMin, -heapq.heappop(self.queMax))

    def findMedian(self) -> float:
        if len(self.queMin) > len(self.queMax):
            return -self.queMin[0]
        return (-self.queMin[0] + self.queMax[0]) / 2

