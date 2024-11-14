# Leetcode 117

# 깊이란 루트에서 리프까지 경로 상의 노드의 개수를 의미
def MDBT(arr):
    def dfs(index):
        # 1. 배열 범위를 벗어나거나 값이 -1인 경우 (노드가 없는 경우)
        if index >= len(arr) or arr[index] == -1:
            return 0  # 깊이는 0
        
        # 2. 왼쪽과 오른쪽 서브트리의 깊이를 재귀적으로 계산
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        left_depth = dfs(left_index)
        right_depth = dfs(right_index)
        
        # 3. 현재 노드 포함한 깊이를 반환
        return max(left_depth, right_depth) + 1 # 리프노드라면 1이 됨

    # DFS 탐색 시작 (루트 노드부터)
    return dfs(0)

arr = list(map(int, input().split()))
print(MDBT(arr))