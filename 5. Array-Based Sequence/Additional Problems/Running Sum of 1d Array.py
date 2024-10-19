# Leetcode 1480
class Solution(object):
    def runningSum(self, nums):
        sum = nums[0]
        
        for i in range(1,len(nums)):
            sum += nums[i]
            nums[i] = sum

        return nums