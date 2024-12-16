# Leetcode 235

def lowestCommonAncestor(arr, p, q):
    i = 0  # 루트 인덱스
    while i < len(arr) and arr[i] != -1:
        val = arr[i]
        
        # p, q 모두 현재 노드 값보다 작다면 왼쪽으로
        if p < val and q < val:
            i = 2*i + 1
        # p, q 모두 현재 노드 값보다 크다면 오른쪽으로
        elif p > val and q > val:
            i = 2*i + 2
        else:
            # 위 두 조건에 해당하지 않으면, 현재 노드가 LCA
            return val

root = list(map(int, input().split()))
p,q = map(int, input().split())

print(lowestCommonAncestor(root,p,q))