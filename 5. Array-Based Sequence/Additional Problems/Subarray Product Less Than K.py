# Leetcode 713
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        left = 0
        prod = 1
        cnt = 0

        for right in range(len(nums)):
            prod *= nums[right]

            # prod가 k 이상인 경우, left를 오른쪽으로 이동시키며 곱을 줄임
            while prod >= k and left <= right:
                prod /= nums[left]
                left += 1

            # 현재 right와 left 사이의 모든 부분 배열을 카운트
            cnt += right - left + 1 # right를 포함한 모든 부분 배열 센 것
            # ex) [10] 1개 , [10,5] 2개 , ...
        
        return cnt