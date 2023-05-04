# @Time    : 2023/4/26 20:25
# @Author  : ygd
# @FileName: leetcode 198.py
# @Software: PyCharm

'''
leetcode
198. 打家劫舍
mid
https://leetcode.cn/problems/house-robber/
'''


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0,0
            rb0=max(dfs(root.left)+max(dfs(root.right)))
            rb1=root.val+dfs(root.left)[0]+dfs(root.right)[0]
            return rb0,rb1
        res=dfs(root)
        return max(res)


            rb0=max(dfs(node.left))+max(dfs(node.right))
            rb1=node.val+dfs(node.left)[0]+dfs(node.right)[0]
            return rb0,rb1
        res=dfs(root)
        return max(res)
