# Leetcode 136
class Solution(object):
    def singleNumber(self, nums):
        A = set()
        for i in nums:
            if i in A:
                A.remove(i)
            else:
                A.add(i)
        return A.pop()