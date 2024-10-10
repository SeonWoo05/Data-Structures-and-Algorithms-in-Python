# 기본동작 - Middle

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head): # 연결리스트는 노드들이 연속적으로 연결되어 있기 때문에,
                                # head 노드만 있으면 그 노드에서 시작하여 리스트의 전체를 접근할 수 있다
        total_count = 0
        crnt_node = head

        while crnt_node:
            total_count += 1
            crnt_node = crnt_node.next
        
        half_count = int(total_count / 2) # 원소가 홀수 => 중간 원소 살리기 위해 
        crnt_node = head
        
        for i in range(0, half_count):
            crnt_node = crnt_node.next
        
        return crnt_node