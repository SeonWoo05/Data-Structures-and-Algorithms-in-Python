# Leetcode 203

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode(-1)
        dummy.next = head
        crnt = dummy

        while crnt.next != None:
            if crnt.next.val == val:
                crnt.next = crnt.next.next
            else:
                crnt = crnt.next

        return dummy.next