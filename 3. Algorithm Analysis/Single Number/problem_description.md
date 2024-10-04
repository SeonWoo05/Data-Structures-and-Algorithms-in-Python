# 1개만 존재하는 원소
주어진 배열 `nums`에서 1개만 존재하는 원소를 찾습니다.

## 문제 풀이 설명
• Hash set 안에 해당 숫자가 없으면 추가  
• 이미 해당 숫자가 있으면 해당숫자를 삭제  
• 마지막에 hash set 안에 남는 숫자가 정답

```python
A = set()
for i in nums:
    if i in A:
        A.remove(i)
    else:
        A.add(i)
```

## 알고리즘의 시간복잡도
$T(n) = 2n – 1$