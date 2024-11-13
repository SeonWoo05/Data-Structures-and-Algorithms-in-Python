# Leetcode 113

def find_paths(arr, targetSum):
    def dfs(index, current_sum, path):
        # 1. 배열 범위를 벗어나거나 값이 -1인 경우(노드가 없는 경우)
        if index >= len(arr) or arr[index] == -1:
            return
        
        # 2. 현재 노드를 경로에 추가하고 합계 갱신
        path.append(arr[index])
        current_sum += arr[index]
        
        # 3. 왼쪽 자식과 오른쪽 자식의 인덱스 계산
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        
        # 4. 리프 노드인지 확인
        if left_index >= len(arr) and right_index >= len(arr):
            # 조건을 만족하면 결과에 경로 추가
            if current_sum == targetSum:
                result.append(list(path))
        
        # 5. 왼쪽과 오른쪽 서브트리 탐색
        dfs(left_index, current_sum, path)
        dfs(right_index, current_sum, path)
        
        # 6. 백트래킹 - 현재 노드를 경로에서 제거
        path.pop() # 이후 탐색에서 path를 이전 상태로 복원

    # 결과를 저장할 리스트
    result = []
    dfs(0, 0, []) # index 0 , current_sum 0 , path []
    return result

# 입력 처리
arr = list(map(int, input().split()))  # 배열로 표현된 트리
targetSum = int(input())

# 함수 실행 및 결과 출력
paths = find_paths(arr, targetSum)
print(paths)
