# 기본동작 - Reverse

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if head == None:
            return head
        elif head.next == None:
            return head
        
        crnt_node = head.next
        prev_node = head
        head.next = None # 가장 첫 노드는 거꾸로 올 때 아무것도 가리키지 않음

        while crnt_node:
            tmp_next_node = crnt_node.next
            crnt_node.next = prev_node
            prev_node = crnt_node
            crnt_node = tmp_next_node

        return prev_node