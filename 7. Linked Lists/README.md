# Linked List

## Linked List 개요
- **연결리스트(Linked List)** : 노드(Node)들이 링크(Link)를 통해 연결된 순차적 자료구조
- 데이터를 **연속적인** 메모리 공간에 저장하고, 각 요소(element)는 인덱스를 이용하여 **임의접근**하는 배열, 리스트와는 다르게 **헤드노드**에서부터 link를 따라 원하는 노드의 데이터를 접근하고 수정
- **삽입과 삭제**에서 배열에 비해 시간 복잡도가 낮음  
특히, 삽입과 삭제에서 **O(1)**의 시간 복잡도를 가짐  
하지만 순차 탐색에서는 **O(n)** 시간이 소요됨 (random access를 제공하지 않음)

## 연결리스트의 종류
1. **한방향 연결리스트(Singly Linked List)** :
   - 노드들이 한쪽 방향으로만 연결된 리스트
   - 각 노드는 **데이터**와 **다음 노드에 대한 참조**를 포함
   - **삽입과 삭제**가 효율적이나, 탐색은 느림
   - 시간 복잡도:
     - 삽입, 삭제: O(1)
     - 탐색: O(n)

2. **양방향 연결리스트(Doubly Linked List)** :
   - 각 노드가 **이전 노드와 다음 노드**에 대한 참조를 포함하여 양방향으로 연결된 리스트
   - **앞쪽과 뒤쪽**에서 모두 탐색할 수 있어 효율적
   - 시간 복잡도:
     - 삽입, 삭제: O(1)
     - 탐색: O(n)

3. **원형 연결리스트(Circular Linked List)** :
   - 마지막 노드가 다시 **첫 번째 노드**를 가리키는 리스트.
   - **모든 노드**가 서로 연결되어 순환 구조를 이룹니다.
   - 시간 복잡도:
     - 삽입, 삭제: O(1)
     - 탐색: O(n)

## 한방향 연결리스트(Singly Linked List)의 구현
```python
class SList:
    class Node:
        __slots__ = 'element', 'next'
        
        def __init__(self, element, next=None):
            self.element = element  # 노드가 저장하는 데이터
            self.next = next  # 다음 노드를 가리키는 링크

    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def insert_front(self, element):
        self.head = self.Node(element, self.head)
        self.size += 1
    
    def delete_front(self):
        if self.is_empty():
            raise Exception('Underflow')
        self.head = self.head.next
        self.size -= 1

    def search(self, target):
        p = self.head
        while p:
            if p.element == target:
                return True
            p = p.next
        return False
```
