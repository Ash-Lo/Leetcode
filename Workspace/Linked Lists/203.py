# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head , val: int) :
        if not head:
            return None

        dummy = ListNode()
        ptr = dummy
        ptr.next = head
        while ptr:
            if ptr.next.val == val:
                if ptr.next.next:
                    ptr.next = ptr.next.next
                else:
                    ptr.next = None
            ptr = ptr.next
        return dummy.next