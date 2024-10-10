# 기본동작 - Reorder

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        if not head:
            return
        
        # find the middle of linked list [Problem 876]
        # in 1->2->3->4->5->6 find 4
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second part of the list [Problem 206]
        # convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
        # reverse the second half in-place
        prev_node, crnt_node = None, slow
        while crnt_node:
            tmp_next_node = crnt_node.next
            crnt_node.next = prev_node
            prev_node = crnt_node
            crnt_node = tmp_next_node
        
        # merge two sorted linked lists [Problem 21]
        # merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
        first, second = head, prev_node
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        
        return head