# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        current = head

        p_less_x = p_less_x_head = ListNode(1)
        p_more_x = p_more_x_head = ListNode(1)

        while current:
            # print current.val
            if current.val < x:
                p_less_x.next = current
                p_less_x = p_less_x.next

            else:
                p_more_x.next = current
                p_more_x = p_more_x.next

            current = current.next

        p_more_x.next = None

        p_less_x.next = p_more_x_head.next

        # helper.next=p_less_x_head.next

        return p_less_x_head.next