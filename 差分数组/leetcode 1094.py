# @Time    : 2023/4/24 14:16
# @Author  : ygd
# @FileName: leetcode 1094.py
# @Software: PyCharm

'''
leetcode
1094. 拼车
mid
https://leetcode.cn/problems/car-pooling/
'''

class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        trips_sort=sorted(trips,key=lambda x: x[2])
        n=trips_sort[-1][2]
        nums = [0] * (n+1)
        for a,b,c in trips:
            nums[b]+=a
            nums[c]-=a
        for i in range(1,n):
            nums[i]+=nums[i-1]
        if max(nums)>capacity:
            return False
        else:
            return True

print(Solution().carPooling([[2,1,5],[3,3,7]],4))

