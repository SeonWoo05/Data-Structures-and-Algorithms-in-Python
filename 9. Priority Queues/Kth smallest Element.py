# 가장 작은 K번째 원소 찾기

import heapq

nums = list(map(int, input().split()))
k = int(input())

heap = [-x for x in nums[:k]] # k개 원소만 받아서 heap에 넣고

heapq.heapify(heap) # 가장 작은 원소가 맨 위에 있음 (사실은 가장 큰 원소)

for num in nums[k:]:
    if -heap[0] > num:
        heapq.heappushpop(heap,-num)

print(-heap[0])