# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):

        ## Using extra memory
        my_list = []
        temp = head
        if not head:
            return  None
        while temp:
            my_list.append(temp.val)
            temp = temp.next
        if len(my_list) % 2: val = len(my_list) // 2
        else: val = (len(my_list) // 2) + 1
        while val:
            head = head.next
            val -= 1
        return head