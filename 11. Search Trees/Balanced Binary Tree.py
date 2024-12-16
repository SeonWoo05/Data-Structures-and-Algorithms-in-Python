# Leetcode 110

def isBalanced(arr):
    # 빈 트리이면 균형 상태
    if not arr:
        return True
    
    def checkBalance(i):
        # i번 인덱스 노드 기준으로 서브트리의 균형 상태와 높이를 반환
        # 반환값: (isBalanced, height)
        
        # 인덱스 범위를 벗어나거나 -1이면 해당 서브트리는 없으므로 균형이고 높이는 0
        if i >= len(arr) or arr[i] == -1:
            return True, 0
        
        # 왼쪽, 오른쪽 서브트리 검사
        left_balanced, left_height = checkBalance(2*i + 1)
        right_balanced, right_height = checkBalance(2*i + 2)
        
        # 현재 노드의 균형 여부 판단
        # 1. 왼쪽과 오른쪽 서브트리가 모두 균형 상태인지
        # 2. 왼쪽과 오른쪽 서브트리 높이 차이가 1 이하인지
        current_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        current_height = max(left_height, right_height) + 1
        
        return current_balanced, current_height
    
    balanced, _ = checkBalance(0)
    return balanced

arr = list(map(int, input().split()))

print(isBalanced(arr))