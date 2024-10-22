# Leetcode 496
from collections import deque

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        dq = deque()
        ans = [-1] * len(nums1)

        for num in nums1:
            nums2_idx = nums2.index(num)
            dq.append(nums2_idx)

        for i in range(len(nums1)):
            idx2 = dq.popleft()
            for j in nums2[idx2+1:]:
                if nums2[idx2] < j:
                    ans[i] = j
                    break
                
        return ans
    

# stack 풀이
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater = {}
        
        # nums2를 순회하면서 스택을 사용해 "다음 더 큰 값"을 저장
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        
        # 스택에 남아있는 값들은 "다음 더 큰 값"이 없으므로 -1로 설정
        while stack:
            next_greater[stack.pop()] = -1
        
        # nums1에 대해 정답 배열 생성
        return [next_greater[num] for num in nums1]
