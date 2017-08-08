class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        helper = ListNode(1)
        helper.next = head

        pre = helper
        current = head

        while current:
            while current.next:
                if current.val == current.next.val:
                    current = current.next
                else:
                    break
            if pre.next == current:
                pre = pre.next
            else:
                pre.next = current.next
            current = current.next

        return helper.next
