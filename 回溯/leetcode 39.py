# @Time    : 2023/5/10 16:37
# @Author  : ygd
# @FileName: leetcode 39.py
# @Software: PyCharm

'''
leetcode
39. 组合总和
mid
https://leetcode.cn/problems/combination-sum/
'''

from typing import List
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(candidates,begin,size,path,res,target):
            if target<0:
                return
            if target==0:
                res.append(path)
                return
            for index in range(begin,size):
                dfs(candidates,index,size,path+[candidates[index]],res,target-candidates[index])


        size=len(candidates)
        if size==0:
            return []
        res=[]
        path=[]
        dfs(candidates, 0, size, path, res, target)
        return res

