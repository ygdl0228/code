# @Time    : 2023/4/24 16:15
# @Author  : ygd
# @FileName: leetcode 1248.py
# @Software: PyCharm

'''
leetcode
1248. 统计「优美子数组」
mid
https://leetcode.cn/problems/count-number-of-nice-subarrays/
'''


class Solution:
    def numberOfSubarrays(self, nums, k):
        dic = {0:1}
        sum = 0
        res = 0
        for num in nums:
            sum += 1 if num % 2 == 1 else 0
            res += dic.get(sum - k, 0)
            dic[sum] = dic.get(sum, 0) + 1
        return res


print(Solution().numberOfSubarrays([1, 1, 2, 1, 1], 3))
