# Definition for singly-linked list.
import copy

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
        List_new = ListNode(None)

        c = 0
        p = List_new
        while l1 != None or l2 != None:
            if l1 == None:
                a = 0
            else:
                a = l1.val
                l1 = l1.next

            if l2 == None:
                b = 0
            else:
                b = l2.val
                l2 = l2.next

            d = (a + b + c) % 10
            c = int((a + b + c) / 10)

            p.next = ListNode(d)
            p = p.next

        if c > 0:
            p = List_new
            while p.next != None:
                p = p.next
            p.next = ListNode(c)
        return List_new.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(8)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

s = Solution()
aa = s.addTwoNumbers(l1, l2)
