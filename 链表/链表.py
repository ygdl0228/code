# @Time    : 2023/5/15 22:35
# @Author  : ygd
# @FileName: 链表.py
# @Software: PyCharm

'''
https://blog.csdn.net/weixin_42327752/article/details/124381258
'''


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def num_ListNode(nums):
    dummy = ListNode(None)
    root = ListNode(nums[0])
    dummy.next = root
    i = 1
    while i < len(nums):
        node = ListNode(nums[i])
        root.next = node
        root = root.next
        i += 1
    root.next = None
    return dummy.next


res = []
nums = [1, 2, 3, 4, 5]
root = num_ListNode(nums)
while root:
    res.append(root.val)
    root = root.next
print(res)
