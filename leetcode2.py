# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        current1 = l1
        current2 = l2
        l = ListNode(0)
        current = l
        jinwei = 0
        while current1 and current2:
            val = (current1.val + current2.val + jinwei) % 10

            jinwei = (current1.val + current2.val + jinwei) // 10
            current.next = ListNode(val)
            current = current.next
            current1 = current1.next
            current2 = current2.next

        while current1:
            val = (current1.val + jinwei) % 10

            jinwei = (current1.val + jinwei) // 10
            current.next = ListNode(val)
            current = current.next
            current1 = current1.next

        while current2:
            val = (current2.val + jinwei) % 10

            jinwei = (current2.val + jinwei) // 10
            current.next = ListNode(val)
            current = current.next
            current2 = current2.next

        if jinwei > 0:
            current.next = ListNode(jinwei)

        return l.next