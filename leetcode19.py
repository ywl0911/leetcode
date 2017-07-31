# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        if length == 1:
            return None
        if n == length:
            return head.next
        current = head
        for i in range(length - n - 1):
            current = current.next

        current.next = current.next.next
        return head    