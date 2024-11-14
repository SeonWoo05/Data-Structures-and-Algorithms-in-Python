# Leetcode 236

# 공통 조상 중 최소 공통 조상 찾기
def find_lca(arr, p, q):
    def dfs(index):
        # 1. 배열 범위를 벗어나거나 값이 -1인 경우 (노드가 없는 경우)
        if index >= len(arr) or arr[index] == -1:
            return None

        # 2. 현재 노드가 p나 q라면 바로 반환
        if arr[index] == p or arr[index] == q:
            return arr[index]

        # 3. 왼쪽과 오른쪽 자식을 재귀적으로 탐색
        left = dfs(2 * index + 1)
        right = dfs(2 * index + 2)

        # 4. 왼쪽과 오른쪽에서 각각 p와 q를 찾았다면 현재 노드가 LCA
        if left and right: # 이 부분은 p,q를 찾고나서 공통조상.
            return arr[index]

        # 5. 둘 중 하나라도 찾았으면 반환
        return left if left else right # 이 부분은 다 못찾아서 다른 경로 탐색할 때.

    # DFS를 루트(인덱스 0)부터 시작
    return dfs(0) # 루트부터 시작해서 4번 조건 만족하는 값 리턴하게 됨

arr = list(map(int, input().split()))
p, q = map(int, input().split())

# LCA 찾기
lca = find_lca(arr, p, q)
print(lca)
