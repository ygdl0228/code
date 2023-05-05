# @Time    : 2023/5/5 15:25
# @Author  : ygd
# @FileName: leetcode 218.py
# @Software: PyCharm

'''
leetcode
218. 天际线问题
hard
https://leetcode.cn/problems/the-skyline-problem/description/
'''


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        length = buildings[-1][1]
        nums = [0 for _ in range(length + 1)]
        for i in buildings:
            nums[i[0]:i[1]] = [i[2] for _ in range(i[1]-i[0])]
        return nums
print(Solution().getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
