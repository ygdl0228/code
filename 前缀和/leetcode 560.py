# @Time    : 2023/4/24 15:31
# @Author  : ygd
# @FileName: leetcode 560.py
# @Software: PyCharm

'''
leetcode
560. 和为 K 的子数组
mid
https://leetcode.cn/problems/subarray-sum-equals-k/
'''


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0: 1}
        sum, res = 0, 0
        for num in nums:
            sum+=num
            res+=dic.get(sum-k,0)
            dic[sum]=dic.get(sum,0)+1
        return res