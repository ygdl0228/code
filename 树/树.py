# @Time    : 2023/5/15 22:29
# @Author  : ygd
# @FileName: 树.py
# @Software: PyCharm


'''
https://blog.csdn.net/weixin_42327752/article/details/124381258
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def num_tree(nums, index):
    if index >= len(nums):
        return
    if nums[index] == None:
        return None
    left = index * 2 + 1
    right = index * 2 + 2
    root = TreeNode(nums[index])
    root.left = num_tree(nums, left)
    root.right = num_tree(nums, right)
    return root


nums = [1, 2, 3, None, 4, 5, None]
root = num_tree(nums, 0)


def inorderTraversal(root):
    ans = [root]
    res = []
    while ans:
        n = len(ans)
        for i in range(n):
            node = ans.pop(0)
            res.append(node.val)
            if node.left:
                ans.append(node.left)
            if node.right:
                ans.append(node.right)
    return res

print(inorderTraversal(root))
