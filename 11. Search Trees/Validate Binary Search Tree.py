# Leetcode 98
import math

def isBST(arr):
    if not arr:
        return True
    
    def validate(i, low, high):
        if i >= len(arr) or arr[i] == -1:
            return True
        
        val = arr[i]

        if not (low < val < high):
            return False
        
        left_idx = 2*i + 1
        right_idx = 2*i + 2

        # 왼쪽 서브트리는 최대 범위를 val로
        # 오른쪽 서브트리는 최소 범위를 val로
        return validate(left_idx, low, val) and validate(right_idx, val, high)

    return validate(0, -math.inf, math.inf)

arr = list(map(int, input().split()))

print(isBST(arr))