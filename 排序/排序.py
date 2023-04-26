# @Time    : 2023/4/25 16:38
# @Author  : ygd
# @FileName: 排序.py
# @Software: PyCharm

'''
leetcode
912. 排序数组
https://leetcode.cn/problems/sort-an-array/
'''

import math


# 稳定排序，是指在排序算法中，相同值的两个元素，在输入数组中先出现的数在输出数组中也先出现
# 原地排序：基本上不需要额外辅助的的空间

# 选择排序 最好：n^2 最坏 n^2 平均：n^2 原地排序 非稳定
def selectionSort(nums):
    for i in range(len(nums)):
        res = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[res]:
                res = j
        tmp = nums[i]
        nums[i] = nums[res]
        nums[res] = tmp
    return nums


# 插入排序 最好：n 最坏 n^2 平均：n^2 原地排序 稳定
def insertionSort(nums):
    n = len(nums)
    for i in range(1, n):
        while i > 0 and nums[i - 1] > nums[i]:
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
            i -= 1
    return nums


# 冒泡排序 最好：n 最坏 n^2 平均：n^2 原地排序 稳定
def bubble_sort(nums):
    count = 1
    while count == 1:
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count = 1
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums


# 希尔排序 nlogn 原地排序 不稳定

def shell_sort(nums):
    gap = 1
    while (gap < len(nums) / 3):
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, len(nums)):
            temp = nums[i]
            j = i - gap
            while j >= 0 and nums[j] > temp:
                nums[j + gap] = nums[j]
                j -= gap
            nums[j + gap] = temp
        gap = math.floor(gap / 3)
    return nums
