# Leetcode 215

import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        
        # nums의 처음 k개의 원소로 최소 힙 생성
        heap = nums[:k]
        heapq.heapify(heap)
        
        # 배열의 나머지 원소들을 순회하며 처리
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappushpop(heap, num)
        
        # 힙의 루트가 k번째로 큰 원소
        return heap[0]