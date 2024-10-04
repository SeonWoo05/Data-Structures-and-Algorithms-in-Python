# 자료구조와 알고리즘의 성능분석

## 자료구조와 알고리즘의 성능(performance):
• 1. 수행 시간을 나타내는 시간복잡도(time complexity)  
• 2. 사용되는 메모리 공간의 크기를 나타내는 공간복잡도(space complexity)

## 알고리즘의 시간복잡도
• 알고리즘의 수행시간 = 최악의 경우의 입력에 대한 기본연산의 수행횟수(time complexity) :$T(n)$

## Big-Oh 표기법
• 정확한 횟수보다는 입력의 크기 `n`이 커질때, 수행시간의 증가하는 정도(rate of the growth of T(n) as n goes big)가 훨씬 중요하다.  
• 최고차항(가장 빨리 증가하는 항)만을 남기고 나머지는 생략하는 식으로 수행시간을 간략히 표기하는 방법을 점근표기법(asymptotic notation)이라고 부르고, Big-O(대문자 O)를 이용하여 다음의 예처럼 표기한다.  
$T(n) = 2n + 5 → T(n) = O(n)$  
$T(n) = 3n^2 + 12n - 6 → T(n) = O(n^2)$