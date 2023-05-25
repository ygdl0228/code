# @Time    : 2023/5/25 16:46
# @Author  : ygd
# @FileName: leetcode 239.py
# @Software: PyCharm


'''
leetcode
239. 滑动窗口最大值
hard
https://leetcode.cn/problems/sliding-window-maximum/description/
'''
import heapq


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        ans = []
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)
        ans.append(-q[0][0])
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <=i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])
        return ans


print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
