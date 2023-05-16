# @Time    : 2023/5/15 22:58
# @Author  : ygd
# @FileName: leetcode 145.py
# @Software: PyCharm

'''
leetcode
145. 二叉树的后序遍历
easy
https://leetcode.cn/problems/binary-tree-postorder-traversal/
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return
        res=[]
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)
        dfs(root)
        return res
