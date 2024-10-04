# 자료구조와 알고리즘의 성능분석

## 자료구조와 알고리즘의 성능(performance):
• 1. 수행 시간을 나타내는 시간복잡도(time complexity)  
• 2. 사용되는 메모리 공간의 크기를 나타내는 공간복잡도(space complexity)

## 알고리즘의 시간복잡도
• 알고리즘의 수행시간 = 최악의 경우의 입력에 대한 기본연산의 수행횟수(time complexity) : $T(n)$

## Big-Oh 표기법
• 정확한 횟수보다는 입력의 크기 `n`이 커질때, 수행시간의 증가하는 정도(rate of the growth of T(n) as n goes big)가 훨씬 중요하다.  
• 최고차항(가장 빨리 증가하는 항)만을 남기고 나머지는 생략하는 식으로 수행시간을 간략히 표기하는 방법을 점근표기법(asymptotic notation)이라고 부르고, Big-O(대문자 O)를 이용하여 다음의 예처럼 표기한다.  
$T(n) = 2n + 5 → T(n) = O(n)$  
$T(n) = 3n^2 + 12n - 6 → T(n) = O(n^2)$

### python으로 기술한 코드의 수행시간
• O(`1`) 시간 알고리즘(constant time algorithm) :  
값을 1 증가시킨 후 리턴

```python
def increment_one(a): 
    return a+1
```

• O($log n$) 시간 알고리즘(logarithmic time algorithm); log의 밑은 2 :  
십진수 `n`을 이진수로 표현할 때 필요한 비트 개수 계산 알고리즘

```python
def number_of_bits(n): 
    count = 0 
    while n > 0: 
        n = n // 2
        count += 1 
    return count
```

• O(`n`) 시간 알고리즘(linear time algorithm) :  
n개의 수 중에서 최대값을 찾는 알고리즘  

• O($n^2$) 시간 알고리즘(quadratic time algorithm) :  
두 배열 A, B의 모든 정수쌍의 곱의 합을 계산하는 알고리즘

```python
def algorithm array_sum(A, B, n) 
    sum = 0 
    for i = 0 to n - 1 do 
        for j = 0 to n - 1 do 
            sum += A[i]*B[j] 
    return sum
```

• O($2^n$) 이상의 시간이 필요한 알고리즘(exponential time algorithm) :  
피보나치수 k를 계산하는 재귀 알고리즘

```python
def fibonacci(k): 
    if k <= 1: return k 
    return fibonacci(k-1) + fibonacci(k-2)
```