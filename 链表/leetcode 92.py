# @Time    : 2023/5/16 16:40
# @Author  : ygd
# @FileName: leetcode 92.py
# @Software: PyCharm

'''
leetcode
92. 反转链表 II
mid
https://leetcode.cn/problems/reverse-linked-list-ii/
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for _ in range(left - 1):
            pre = pre.next
        cur = pre.next
        for _ in range(right-left):
            tmp=cur.next
            cur.next=tmp.next
            tmp.next = pre.next
            pre.next = tmp
        return dummy.next