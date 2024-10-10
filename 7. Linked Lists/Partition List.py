# 기본동작 - Split

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        before = before_head = ListNode(-1)
        after = after_head = ListNode(-1)

        crnt_node = head

        while crnt_node:
            val = crnt_node.val
            if x <= val:
                after.next = crnt_node
                after = after.next
                crnt_node = crnt_node.next
            else:
                before.next = crnt_node
                before = before.next
                crnt_node = crnt_node.next
        
        after.next = None
        before.next = after_head.next

        return before_head.next