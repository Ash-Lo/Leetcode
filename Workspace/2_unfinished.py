# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        tail = dummy

        def add(val1,val2, carry):
            return (val1 + val2 + carry) % 10, (val1 + val2 + carry) // 10

        carry = 0
        while l1 and l2:
            l1.val, carry = add(l1.val, l2.val, carry)
            tail.next = l1
            l1 = l1.next
            l2 = l2.next

        if carry:
            tail.next = ListNode()
            tail = tail.next
            tail.val = carry

        return dummy.next