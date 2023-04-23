# @Time    : 2023/4/23 15:39
# @Author  : ygd
# @FileName: leetcode 729.py
# @Software: PyCharm

'''
leetcode
线段树
729. 我的日程安排表 I
mid 没明白
https://leetcode.cn/problems/my-calendar-i/description/?languageTags=python
'''


class MyCalendar(object):

    def __init__(self):
        self.tree = set()
        self.lazy = set()

    def quary(self, start, end, l, r, idx):
        if r < start and end < l:
            return False
        if idx in self.lazy:
            return True
        if start <= l and end >= r:
            return idx in self.tree
        mid = (l + r) // 2
        return self.quary(start, end, l, mid, 2 * idx) or self.quary(start, end, mid + 1, r, 2 * idx + 1)

    def update(self, start, end, l, r, idx):
        if r < start and end < l:
            return
        if start <= l and end >= r:
            self.tree.add(idx)
            self.lazy.add(idx)
        else:
            mid = (l + r) // 2
            self.quary(start, end, l, mid, 2 * idx)
            self.quary(start, end, mid + 1, r, 2 * idx)
            self.tree.add(idx)
            if 2 * idx in self.lazy and 2 * idx + 1 in self.lazy:
                self.lazy.add(idx)

    def book(self, start, end):
        # 检查与已有日期是否冲突
        if self.quary(start, end - 1, 0, 10 ** 9, 1):
            return False
        # 没有冲突 添加到数组中
        self.update(start, end - 1, 0, 10 ** 9, 1)
        return True
