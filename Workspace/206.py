# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev = None
        p1 = head
        while p1 != None:
            temp = p1.next
            p1.next = prev
            prev = p1
            p1 = temp
        return prev