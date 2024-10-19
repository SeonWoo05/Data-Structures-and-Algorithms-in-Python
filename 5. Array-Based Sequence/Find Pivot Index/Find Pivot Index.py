# Leetcode 724
class Solution(object):
    def pivotIndex(self, nums):
        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            if left_sum == (total_sum - nums[i] - left_sum):
                return i
            left_sum += nums[i]
            
        return -1