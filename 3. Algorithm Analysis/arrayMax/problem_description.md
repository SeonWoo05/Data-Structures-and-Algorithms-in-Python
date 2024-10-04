# n개의 정수 중 최대값
주어진 배열 `A`에서 `n`개의 정수 중 최대값을 찾습니다.

## 문제 풀이 설명
if 문의 결과에 따라 currentMax = A[i]의 실행 여부가 결정됩니다.  

```python
currentMax = A[0]
for i in range(1, n):
    if currentMax < A[i]:
        currentMax = A[i]
```

## 알고리즘의 시간복잡도
최악의 입력에 대한 횟수 분석 : $T(n) = 2n – 1$  
오름차순 정렬이 되어 있어 `currentMax = A[i]`가 매번 실행되는 경우.
