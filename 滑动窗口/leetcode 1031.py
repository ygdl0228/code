# @Time    : 2023/4/26 16:36
# @Author  : ygd
# @FileName: leetcode 1031.py
# @Software: PyCharm

'''
leetcode
1031. 两个非重叠子数组的最大和
mid
https://leetcode.cn/problems/maximum-sum-of-two-non-overlapping-subarrays/description/
'''


class Solution:
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        return max(self.help(nums, firstLen, secondLen), self.help(nums, secondLen, firstLen))

    def help(self, nums, firstLen, secondLen):
        suml = 0
        sumr = 0
        res = 0
        for i in range(0, firstLen):
            suml += nums[i]
        maxsuml = suml
        for i in range(firstLen, firstLen + secondLen):
            sumr += nums[i]
        res = sumr + maxsuml
        j = firstLen
        for i in range(firstLen + secondLen, len(nums)):
            suml += nums[j] - nums[j - firstLen]
            maxsuml = max(suml, maxsuml)
            sumr += nums[i] - nums[i - secondLen]
            res = max(res,maxsuml+sumr)
            j += 1
        return res


print(Solution().maxSumTwoNoOverlap([3, 8, 1, 3, 2, 1, 8, 9, 0], 3, 2))
