# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return []
        length = 0
        l = head
        while l:
            l = l.next
            length += 1

        if k > length:
            k = k % length

        current = head
        while current.next:
            current = current.next

        current.next = head

        for i in range(length - k):
            current = current.next

        head = current.next
        current.next = None
        return head
