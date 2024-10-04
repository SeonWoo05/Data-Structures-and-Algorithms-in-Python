# n개의 정수 중 최대값
주어진 배열 `A`에서 `n`개의 정수 중 최대값을 찾습니다.

## 문제 풀이 설명
다음 코드는 `if` 문을 사용하여 배열의 각 요소와 현재까지의 최대값을 비교합니다. 

```python
currentMax = A[0]
for i in range(1, n):
    if currentMax < A[i]:
        currentMax = A[i]