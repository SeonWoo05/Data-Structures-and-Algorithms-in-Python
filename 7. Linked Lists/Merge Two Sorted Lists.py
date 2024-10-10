# Merge

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # 가짜 헤드 생성
        dummy = ListNode(-1)
        current = dummy
        
        # 두 리스트의 head를 비교하며 병합
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # 남은 리스트가 있다면 그대로 이어 붙임
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # 가짜 헤드 다음 노드를 반환 (실제 병합된 리스트의 시작)
        return dummy.next