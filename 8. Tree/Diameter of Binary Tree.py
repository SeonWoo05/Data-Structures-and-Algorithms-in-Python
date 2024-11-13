def diameter_of_binary_tree(arr):
    def dfs(index):
        # 1. 배열 범위를 벗어나거나 값이 -1인 경우(노드가 없는 경우)
        if index >= len(arr) or arr[index] == -1:
            return 0  # 높이 0 반환

        # 2. 왼쪽과 오른쪽 서브트리의 높이를 재귀적으로 계산
        left_height = dfs(2 * index + 1)  # 왼쪽 자식
        right_height = dfs(2 * index + 2)  # 오른쪽 자식

        # 3. 지름 계산: 현재 노드를 루트로 하는 경로의 길이
        diameter[0] = max(diameter[0], left_height + right_height)  # 최대 지름 갱신

        # 4. 현재 노드의 높이를 반환
        return max(left_height, right_height) + 1

    # 결과를 저장할 리스트
    diameter = [0]  # 리스트로 지름 저장
    dfs(0)  # 루트 노드(인덱스 0)에서 탐색 시작
    return diameter[0]

# 입력 처리
arr = list(map(int, input().split()))  # 배열로 표현된 트리
print(diameter_of_binary_tree(arr))
