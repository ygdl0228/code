# @Time    : 2023/5/16 16:34
# @Author  : ygd
# @FileName: leetcode 206.py
# @Software: PyCharm

'''
leetcode
206. 反转链表
easy
https://leetcode.cn/problems/reverse-linked-list/
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        per=None
        cur=head
        while cur:
            tmp=cur.next
            cur.next=per
            per=cur
            cur=tmp
        return per