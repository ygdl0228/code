# @Time    : 2023/5/10 16:55
# @Author  : ygd
# @FileName: leetcode 40.py
# @Software: PyCharm

'''
leetcode
40. 组合总和 II
mid
https://leetcode.cn/problems/combination-sum-ii/
'''


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(begin, path, residue):
            if residue == 0:
                res.append(path[:])
                return
            for index in range(begin, size):
                if candidates[index] > residue:
                    break
                if index > begin and candidates[index] == candidates[index - 1]:
                    continue
                path.append(candidates[index])
                dfs(index + 1, path, residue - candidates[index])
                path.pop()

        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        res = []
        dfs(0, [], target)
        return res
