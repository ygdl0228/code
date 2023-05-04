# @Time    : 2023/5/4 9:51
# @Author  : ygd
# @FileName: leetcode 207.py
# @Software: PyCharm

'''
leetcode
207. 课程表
mid
https://leetcode.cn/problems/course-schedule/
'''


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if len(prerequisites) == 0:
            return True
        in_drgeen = [0 for _ in range(numCourses)]
        adj = [set() for _ in range(numCourses)]
        quene = []
        nums = 0
        for second, first in prerequisites:
            in_drgeen[second] += 1
            adj[first].add(second)
        for i in range(numCourses):
            if in_drgeen[i] == 0:
                quene.append(i)
        while quene:
            top = quene.pop(0)
            nums += 1
            for i in adj[top]:
                in_drgeen[i] -= 1
                if in_drgeen[i] == 0:
                    quene.append(i)
        return nums == numCourses

print(Solution().canFinish(5,[[1,4],[2,4],[3,1],[3,2]]))