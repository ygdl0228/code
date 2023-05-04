# @Time    : 2023/5/4 9:51
# @Author  : ygd
# @FileName: leetcode 210.py
# @Software: PyCharm

'''
leetcode
210. 课程表 II
mid
https://leetcode.cn/problems/course-schedule-ii/
'''


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        res = []
        quene = []
        in_drgeen = [0 for _ in range(numCourses)]
        adj = [set() for _ in range(numCourses)]
        for second, first in prerequisites:
            in_drgeen[second] += 1
            adj[first].add(second)
        for i in range(numCourses):
            if in_drgeen[i] == 0:
                quene.append(i)
        nums=0
        while quene:
            top = quene.pop(0)
            res.append(top)
            nums+=1
            for i in adj[top]:
                in_drgeen[i]-=1
                if in_drgeen[i] == 0:
                    quene.append(i)
        return res if nums==numCourses else []

